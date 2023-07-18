## ECT Lab Introduction - Gathering IP Information

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

### Task 7 - Gathering IP Information

**Note:** It is possible to complete this class on PCs that are not Windows based. However, the student is responsible to altering instructions to suit that system. Support from the instructors on these other systems will be very limited.

33. If you do not already have a preferred Text Editor, install Notepad++ with the instructions at: <https://notepad-plus-plus.org> 
**BEWARE: Make sure you are not clicking on an advertisement.**
    - For each of the commands that are used, make sure the response is free from error notations and is like responses that are shown in class and in ECT Tech Nuggets. 
    - Most of the diagnostic commands will be used every lab in this class. Detailed notes should be kept in your lab notebook.
    - All of the diagnostic commands that are in use in the labs have quick help that is available on the command line with either a `-h` or `/?` flag. Additional information can also be found via Internet searches.

34. Each operating system has different ways of naming network cards, which are refered to in this course as an "ethernet card" or an "interfaces" or "NIC" (network interface card). Interface names may be a few letters (2-6) that specifies the type of the technology, followed by a number especially when there is more than one of the same types. 
     - Loopback Interface: `lo0`
     - Ubuntu (Linux):`ens160`
     - VyOS:`eth0` and `eth1`
     - Windows has "helpful" names: `Ethernet Card (1)`
    
35. In Ubuntu-GUI-1 open a terminal window (AKA CLI or bash shell)
    - Use the command `ip a` to show command to show similar and additional data
    - Use the command `nmcli` to show command to show similar and additional data
    - Note the similarities and differences

36. Using the consol of Ubuntu-CLI-1 login using itsclass and previously given password.
    - Use the command `ip a` to show network information
    - Use the command `nmcli` to show similar and additional data
    - Note the similarities and differences

    The ip and nmcli commands are in use in many Linux distributions and have an extensive number of flags that both show and configure the computers network stack. Search engines and man pages are necessary resources to fully leverage these tools.

37. On the Windows-Desktop-1 Left-Click on the Start Button and type `powershell.exe` OR Start Button and type `cmd` [Windows has several CLI environments... Oh yippy]. In this case either CLI type will work.
    -   In either type of Windows CLI enter `ipconfig /all` to show network information

38. Use the correct command for the each GNS3 object (`ip a` / `nmcli` / `ipconfig /all`) to **create a table** that correlates the following information for each computer. *Be lazy*, copy the ipconfig output from Powershell by highlight the text and then right click within the highlight. 

|Computer Name   | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  |
|---|---|
|Adapter Type   |  &nbsp; |
|Adapter Name   |   |
|IPv6 Address (if available)   |   |
|IPv4 Address   |   |
|Subnet Mask   |   |
|Default Gateway   |   |