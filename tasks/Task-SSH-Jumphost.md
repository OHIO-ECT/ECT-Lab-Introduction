## SSH Sessions via a Jumphost

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
    - [ECT Tech Nugget - N34.0 - Technology Perspective](https://youtu.be/ixrzbdUu8yQ)

### Resources

- Personal Computer (Destkop or Laptop)
- A document you have created to use as a lab notebook
- Assigned gHost (GNS3 Virtual Machine)
- [ECT/ITS Lab Notebook Cheatsheet](https://github.com/OHIO-ECT/Lab-Notebook-Cheat-Sheet)

### Toolkit

-   Shells (i.e. Powershell, Bash)
-   SSH (i.e. Secure Shell)
-   Commands to be typed by the student and output from shells are indicated within this document in the ``fixed width font Courier New`` (as shown here).
-   Varibles to be filled in by the student are presented in ``<brackets>``. The student will need to replace the <> and the text with the needed varible. Example: **My name is ``<Name>``**. Would change to **My name is Bob.**
-   Find a Print Screen / Screen Capture tool that you like. The following is a list of tools known to work:
    -   Lightshot <https://app.prntscr.com>
    -   Greenshot <https://getgreenshot.org>

### SSH Sessions via a Jumphost

More information about the jump host can be found at: 
https://sites.google.com/site/ohioitslab/home/how-to/ssh-jump-box

1. It is common to need to customize commands for them to be used by a particular student. For example, the following command would result connecting to a remote machine `132.235.160.189` through the ssh jumphost `ect-bh-its.ohio.edu` using Professor Saunders' student account `bs257595@ohio.edu`.

    Professor Saunders Example:

    ``
    ssh -J bs257595@ohio.edu@ect-bh.its.ohio.edu itsvm@132.235.160.189
    ``
    
    Student Template:

    ``
    ssh -J <OHIOID>@ohio.edu@ect-bh.its.ohio.edu itsvm@<gHost IP>
    ``

2. Using what commands learned above construct an SSH command that connects from the personal computer to your gHost via the Jumphost.