# Wireshark

## Goals
- Learn to use Wireshark to packet sniff network traffic
- Use Wireshark filters to search specific types or qualities of traffic

## Pre-Lab

- Watch the the following [ECT Tech Nuggets](https://www.youtube.com/@ecttechnuggets9126/featured) videos on YouTube:
    - [ECT Tech Nugget N0.5 Basic Diagnostic Tools 5](https://youtu.be/QTIbS9wyfag)

## Resources

- Personal Computer (Desktop or Laptop)
- A document you have created to use as a lab notebook
- Assigned gHost (GNS3 Virtual Machine)
- [ECT/ITS Lab Notebook Cheatsheet](https://github.com/OHIO-ECT/Lab-Notebook-Cheat-Sheet)

## Environmental Context

- Connection to gHost VM
- Running "98 - Intro Lab" GNS3 project
- Child VMs are started and ready for use

## Personal Computer Wireshark

Wireshark is a packet capture tool available on Linux, Mac and Windows for free.  See [ECT Tech Nugget N0.5 Basic Diag Tools 5 Wireshark](https://youtu.be/QTIbS9wyfag) for more detail about Wireshark.  Wireshark may be used in several contexts with the student's ecosystem.  Including on the the student's Personal Computer, within GNS3, and with GNS3 objects.

1. Install Wireshark on **your** machine, if not installed already: http://www.wireshark.org/download.html. Install the current stable release.
<br>

2. When Wireshark first starts it requests the user to select the interface to capture on.  Wait 20 to 30 seconds and look for an interface with traffic on the the associated graph, and double click on that interface to start the packet capture.  Stop the capture and explore the interface.  DO NOT LEAVE WIRESHARK CAPTURING PACKETS.  It will cause significant memory issues for the device that it is running on.

3. Wireshark can save packets in an industry standard libpcap format for later processing.  Students will regularly capture data on the gHost to be processed later on the student PC. From the list of files listed at the top of this page download [ITS-Wireshark-Sample.pcap](../files/ITS-Wireshark-Sample.pcap). Start Wireshark and open the "ITS-Wireshark-Sample.pcap" file using File/Open options. Note that you may not get Wireshark to start by double-clicking a capture file.  The data in this file will be used for the remainder of this task.

## Wireshark MAC Address Information

4. In Wireshark the summary lines are the lines of data shown in the top frame of Wireshark. To select a packet, click anywhere on the summary line.
<br>

5. Scroll down to packet 58. This machine is trying to match the IP address 132.235.233.254 to the corresponding Ethernet (MAC) address using the ARP protocol. The next packet (59) contains the answer, right on the summary line in the top Wireshark window.

## Wireshark Filtering and exporting

6. Rather than searching through the raw data, display filters are used to help find types of packets. Look for:
`Apply a display filter ... <Ctrl-/>` 
text box near the top of the Wireshark window. 
    - In the filter window use the filter `ip.addr==132.235.232.204`
    - The field should turn green showing that this is a valid filter. 
    - Press Enter to apply filer. To reset the view, use the "X" button on the far right of the filter line.

7. In the filtered view, look for a packet with `Echo (ping) Request`.
<br>

8. Use the `View` menu and select `Expand All`. Notice that the middle frame expands the packet data to show **a lot** of detail.
<br>

9. To get packet detail needed into a format where portions of it are can be used in a lab report use `File -> Export Packet Dissections -> As Plain Text...`
<br>

10. A Wireshark Save dialog window will open with several choices along the bottom. 
    - In the lower left called `Packet Range` change the radio button to `Selected packet`
    - In the lower right called `Packet Format` make sure the `Packet summary line`,`Include column headings` and `Packet details: As Displayed` options are checked (checked by default)
<br>

11. Select a location and name for the file. Pressing the Save button will create a **TEXT** file for use in a lab report. The packet text output may need some formatting before using it in an assignment.
<br>

12. For more detail about how to export data for lab reports see [ECT Wireshark Export Guide](https://github.com/OHIO-ECT/Wireshark-Export-Guide).

## GNS3 Wireshark

Using Wireshark to sniff packets in a GNS3 project can be very helpful when diagnosing issues. The procedure is shown in [ECT Tech Nugget - N1.1 - GNS3](https://youtu.be/w5qsM3LhpQI) (scrub to 9:49) for details. Wireshark functions a bit different in a GNS3 environment. It's a two part process. Right-Clicking on a link and selecting "Start Capture" will start the packet capture program on the link **and** start Wireshark to view the the packets. The problem is that stopping Wireshark **does not** stop the packet capture program. This means will will keep running collecting packets! After enough time the gHost will run out of memory and crash if the packet capture program isn't stopped. To stop the capture program, right-click on the link again and select "Stop Capture".

14. In the running GNS3 project right-click on the link between the Ubuntu-GUI-1 and the switch. In the context menu select `Start Capture` and press OK on the popup dialog box to begin packet capture (AKA packet sniffing). Wireshark GUI will auto-start and begin showing packet data for traffic going to or from the Ubuntu-GUI-1 object. A small magnifying glass icon will appear in GNS3 on the link.
<br>

15. In the Wireshark display filter use the following filter: `ip.addr==X.X.X.X`. Make sure to replace `X.X.X.X` with the IP for the Ubuntu-GUI-1 that was discovered earlier. This filter displays traffic going to or from the specified IP (Ubuntu-GUI-1 in this case). 
<br>

16. On Ubuntu-GUI-1 open a terminal window and `ping 8.8.8.8`. Allow it to run for five ping iterations and use CTRL+C to stop ping.
<br>

17. Go back to Wireshark and find those five ping packets (there should also be five responses).
<br>

18. Stop the capture process (not Wireshark). Right-click on the link with the magnifying glass, in the context menu select `Stop Capture`. This will stop **new** packets from showing up in Wireshark.
<br>

19. On the filter line in Wireshark add the following to the end after the current filter `&& icmp`. The complete filter will be:

    ``ip.addr==X.X.X.X && icmp``

    This filters the results even further to show only packets from the specified IP **and** packets that are ICMP (ping packets in this case).