# Connecting Objects Inside GNS3

## Goals
- Learning to create new GNS3 projects
- Learning to connect GNS3 child objects together.

## Resources
- Personal Computer (Desktop or Laptop)
- A document you have created to use as a lab notebook
- Assigned gHost (GNS3 Virtual Machine)
- [ECT/ITS Lab Notebook Cheatsheet](https://github.com/OHIO-ECT/Lab-Notebook-Cheat-Sheet)

## Environmental Context
- Connection to gHost VM
- Running "98 - Intro Lab" GNS3 project
- Running GNS3 project

## Task Shutting down GNS3 Projects

1. When work is completed for a lab, students should shutdown projects.

2. Using the red stop button in the toolbar is effectively like pulling the power from a running computer.  In many cases this is acceptable with two warnings if the project is ever to be used again in the future.
    a.  There is a small chance the child objects will be corrupted. 
    b.  Work inside of the VMs (unsaved documents or configurations) could be lost.

3. Each child VM has a correct shutdown procedure for each operating system.
    a. Windows - Close all applications and save all documents.  Select the start button, the power icon, and "Shut Down" from the rollup menu.  The VM window should close when the system powers it self off.

    b. Ubuntu-GUI - Close all applications and save all documents.  Select the power icon in the upper right corner of the child object.  Note make sure to NOT select the power icon for the gHost.  In the drop down menu select "Power Off/Log Out" and then "Power Off".  Confirm the power off in the dialog box that pops up.  The VM window should close when the system powers it self off.

    c. Ubuntu-CLI - In the CLI window issue the command ``sudo poweroff`` and enter the itsclass users password.

    d. Proper shutdown for other objects will be described as they are introduced.

4. Once all child objects are closed the stop button can be pressed to shutdown the other objects in the project and GNS3 can be safely closed.

5. NEVER SHUTDOWN THE gHOST.