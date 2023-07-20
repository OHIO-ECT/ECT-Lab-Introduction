## Advanced Network Diagnostic Commands

### Goals
- Learn to use the following command line (CLI) tools: netstat, ip, nslookup, dig

### Pre-Lab
- Watch the the following [ECT Tech Nuggets](https://www.youtube.com/@ecttechnuggets9126/featured) videos on YouTube:
  - [ECT Tech Nugget N0.3 Basic Diagnostic Tools 3](https://youtu.be/PMk53TngTio)
  - [ECT Tech Nugget N0.4 Basic Diagnostic Tools 4](https://youtu.be/gD-Tk1Bk7x0)

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

### Advanced Network Diagnostic Commands

#### Route Tables
The route table is part of an Internet Protocol enabled network stack, and includes the directions on where network packets should be sent next on their journey from the source host to the destination. The network diagnostic tools to view that table is very helpful in lab.
- Linux command: `ip route`
- Windows: `netstat -rn`

1. Use the correct command to get the route table from each of the machines.

#### NSLookup and Dig

Converting Internet names to numbers and numbers to names is the responsibility of the Name Resolution services which use the Domain Name System (DNS) protocols. There are two commands that can access this name system. 
Syntax: `nslookup <destination>`
Where `<destination>` is replaced with either a hostname or IP.
Example: `nslookup google.com`<br>

2. On Ubuntu-CLI-1 use `nslookup` for each of the following host names:
- www.ohio.edu
- youtube.com

3. On Ubuntu-GUI-1 use `nslookup` for each of the following host names:
- xkcd.com
- 69.58.0.32

4. `nslookup` can also use non-default name servers.
Syntax: `nslookup <Target IP> <DNS Server IP>`
Example: `nslookup google.com 8.8.4.4`<br>
On Windows-Desktop-1 use nslookup and Google's public DNS server (8.8.8.8) as the `<DNS Server IP>` for each of the following host names:
    -  132.235.1.1
    -  www.cnn.com
    -  132.235.9.75
    -  98.139.183.24
<br>

5. Dig output returns more information than nslookup giving details of DNS record for that host/IP, but is only available in Linux.
Syntax: `dig <destination>`
Where `<destination>` is replaced with either a hostname or IP. To request a number to name conversion you must include the `-x` option.
Example: `dig google.com`
    On Ubuntu-GUI-1 `dig` for each of the following host names:
    - 203.178.141.194
    - www.ford.com
    - www.ohio.edu
    - www.google.com
<br>

6. On Ubuntu-CLI-1 `dig` for each of the following host names:
    -   132.235.67.1
    -   69.58.0.32
    -   8.8.8.8