## ECT Lab Introduction - SSH (Secure Shell)

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


### Toolkit

-   Shells (i.e. Powershell, Bash)
-   SSH (i.e. Secure Shell)
-   Commands to be typed by the student and output from shells are indicated within this document in the ``fixed width font Courier New`` (as shown here).
-   Varibles to be filled in by the student are presented in ``<brackets>``. The student will need to replace the <> and the text with the needed varible. Example: **My name is ``<Name>``**. Would change to **My name is Bob.**
-   Find a Print Screen / Screen Capture tool that you like. The following is a list of tools known to work:
    -   Lightshot <https://app.prntscr.com>
    -   Greenshot <https://getgreenshot.org>

### Task 2 - SSH (Secure Shell)

1. The gHost uses the current version of Ubuntu, which is a distribution of Linux that often uses a GUI like Windows and Mac.
<br>

2. Open the ghost Terminal from the task bar on the right of the gHost desktop.
    ![](./images/image4.png)
<br>

3. Ensure that the prompt shows something **similar to**: ``itsvm@ITS-2300-GNS3-000-bc012345``
<br>

4. Replace ```<ghost IP>``` with the IP for your gHost. Then run the command: ``ssh itsclass@<gHost IP>``
<br>

5. Return to the gHost terminal by exiting this ssh session with the following command: ``exit``
<br>

6. The gHost VM will run throughout the semester even if you are not connected to it. The GUI shutdown menu turned is off. **DO NOT** attempt to turn the gHost off without instructor approval. Instead, push the mouse cursor to the top of the screen to reveal the blue control bar. The commands on the bar to exit the remote desktop to return to the personal computer.