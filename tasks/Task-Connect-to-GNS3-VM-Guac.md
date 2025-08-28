## Connect gHost VM via Guacamole Remote Access Service

### Goals
- Demonstrate how a student can connect to a Graphical User Interface of their virtual host via a web-based method.
- Demonstrate how a student can connect to a Command Line Interface of their virtual host via a web-based method.

### Pre-Lab
- Watch the the following [ECT Tech Nuggets](https://www.youtube.com/@ecttechnuggets9126/featured) videos on YouTube:
    - [ECT Tech Nugget - N15.1 - Guacamole Remote Access](https://www.youtube.com/watch?v=sG9YlohRf_0)

### Resources

- Personal Computer (Desktop or Laptop) with a web browser, such as Chrome, Firefox, or Edge.
- Assigned gHost (GNS3 Virtual Machine)
- A document used as a lab notebook
- Tech Nuggets: [Tech Nuggets on YouTube](https://www.youtube.com/@ecttechnuggets9126)

### Connect to the Guacamole Service

Each student has been issued their own Linux Ubuntu Desktop Virtual Machine (VM). This system will be referred to as the "gHost" throughout the lab. The goal of this task is to show students how to connect to that environment so that they can work and complete assignments.

1. Retrieve the following received via email from ECT Dept. (Ask faculty for assistance if needed).

- GNS3 VM IP address
- GNS3 VM Username
- GNS3 VM Password

2. Watch the Pre-Lab video. **DO NOT follow along the first time.** Watch other ECT Tech Nuggets as necessary to round out understanding of related topics.

3.  Connect to the Guacamole service from computer using a browser. Bookmark the following URL!
    - https://rm.its.ohio.edu

4. The first time a browser connects to the Guacamole service, a screen similar to the following will appear. Click on the "Allow" button to allow the Guacamole service to access the local clipboard. This will allow a user to copy and paste text between their personal computer and the VM. This feature will be required to work effectively with the remote machines.
![](./images/Guac-Browser-Clipboard-Access.png)

This is a one-time action. If using a different browser or a different computer, the user will need to allow clipboard access again. If set correctly in the browser settings, the user should not see this message again.<br>

5. Check status of this setting in the current settings to ensure it is enabled. For example, in Chrome, check the clipboard setting by clicking on the lock icon in the address bar and then clicking on "Site settings". Ensure that the clipboard setting is set to "Allow" as shown below:<br>
    ![](./images/Guac-Browser-Clipboard-Status.png)

6. Login using OHIO ID, Password, and established method of Multifactor Authentication (MFA). Note: If user is already logged into some other Ohio University service, single sign-on features will reuse the credentials and session already established. 
    <br>
    Once authenticated, the following screen will be shown:
![](./images/Guac-Home-1.png)

### Connect to gHost's GUI via Guacamole
7. Locate and expand the "Class and Labs" caret (a little plus sign in a box) to reveal a list of the classes in which the user has gHosts.

- It is possible to be in multiple classes each with their own VM. If so, it is important to use the correct VM for the correct class. Different classes may have gHost configurations for different classes. 

**TL;DR - Don't use an ITS-2801 VM for ITS-2300, and/or vice-versa, even if it seems to work.**

![](./images/Guac-Home-2.png)

8. Note that if connected to Guacamole previously the "Recent Connections" portion of the screen will present with a quick way to reconnect. Previous connections are presented as shown below:

![](./images/Guac-Home-4.png)

9. Click on the line with the computer icon. This will establish a GUI connection to the gHost. **Be patient** as it may take a few seconds to establish. If the black login screen persists for more than 30 seconds, please contact the course instructor.

    For now, avoid any lines with an ">_" icon as that leads to a SSH Command Line interface (CLI).
![](./images/Guac-GUI-1.png)

### A Tour of the GUI

10. The toolbar on the left of the screen has a number of useful icons. Mouse-over icons to see the names of the applications. Find each of the following:
- Google Chrome
- Firefox
- Files
- Terminal
- GNS3
- Trash
- Show Apps

The last one is in the lower left corner, similar to where the Windows icon (aka Start Button) would be located.

### Exfiltrating Data

11. The gHost machine has access to the outside world. When saving data for lab reports there are several options. The easiest is to use a browser on the gHost to access web-based email. Open the file named "README.txt" on the desktop, highlight the text found within, and copy it either by right-clicking on the highlighted text and choosing "copy" or via the CONTROL-C keys.

12. Back on local personal computer, open up any application that can receive text, such as Notepad, Notepad++. Paste in the text copied from gHost. Notice that it's possible to copy and paste to and from gHost to local personal computer, and vice-versa. This will be very helpful (even necessary) for future assignments.

13. Back on gHost, launch either the Chrome or Firefox browsers, login into Catmail, compose a message to your OHIO ID, and attach the ReadMe.txt file to the message as an attachment. Send the message. Then, on local personal computer, check Catmail to verify the email was received with attachment.

14. Back on gHost, use a web browser to navigate to the Canvas LMS used by the class:
    - https://canvas.ohio.edu

Note: The Canvas LMS can be used as normal from within gHost and assignments can be submitted directly from gHost, if needed.

15. Use browser's back button to return to the Guacamole Home screen. If in the step above the user closed the browser window, then return to the URL and login again:
    - https://rm.its.ohio.edu

### Connect to gHost Virtual Machine's CLI

16. Locate and expand the "Class and Labs" caret to reveal a list of the classes for which the user has a gHost connection. Within the folder showing GUI connections to gHosts is another sub-folder ending in "-SSH". Expand that folder to reveal SSH connections to gHost. The connection icon ">_" will indicate these connections. The name of the connection will end in "-SSH", but otherwise have the same name as the GUI connection.

![](./images/Guac-Home-3.png)

17. Select the SSH connection to login the gHost SSH (AKA CLI) interface.
![](./images/Guac-CLI-1.png)

### Disconnecting from a VM

18. To disconnect from gHost either close the browser window or tab. This will leave gHost in its current state (all applications still running) so that later work can resume left off. This is **recommended** as often projects will require multiple sessions to complete.

### Black Screen of Death (sigh)
**DON NOT RUN THIS UNLESS INSTRUCTED**
The instructor will have you use this command if you encounter a black screen when trying to connect to the gHost. It's used via the SSH Guac connection:

```
DISPLAY=:10.0 timeout 0.5 xmessage -iconic x
```