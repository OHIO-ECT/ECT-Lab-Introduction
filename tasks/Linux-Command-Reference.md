# Linux Command Reference

## File System

| Command | Explanation |
| ------- | ----------- |
| cd \<path\> | Change Directory |
| chmod | Change File Permissions |
| chown | Change File Owner |
| cp \<source\> \<target\> | Copy Files (and more) |
| ls \<path\> | List Files |
| mkdir \<path\> | Make Directory |
| mv \<source\> \<target\> | Move Files (and more) - Also used to rename |
| pwd | Print Working (Current) Directory |
| rm \<file-path\> | Remove Files (and more) |
| rmdir \<path\> | Remove Directory |

### Aliases

| Command | Explanation |
| ------- | ----------- |
| l | ls -CF |
| la | ls -A |
| ll | ls -alF |

### Path Special Symbols

| Symbol | Explanation |
| ------- | ----------- |
| / | Top of the File System |
| ~ | Home Directory |
| . | Current Directory |
| .. | Parent Directory |

## Create or Edit Files

| Command | Explanation |
| ------- | ----------- |
| nano \<file-path\> | Invokve the Nano Text Editor |
| pico \<file-path\> | Invokve the Pico Text Editor (deprecated) |
| vi \<file-path\> | Invoke the VIM Editor (historical way) |
| vim \<file-path\> | Invoke the VIM Editor (modern way) |
| code \<path\> | Invoke the VS Code Editor (if installed) |

## Python

| Command | Explanation |
| ------- | ----------- |
| python3 | Invokes the interactive Python environment. Use quit() to Exit. |
| python3 \<file-path\> | Runs the Python program at the specified path. |

## Web Commands

| Command | Explanation |
| ------- | ----------- |
| curl \<url\> | Retrieve a file from a web server. |
| wget \<url\> | Retrieve a file from a web server. |

## Misc

| Command | Explanation |
| ------- | ----------- |
| cat \<file-path\> | Concatenate file(s) to the screen (or other places) |
| df | Disk Free |
| du | Disk Usage |
| find | A complex command with many options to find files and then perform some action on them. |
| grep \<regex\> \<path\> | Search path for files containing the regex. |
| head \<file-path\> | Prints the first 10 lines of the file to the console. |
| hostname \<new-hostname\> | Change the host name of the VM (perhaps your command line prompt is too long) |
| ps | List processes being run by the current user |
| sudo \<command\> | Super-User Do single command |
| sudo -i | Super-User Do interactive |
| tail \<file-path\> | Prints the last 10 lines of the file to the console. |
| tail -f \<file-path\> | Prints the last 10 lines of the file to the console and the continues to follow the file. |
| top | Display and monitor all running processes |
| touch \<file-path\> | Changes the modified date/time to be current |

