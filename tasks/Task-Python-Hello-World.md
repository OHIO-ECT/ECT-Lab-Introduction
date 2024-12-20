# Develop a Basic Python Script

Stated plainly, a python script is a series of python command placed in a text file which is then executed by the Python interpreter. So, in order to develop a python script, you must type your commands into a text file. By convention, we name these scripts with a ".py" extension. Thus, a file named "hello.py" is a python script.

Any text editor can be used to write a script. You could use Notepad on your Windows computer or nano on a Linux computer. You could even use MS Word and save the program as a text file. But programmers tend to use text editors that are specially designed to be used for programming because those editors come with more features. This task will walk you through using the VS Code editor.

## Objectives

- Demonstrate how to use the VS Code Editor
- Develop a basic program that will prove the Development Environment is functional.
- Run the basic program and observe the results.
- Exfiltrate your program so you can turn it in as part of your assignment.

## Tasks

### Login to your VM

1. Login to your VM as has been described in previous tasks.
<br>

2. Launch the Terminal application. It might still be running from a previous task.
<br>

3. Launch the Files application if you want to, but it is not required. It might also still be running from a previous task.
<br>

### Create a python Directory

4. In the Terminal application, make sure your current directory is your Home Directory. Remember that you can use the "cd" command with no other options to return to your Home Directory.

```
cd
```
<br>

5. Make a directory named "python". This will make a single place to collect all of your python programs.

```
mkdir python
```
<br>

### Create an assignment-01 Directory

6. Change to your python directory.

```
cd python
```
<br>

7. Make a directory for this assignment called "program00".

```
mkdir program00
```
<br>

8. Change to your program00 directory.

```
cd progam00
```
<br>

9. If you have the Files application running, you should see those new directories have been created. The next steps are going to use another program that will need space on your screen. Leave the Files application running if it provides you some comfort, but you don't need it. You could always launch it again if you wanted it.
<br>

### Launch VS Code

VS Code (Visual Studio Code) is a popular text editor used by programmers. It understands the syntax of programming languages. This lets it provide syntax coloring and hints that might save you time. Visual Code wants to work on a project and it will think of directory as the location of this project. You can either specify that directory when you launch VS Code, or tell VS Code which directory to use after you have launched it. By default, VS Code appears to detect the python directory that you have created.
<br>

10. Launch VS Code via either of these methods:

- Type this command: ```code``` in your Terminal window.
- Click on the "Visual Studio Code" icon that you've added to your Toolbar.
- Click on the "Show Apps" icon in the lower left corner of the GUI and then choose "Visual Studio Code."
<br>

11. When asked if you "trust the authors of the files in your python folder", choose **Yes, I trust the authors**.
<br>

12. Take a few minutes to become familiar with the layout of the screen.
<br>

- On the left is a toolbar with icons such as "Explorer", "Search", "Source Control", "Run and Debug", "Extensions", "Remote Explorer", and "Docker."
- The "Explorer" icon is a little brighter indicating it is selected, which is why there is an "Explorer" pane on the left side showing your python and program00 folders.
- The "Welcome" pane on the right tells you of some basic functions. As you open files to edit they will also appear on the right.

![](./images/VSCode-1.png)
<br>

### Enter the Hello World Program

13. In the Explorer pane, click on "program00" and it should become highlighted.
<br>

14. Click on the "New File" icon in the upper right of the Explorer pane as shown here:

![](./images/VSCode-2.png)
<br>


### Run the Hello World Program

### Exfiltrate the Hello World Program


