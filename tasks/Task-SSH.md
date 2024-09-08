# Task SSH (Secure Shell)

## Goals
- Learn to use SSH to connect to remote systems

## Resources

- A document you have created to use as a lab notebookF
- Assigned gHost (GNS3 Virtual Machine)

## Environmental Context
- Connection to gHost VM

## Task SSH (Secure Shell)

1. The gHost uses the current version of Ubuntu, which is a distribution of Linux that often uses a GUI like Windows and Mac.

2. Open the ghost Terminal from the task bar on the right of the gHost desktop.
![](./images/image4.png)

3. Ensure that the prompt shows something **similar to**: ``itsvm@ITS-2300-GNS3-000-bc012345``

4. In Ubuntu-CLI open a terminal and retrieve the IP address of that computer.

5. In the gHost terminal, run the command: ``ssh itsclass@<Ubuntu-CLI IP>``.  Replace ```<Ubuntu-CLI IP>``` with the IP found in the previous step. 

6. Note the change in the prompt to reflect the change in the device that commands are issued to.  This is the reason to set server host names.

7. Use the following command to set a permanent hostname on the server.  Note: The prompt will only update when the user logs out and logs back into the server.

8. Return to the gHost terminal by exiting this ssh session with the following command: ``exit``
