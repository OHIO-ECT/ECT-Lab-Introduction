# Advanced Network Diagnostic Commands

## Goals
- Learn to use the following command line (CLI) tools: netstat, ip, nslookup, dig

## Pre-Lab
- Watch the the following [ECT Tech Nuggets](https://www.youtube.com/@ecttechnuggets9126/featured) videos on YouTube:
  - [ECT Tech Nugget N0.2 Basic Diagnostic Tools 2](https://youtu.be/hWeJlNVaUbU)
  - [ECT Tech Nugget N0.3 Basic Diagnostic Tools 3](https://youtu.be/PMk53TngTio)
  - [ECT Tech Nugget N0.4 Basic Diagnostic Tools 4](https://youtu.be/gD-Tk1Bk7x0)

## Resources
- Personal Computer (Desktop or Laptop)
- A document you have created to use as a lab notebook
- Assigned gHost (GNS3 Virtual Machine)
- [ECT/ITS Lab Notebook Cheatsheet](https://github.com/OHIO-ECT/Lab-Notebook-Cheat-Sheet)

## Environmental Context
- Connection to gHost VM
- GNS3 Running "98 - Intro Lab" GNS3 project
- Child VMs are started and ready for use

## Ping

Ping is a basic (the **MOST** basic) tool for figuring out if a machine has network access. The command will, in effect, bounce packets off the destination machine like a sonar.... PING. The command gives a binary answer: **YES** it sees something or **NO** it does not.

The **best** network debugging processes start with pinging another machine that is in the same IP network (more on that idea later) usually this is the default gateway.

1. The format of the ping command is `ping <destination>`. Where `<destination>` is replaced with either a hostname or IP. For example `ping google.com` or `ping 8.8.8.8`

2. In a powershell terminal in Windows-Desktop-1 run the command ``ping 13.107.246.51`` and expect to get 4 "Reply" with round trip or ping time.

3. Most implementations of ping will repeat the ping process several times; others will run continuously until user presses <ctrl+c> to stop the process.  For example, try ``ping 132.235.1.1`` in the Ubuntu-GUI-1.  

4. Ping can also take DNS names.  Try ``ping xkcd.com`` on the Ubuntu-CLI-1

5. Use the help command line flag (`-h` for Linux or `/?` for Windows) to find the proper flag to request 15 pings and then stop.
    -   Ubuntu-GUI-1: 99.83.183.221
    -   Windows-Desktop: www.kame.net

## Traceroute

The traceroute command gives more detail about the network **BETWEEN** the machine and the destination.

The `-n` or `-d` option suppresses DNS hostname lookups on many commands. Typically, DNS names are not necessary for network diagnostics and consume time and create unwanted network traffic.

When an individual traceroute hit fails (lines noted with `* * *`) traceroute will typically continue until the test has reached 30 hops. Press Ctrl+C to stop traceroute, if you get three or more lines with the `* * *` notation.

Syntax: `traceroute -n <destination>`
Where `<destination>` is replaced with either a hostname or IP.
Example: `traceroute -n google.com`

6. In Ubuntu-GUI-1 machine and use the traceroute command gather path information to the following destinations:
    -   132.235.8.133
    -   www.ford.com
    -   8.8.8.8
    -   github.com
<br>

7. In Windows-Desktop access the powershell terminal (aka CLI). Windows is limited to eight-character old-school commands (long story why) and uses a different switch to suppress DNS lookups. Access the Windows CLI and issue the command:
Syntax: `tracert -d <destination>`
Where `<destination>` is replaced with either a hostname or IP.
Example: `tracert -d google.com`
<br>

8. In the Windows machine, traceroute to the following destinations:
    -   8.8.4.4
    -   microsoft.com

## Simple Name Resolution

9. Converting Internet names to numbers and numbers to names is the responsibility of the Name Resolution services which use the Domain Name System (DNS) protocols. There are two commands that can access this name system. nslookup is universal accross all of the GNS3 objects that the ITS department uses. 

Syntax: `nslookup <destination>`
Where `<destination>` is replaced with either a hostname or IP.
Example: `nslookup google.com`
<br>

10. On Ubuntu-CLI-1 use `nslookup` for each of the following host names:
- www.ohio.edu
- youtube.com

11. On Ubuntu-GUI-1 use `nslookup` for each of the following host names:
- xkcd.com
- 69.58.0.32

12. nslookup always uses the computers configured name server.  There are advanced debugging processes where it is helpful to query some other DNS server for its response to a query.  For example Google runs two open Caching DNS servers that are regularly used in these labs.  8.8.8.8 and 8.8.4.4.

Syntax: ``nslookup <Target IP> <DNS Server IP>``
Example: ``nslookup google.com 8.8.8.8``
<br>

13. On Windows-Desktop-1 use nslookup and Google's public DNS server (8.8.8.8) as the `<DNS Server IP>` for each of the following host names:
    -  132.235.1.1
    -  www.cnn.com
    -  132.235.9.75
    -  98.139.183.24
<br>

## Detailed Name Resolution

14. Dig output returns more detailed information than nslookup does by default, but is only available in Linux.

Syntax: `dig <destination>`
Where `<destination>` is replaced with either a hostname or IP. 
To request a number to name conversion you must include the `-x` option.
Example: `dig google.com`

15. On Ubuntu-GUI-1 `dig` for each of the following host names:
    - 203.178.141.194
    - www.ford.com
    - www.ohio.edu
    - www.google.com
<br>

