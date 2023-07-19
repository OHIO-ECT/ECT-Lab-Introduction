## ECT Lab Introduction - SSH (Secure Shell)

### Goals
-   Learn to use SSH to connect to remote systems

### Resources

- Personal Computer (Destkop or Laptop)
- A document you have created to use as a lab notebook
- Assigned gHost (GNS3 Virtual Machine)

### Toolkit

-   Shells (i.e. Powershell, Bash)
-   SSH (i.e. Secure Shell)
-   Commands to be typed by the student and output from shells are indicated within this document in the ``fixed width font Courier New`` (as shown here).
-   Varibles to be filled in by the student are presented in ``<brackets>``. The student will need to replace the <> and the text with the needed varible. Example: **My name is ``<Name>``**. Would change to **My name is Bob.**

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
