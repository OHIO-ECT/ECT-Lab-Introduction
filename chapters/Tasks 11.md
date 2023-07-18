## ECT GNS3 Introduction - The Toolkit

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

### Task 11 - Advanced Network Diagnostic Commands

#### Route Tables
The route table is part of an Internet Protocol enabled network stack, and includes the directions on where network packets should be sent next on their journey from the source host to the destination. The network diagnostic tools to view that table is very helpful in lab.
- Linux command: `ip route`
- Windows: `netstat -rn`

63. Use the correct command to get the route table from each of the machines.

#### NSLookup and Dig

Converting Internet names to numbers and numbers to names is the responsibility of the Name Resolution services which use the Domain Name System (DNS) protocols. There are two commands that can access this name system. 
Syntax: `nslookup <destination>`
Where `<destination>` is replaced with either a hostname or IP.
Example: `nslookup google.com`<br>

64. On Ubuntu-CLI-1 use `nslookup` for each of the following host names:
- www.ohio.edu
- youtube.com

65. On Ubuntu-GUI-1 use `nslookup` for each of the following host names:
- xkcd.com
- 69.58.0.32

66. `nslookup` can also use non-default name servers.
Syntax: `nslookup <Target IP> <DNS Server IP>`
Example: `nslookup google.com 8.8.4.4`<br>
On Windows-Desktop-1 use nslookup and Google's public DNS server (8.8.8.8) as the `<DNS Server IP>` for each of the following host names:
    -  132.235.1.1
    -  www.cnn.com
    -  132.235.9.75
    -  98.139.183.24
<br>

67. Dig output returns more information than nslookup giving details of DNS record for that host/IP, but is only available in Linux.
Syntax: `dig <destination>`
Where `<destination>` is replaced with either a hostname or IP. To request a number to name conversion you must include the `-x` option.
Example: `dig google.com`
    On Ubuntu-GUI-1 `dig` for each of the following host names:
    - 203.178.141.194
    - www.ford.com
    - www.ohio.edu
    - www.google.com
<br>

68. On Ubuntu-CLI-1 `dig` for each of the following host names:
    -   132.235.67.1
    -   69.58.0.32
    -   8.8.8.8