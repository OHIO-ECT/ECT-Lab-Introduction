## Terminal Shell and File Management

### Goals
-   Become familiar with the Windows Powershell and Linux Bash command line terminals

### Resources

- Personal Computer (Destkop or Laptop)
- A document you have created to use as a lab notebook
- Assigned gHost (GNS3 Virtual Machine)
- [ECT/ITS Lab Notebook Cheatsheet](https://github.com/OHIO-ECT/Lab-Notebook-Cheat-Sheet)

### Environmental Context
- Connection to gHost VM
- GNS3 project shown in Network Diagram below
- Child VMs are started and ready for use

### Network Diagram

![](./images/lab1-pic2-1.png)

### Toolkit

-   Shells (i.e. Powershell, Bash)

### Terminal Shell and File Management

1. Open Powershell in Windows or open a Linux Terminal.
<br>

2. Run the command ``pwd`` to get the current working directory of the session.
<br>

3. Open a file explorer and go the same directory as seen in the pwd output. Note the relationship between the files in each location.
<br>

4. Run the Command ``mkdir test`` and then ``cd test``
<br>

5. Notice that test directory will also now appear in the file browser and you can move into that directory.
<br>

6. Start a new document in Notepad++ or your preferred text editor. Copy a couple of lines from <https://hipsum.co> into that file and save the file to the test directory made above.
<br>

7. Use Microsoft Word to create a docx file in this directory with the same text as the text file.
<br>

8. Open a powershell windows and use the ``dir`` or ``ls`` commands in your shell and note the difference in the file sizes.
<br>

9. Use the ``cat <TEXT_FILENAME>`` command to show the raw content of the file.
<br>

10. Cat the word document. What is all that other stuff for?
