# GNS3 Projects

## Goals

- Learn to start a GNS3 Project

## Resources

- Personal Computer (Desktop or Laptop)
- Lab notebook document
- Assigned gHost (GNS3 Virtual Machine)
- [ECT/ITS Lab Notebook Cheatsheet](https://github.com/OHIO-ECT/Lab-Notebook-Cheat-Sheet)
- [ECT Tech Nuggets Playlist](https://www.youtube.com/playlist?list=PLEA5GnkCPRTlvN_eyR99jOSsBCaV6khRS)
- [GNS3 GUI Documentation](https://docs.gns3.com/docs/using-gns3/beginners/the-gns3-gui)

## Environmental Context

- Connection to gHost VM

## GNS3 Projects

1. Start the GNS3 application with gecko icon in the right hand navigation.

2. Use the "New Blank Project" button from the GNS3 toolbar. The interface that appears has two tabs. The first allows creating a new blank project and the second provides a list of projects from this computer "Project Library". Choose the project library and open the project "98 - Intro Lab".

3. If necessary, review [ECT Tech Nugget N1.1 GNS3](https://www.youtube.com/watch?v=w5qsM3LhpQI)

4. Expand the "All Devices" menu from the "Devices Toolbar" on the left hand side of GNS3.

5. Using the network diagram shown in this document connect all the GNS3 objects together. Review [ECT Tech Nugget N1.1 GNS3](https://www.youtube.com/watch?v=w5qsM3LhpQI) (scrub to about 6:20) for detailed instructions how to connect objects together in GNS3.<br>
![](./images/lab1-pic2.png)

6. Start all objects in the project with the big green triangle in the top tool bar. This action will start **ALL** the VMs at once. Get comfy as Atlas heaves the world up. The more objects in a project the longer this start up time will take. If Atlas is unfamiliar, there is time to read [this](https://greekgodsandgoddesses.net/gods/atlas) while all the GNS3 VMs (AKA child VMs) start up. Each child VM typically starts a console window so the status can be monitored.<br>
**Note:** It is not always necessary (or desired) to start all objects at once. If needed, Right-Click a specific child object and use its context menu to control it individually.

7. After starting up a project each GNS3 VM object will (typically) open a child console window. In this case should be three child windows inside the gHost.
- "Ubuntu-CLI-1", a Linux Server (terminal only)
- "Ubuntu-GUI-1", a Linux Desktop (GUI with terminal option)
- "Windows-Desktop-1", a Windows Desktop (GUI)<br><br>
![](./images/lab1-pic1.png)

8. It is possible to close the console of a GNS3 object and it will continue to operate normally (it would be like turning off the monitor on a physical computer). The console can be restored by right click on the object and selecting "Console".

9. Operating systems running inside operating systems (with computers running inside computers) can be a very [Inception] idea. If this idea provides a headache, **it is being done correctly**. Much of what we do as IT Professional is virtual. Our gHost environment is a very good example. For some help with this idea see [ECT Tech Nugget - N34.0 - Technology Perspective](https://youtu.be/ixrzbdUu8yQ.)

10. Once all the GNS3 VMs (aka "child VMs" as they are a child the the gHost) have started and are either at a login prompt or are at a GUI desktop they are ready for use.

11. **Record the following credentials in your lab notebook for future reference.** Child VMs in GNS3 and many other student used systems will use this standard username `itsclass` and password `class115#`. You will need these credentials to access each child VM throughout the remainder of the course.

12. Projects remain running even if the user is NOT connected to the remote desktop connection. This allows the student to take a break from the lab work and return to the project later.

13. Shutting down GNS3 projects will be discussed on a separate page.