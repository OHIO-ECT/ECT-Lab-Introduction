## Basic Network Diagnostic Tools

### Goals
- Learn to use basic command line (CLI) tools: ping and traceroute

### Pre-Lab

- Watch the the following [ECT Tech Nuggets](https://www.youtube.com/@ecttechnuggets9126/featured) videos on YouTube:
  - [ECT Tech Nugget N0.2 Basic Diagnostic Tools 2](https://youtu.be/hWeJlNVaUbU)

  
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


### Basic Network Diagnostic Tools

Ping is a basic (the **MOST** basic) tool for figuring out if a machine has network access. The command will, in effect, bounce packets off the destination machine like a sonar.... PING. The command gives a binary answer: **YES** it sees something or **NO** it does not.

The **best** network debugging processes start with pinging another machine that is in the same IP network (more on that idea later) usually this is the default gateway.

Most implementations of ping will repeat the ping process several times; others will run continuously until user presses CTRL+C to stop the process.

The format of the ping command is `ping <destination>`. Where `<destination>` is replaced with either a hostname or IP. For example `ping google.com` or `ping 8.8.8.8`

1. Use the ping command on the specified machine to ping the following locations.
    -   Ubuntu-GUI-1: 132.235.1.1
    -   Windows-Desktop-1: 13.107.246.51
    -   Ubuntu-CLI-1: xkcd.com
<br>

2. Use the help command line flag (`-h` for Linux or `/?` for Windows) to find the properly flag to request 15 pings and then stop.
    -   Ubuntu-GUI-1: 99.83.183.221
    -   Windows-Desktop: www.kame.net

#### Traceroute Command

The traceroute command gives more detail about the network **BETWEEN** the machine and the destination.

The `-n` or `-d` option suppresses DNS hostname lookups on many commands. Typically, DNS names are not necessary for network diagnostics and consume time and create unwanted network traffic.

When an individual traceroute hit fails (lines noted with `* * *`) traceroute will typically continue until the test has reached 30 hops. Press Ctrl+C to stop it once if you get three or more lines with the `* * *` notation.

3. In gHost open terminal (aka CLI) and use the traceroute command.
Syntax: `traceroute -n <destination>`
Where `<destination>` is replaced with either a hostname or IP.
Example: `traceroute -n google.com`
<br>Traceroute to the following destinations:
    -   132.235.8.133
    -   www.ford.com
    -   8.8.8.8
    -   itsohio.net
<br>

4. In Windows-Desktop access the powershell terminal (aka CLI). Windows is limited to eight-character old-school commands (long story why) and uses a different switch to suppress DNS lookups. Access the Windows CLI and issue the command:
Syntax: `tracert -d <destination>`
Where `<destination>` is replaced with either a hostname or IP.
Example: `tracert -d google.com`
<br>Traceroute to the following destinations:
    -   8.8.4.4
    -   microsoft.com