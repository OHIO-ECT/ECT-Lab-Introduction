## Task SSH (Secure Shell)

### Goals
-   Learn to use SSH to connect to remote systems

### Resources

- Personal Computer (Desktop or Laptop)
- A document you have created to use as a lab notebookF
- Assigned gHost (GNS3 Virtual Machine)

### Environmental Context
- Connection to gHost VM

### Task SSH (Secure Shell)

1. The gHost uses the current version of Ubuntu, which is a distribution of Linux that often uses a GUI like Windows and Mac.
<br>

2. Open the ghost Terminal from the task bar on the right of the gHost desktop.
    ![](./images/image4.png)
<br>

3. Ensure that the prompt shows something **similar to**: ``itsvm@ITS-2300-GNS3-000-bc012345``
<br>

4. Replace ```<ghost IP>``` with the IP for your gHost. Then run the command: ``ssh itsvm@<gHost IP>``
<br>

5. Return to the gHost terminal by exiting this ssh session with the following command: ``exit``