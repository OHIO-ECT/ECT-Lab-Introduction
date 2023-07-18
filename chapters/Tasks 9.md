## ECT Lab Introduction - Wireshark

### Goals
-   Configure Remote Desktop to connect to the lab environment
-   Learn the basic setup of the GNS3 virtual lab environment
-   Overview of Windows and Unix operating systems
-   Introduction to the CLI, and the interaction with filesystems
-   Become familiar with the Linux command line terminal (bash shell)

### Pre-Lab
- Homework/Labs/Projects will often have associated ECT Tech Nuggets that are recommended viewing after reading the lab the first time but before starting the work on the lab.  Do **NOT** follow along with the ECT Tech Nuggets while watching them for the first time. Watch the video and use what you have learned. - Windows is the only OS that is officially supported, but other OS's may be possible. 
<br>
- Watch the the following [ECT Tech Nuggets](https://www.youtube.com/@ecttechnuggets9126/featured) videos on YouTube:
    - GNS3 Introduction - [ECT Tech Nugget N1.1 GNS3]
    - [ECT Tech Nugget - N34.0 - Technology Perspective](https://youtu.be/ixrzbdUu8yQ)
    - Remote Desktop Connection
        - Windows Users: [ECT Tech Nugget N14.1 RDC Connections](https://youtu.be/H52fC9hCmdk)
        - Apple Users: [ECT Tech Nugget N17.0 RDC and RD Gateway Apple Mac OSX](https://youtu.be/g1oYzEham8c)
        - RD Gateway IP/Hostname: ```its-s15.its.ohio.edu```

### Resources

- Personal Computer (Destkop or Laptop)
- A document you have created to use as a lab notebook
- Assigned gHost (GNS3 Virtual Machine)
- [ECT/ITS Lab Notebook Cheatsheet](https://github.com/OHIO-ECT/Lab-Notebook-Cheat-Sheet)
- Additional [ECT Tech Nuggets](https://www.youtube.com/@ecttechnuggets9126/featured):
  - [ECT Tech Nugget N0.1 Basic Diagnostic Tools 1](https://youtu.be/_pRXauSnU6U)
  - [ECT Tech Nugget N0.2 Basic Diagnostic Tools 2](https://youtu.be/hWeJlNVaUbU)
  - [ECT Tech Nugget N0.3 Basic Diagnostic Tools 3](https://youtu.be/PMk53TngTio)
  - [ECT Tech Nugget N0.4 Basic Diagnostic Tools 4](https://youtu.be/gD-Tk1Bk7x0)
  - [ECT Tech Nugget N0.5 Basic Diagnostic Tools 5](https://youtu.be/QTIbS9wyfag)
  - [ECT Tech Nugget N11.0 NMCLI](https://youtu.be/43F51qVz9Ds)

### Network Diagram

![](./images/lab1-pic2-1.png)

### Toolkit

-   Shells (i.e. Powershell, Bash)
-   SSH (i.e. Secure Shell)
-   Commands to be typed by the student and output from shells are indicated within this document in the ``fixed width font Courier New`` (as shown here).
-   Varibles to be filled in by the student are presented in ``<brackets>``. The student will need to replace the <> and the text with the needed varible. Example: **My name is ``<Name>``**. Would change to **My name is Bob.**
-   Find a Print Screen / Screen Capture tool that you like. The following is a list of tools known to work:
    -   Lightshot <https://app.prntscr.com>
    -   Greenshot <https://getgreenshot.org>

### Task 9 - Wireshark

Wireshark is a packet capture tool available on Linux, Mac and Windows for free. This means that it will capture traffic (all or some) that comes to or leaves a NIC on the machine. We will be looking at pre-captured data as an example. From files listed above (i.e. in this repo), download the ITL sample file called `Lab 01 - ITLsample.pcap`. See [ECT ECT Tech Nugget N0.5 Basic Diag Tools 5 Wireshark][ECT Tech Nugget N0.5 Basic Diagnostic Tools 5] for more detail about Wireshark.

43. Install Wireshark on **your** machine, if not installed already: http://www.wireshark.org/download.html. Install the current stable release.
<br>

44. From the list of files listed at the top of this page download "ITS-Wireshark-Sample.pcap". Start Wireshark and open the "ITS-Wireshark-Sample.pcap" file using File/Open options. Note that you may not get Wireshark to start by double-clicking a capture file.

#### Wireshark MAC Address Information

45. In Wireshark the summary lines are the lines of data shown in the top frame of Wireshark. To select a packet, click anywhere on the summary line.
<br>

46. Scroll down to packet 58. This machine is trying to match the IP address 132.235.233.254 to the corresponding Ethernet (MAC) address using the ARP protocol. The next packet (59) contains the answer, right on the summary line in the top Wireshark window.

#### Wireshark Filtering for Specific IP

47. Rather than searching through the raw data, display filters are used to help find types of packets. Look for:
`Apply a display filter ... <Ctrl-/>` 
text box near the top of the Wireshark window. 
    - In the filter window use the filter `ip.addr==132.235.232.204`
    - The field should turn green showing that this is a valid filter. 
    - Press Enter to apply filer. To reset the view, use the "X" button on the far right of the filter line.

48. In the filtered view, look for a packet with `Echo (ping) Request`.
<br>

49. Use the `View` menu and select `Expand All`. Notice that the middle frame expands the packet data to show **a lot** of detail.
<br>

50. To get packet detail needed into a format where portions of it are can be used in a lab report use `File -> Export Packet Dissections -> As Plain Text...`
<br>

51. A Wireshark Save dialog window will open with serveral choices along the bottom. 
    - In the lower left called `Packet Range` change the radio button to `Selected packet`
    - In the lower right called `Packet Format` make sure the `Packet summary line`,`Include column headings` and `Packet details: As Displayed` options are checked (checked by default)
<br>

52. Select a location and name for the file. Pressing the Save button will create a **TEXT** file for use in a lab report. The packet text output may need some formatting before using it in an assignment.
<br>

53. For more detail about how to export data for lab reports see [ECT Wireshark Export Guide](https://github.com/OHIO-ECT/Wireshark-Export-Guide).

#### GNS3 Wireshark

Using Wireshark to sniff packets in a GNS3 project can be very helpful when diagnosing issues. The procedure is shown in [ECT Tech Nugget - N1.1 - GNS3](https://youtu.be/w5qsM3LhpQI) (scrub to 9:49) for details. Wireshark functions a bit different in a GNS3 environment. It's a two part process. Right-Clicking on a link and selecting "Start Capture" will start the packet capture program on the link **and** start Wireshark to view the the packets. The problem is that stopping Wireshark **does not** stop the packet capture program. This means will will keep running collecting packets! After enough time the gHost will run out of memory and crash if the packet capture program isn't stopped. To stop the capture program, right-click on the link again and select "Stop Capture".

54. In the running GNS3 project right-click on the link between the Ubuntu-GUI-1 and the switch. In the context menu select `Start Capture` and press OK on the popup dialog box to begin packet capture (AKA packet sniffing). Wireshark GUI will auto-start and begin showing packet data for traffic going to or from the Ubuntu-GUI-1 object. A small magnifiying glass icon will appear in GNS3 on the link.
<br>

55. In the Wireshark display filter use the following filter: `ip.addr==X.X.X.X`. Make sure to replace `X.X.X.X` with the IP for the Ubuntu-GUI-1 that was discovered earlier. This filter display only traffic going to or from the specified IP (Ubuntu-GUI-1 in this case). 
<br>

56. On Ubuntu-GUI-1 open a terminal window and `ping 8.8.8.8`. Allow it to run for five ping iterations and use CTRL+C to stop ping.
<br>

57. Go back to Wireshark and find those five ping packets (there should also be five responses).
<br>

58. Stop the capture process (not Wireshark). Right-click on the link with the magnifiying glass, in the context menu select `Stop Capture`. This will stop **new** packets from showing up in Wireshark.
<br>

59. On the filter line in Wireshark add the following to the end after the current filter ` && icmp`. The complete filter will be:

    ``ip.addr==X.X.X.X && icmp``

    This filters the results even further to show only packets from the specified IP **and** packets that are ICMP (ping packets in this case).
