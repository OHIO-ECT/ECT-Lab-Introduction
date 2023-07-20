## GNS3 Projects

### Goals
- Learn to start GNS3 Project

### Resources

- Personal Computer (Destkop or Laptop)
- A document you have created to use as a lab notebook
- Assigned gHost (GNS3 Virtual Machine)
- [ECT/ITS Lab Notebook Cheatsheet](https://github.com/OHIO-ECT/Lab-Notebook-Cheat-Sheet)

### Environmental Context
- Connection to gHost VM

### Network Diagram

![](./images/lab1-pic2-1.png)

### GNS3 Projects

1.  Start all objects in the project with the big green triangle in the top tool bar.
<br>

2.  This action will start **ALL** the VMs will start at once. Get comfy as Atlas heaves the world up. The more objects in a project the longer this start up time will take. If you don't know who Atlas is you'll have some time to read [this](https://greekgodsandgoddesses.net/gods/atlas) while the all the GNS3 VMs (AKA child VMs) start up. Each child VM typicially starts a consol window so the user can see what's going on. 
<br>
    **Note:**  It is not always necessary (or desired) to start all objects at once. If needed, Right-Click a specific child object and use it's context menu to control it individually.
<br>

3. Once all the GNS3 VMs have started and are either at a login prompt to a desktop GUI they are ready for use.
<br>

4. After starting up a project each GNS3 VM object will (typically) open a child console window (as shown in picture below). In this case should be three child windows inside gHost. First, Ubuntu-CLI-1 a Linux Server (terminal only), second is Ubuntu-GUI-1 a Linux Desktop (GUI with terminal option), third is Windows-Desktop-1. Operating systeming running inside operating systems (with windows inside windows) can be a very [Inception] idea. If this idea gives you a headache you are **doing it correctly**. Much of what we do as IT Professional is virtual. This type of environment is a very good example. For some help with this idea see [ECT Tech Nugget - N34.0 - Technology Perspective](https://youtu.be/ixrzbdUu8yQ.)

    - See [ECT Tech Nuggets Playlist](https://www.youtube.com/playlist?list=PLEA5GnkCPRTlvN_eyR99jOSsBCaV6khRS) for more detail. As always, if you have questions it's your responsibility to **ASK** for help! We can't know if you don't understand!

    ![](./images/lab1-pic1.png)

    Shown above GNS3 and GNS3 VMs - GNS3 Window (left), Ubuntu Linux Server (top center), Windows Desktop (bottom center), Ubuntu Linux Desktop/GUI (right).