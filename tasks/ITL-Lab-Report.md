## ECT Lab Introduction - Lab Reports

### Goals
-   Configure Remote Desktop to connect to the lab environment
-   Learn the basic setup of the GNS3 virtual lab environment
-   Overview of Windows and Unix operating systems
-   Introduction to the CLI, and the interaction with filesystem
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

- Personal Computer (Desktop or Laptop)
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
-   Variables to be filled in by the student are presented in ``<brackets>``. The student will need to replace the <> and the text with the needed variable. Example: **My name is ``<Name>``**. Would change to **My name is Bob.**
-   Find a Print Screen / Screen Capture tool that you like. The following is a list of tools known to work:
    -   Lightshot <https://app.prntscr.com>
    -   Greenshot <https://getgreenshot.org>

### Task 12 - Lab Reports

Lab Reports are to be written individually (no group work). Reports will be uploaded to Blackboard electronically as a **PDF** (ONLY!). Reports do not generally need to be more than several pages. Officially, they need to be "long enough to answer the questions".

An example lab report format doc can be found here. (https://github.com/OHIO-ECT/ECT-Lab-Introduction/blob/main/files/ITL%20-%20Lab%20Report%20Example.pdf)

Each lab report must have a header (**no cover pages!**) on the first page that includes:
-   Student Name
-   Lab section attended
-   Student program affiliation (CS ugrad, CS grad, ITS ugrad, ITS grad, etc.)
- For terminal window data (ping, traceroute, netstat etc.) data should be formatted with a fixed width font like courier to preserve the columns and displayed as shown on screen.
- Absolutely **NO SCREEN SHOTS!** (with your phone camera or screen shot tool) There are extremely rare cases when a screen shot (usually for a web interface) will be required. This will be noted in the assignment instructions.
- Number your answers with the same numbers as the Lab Report Questions.
- Terminal window (CLI) data needs to be reformatted to remove the extra line breaks. While this report is long future ones will be **much** longer. Removing the extra line breaks will save much space. A smaller font can also be used for terminal window data or adjust margins for that data to stop line wrapping.

#### Lab Report Questions

1.  From the **Connect to your GNS3 VM** section - **Show** to and from fields and the body text of email to yourself.
<br>

2.  From the **Ethernet Card Data** section - **Show** table created.
<br>

3.  From the **Ping Command** section - **Show** the command used and the first 3 lines of output for each target, and add the average round trip time for each destination on the next line (copy it from the summary line if ping printed one, or calculate it).
<br>

4.  From the **Traceroute Command** section - Using output from traceroute command create a table showing command, hops (IP or hostname), and hop time. In the table **show** the single **longest** delay among all times for each hop. Note that each line (AKA hop) of traceroute output is the results from a new set of probe packets (i.e. times are not always getting longer for later lines in the output). 
<br>

5.  From the **Route Table Commands** section - **Show** the IP address of the router AKA default gateway for each GNS3 guest VMs in the project (i.e. Windows, Ubuntu, etc.) **Hint:** check against traceroute data for verification!
<br>

6.  From the **NSLookup and Dig Commands** - **Show** command and command output for each target, highlight only the IPv4 address or addresses returned for that particular hostname. The command line version will return additional names and IP addresses; ignore these for now. Highlight only the host name or names returned for that particular IP address.
<br>

7.  From the **Wireshark Data** section - (for help see Lab Writeup Guide and [ECT Tech Nugget N0.5 Wireshark][ECT Tech Nugget N0.5 Basic Diagnostic Tools 5])<br>
    a.  Find packet 58, show the full MAC address (don't let Wireshark hide parts). **Explain** which part of the address identifies the manufacturer of the card. Wireshark may try to "help" you out. Using ONLY the MAC address how can YOU figure out who NIC manufacturer is?<br>
    <br>
    b.  Find DNS data in the capture and **show** entire Wireshark packet output from the packet.
<br>

8. From the **Create a GitHub Account** section - email GitHub account name to instructors. **Show** your Github username in the report.