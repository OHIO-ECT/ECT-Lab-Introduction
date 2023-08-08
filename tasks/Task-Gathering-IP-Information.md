## Gathering IP Information

### Goals
- Using command line (CLI) tools to discover IP configuration information
### Pre-Lab
- Watch the the following [ECT Tech Nuggets](https://www.youtube.com/@ecttechnuggets9126/featured) videos on YouTube:
  - [ECT Tech Nugget N0.1 Basic Diagnostic Tools 1](https://youtu.be/OtpzbVz7Ay8)
  - [ECT Tech Nugget N11.0 NMCLI](https://youtu.be/43F51qVz9Ds)

### Resources

- Personal Computer (Destkop or Laptop)
- A document you have created to use as a lab notebook
- Assigned gHost (GNS3 Virtual Machine)
- [ECT/ITS Lab Notebook Cheatsheet](https://github.com/OHIO-ECT/Lab-Notebook-Cheat-Sheet)

### Network Diagram

![](./images/lab1-pic2-1.png)

### Environmental Context

- Connection to gHost VM
- GNS3 project shown in Network Diagram below
- Child VMs are started and ready for use

### Gathering IP Information
Each operating system has different ways of naming network cards, which are refered to in this course as an "ethernet card" or an "interfaces" or "NIC" (network interface card). Interface names may be a few letters (2-6) that specifies the type of the technology, followed by a number especially when there is more than one of the same types. 
     - Loopback Interface: `lo0`
     - Ubuntu (Linux):`ens160`
     - VyOS:`eth0` and `eth1`
     - Windows has "helpful" names: `Ethernet Card (1)`
<br>

1. In Ubuntu-GUI-1 open a terminal window (AKA CLI or bash shell)
    - Use the command `ip a` to show command to show similar and additional data
    - Use the command `nmcli` to show command to show similar and additional data
    - Note the similarities and differences
<br>
   
2. Using the consol of Ubuntu-CLI-1 login using itsclass and previously given password.
    - Use the command `ip a` to show network information
    - Use the command `nmcli` to show similar and additional data
    - Note the similarities and differences

    The ip and nmcli commands are in use in many Linux distributions and have an extensive number of flags that both show and configure the computers network stack. Search engines and man pages are necessary resources to fully leverage these tools.
<br>

3. On the Windows-Desktop-1 Left-Click on the Start Button and type `powershell.exe` OR Start Button and type `cmd` [Windows has several CLI environments... Oh yippy]. In this case either CLI type will work.
    -   In either type of Windows CLI enter `ipconfig /all` to show network information
<br>

4. Use the correct command for the each GNS3 object (`ip a` / `nmcli` / `ipconfig /all`) to **create a table** (Excel or Google Sheets) like the chart below. Fill out as much as you can find out. This will be part of your lab report. that correlates the following information for each computer. *Be lazy*, copy the ipconfig output from Powershell by highlight the text and then right click within the highlight. 
<br>

|Computer Name &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Adapter Name | Description | IPv4 Address | Subnet Mask | Default Gateway | IPv6 Address (if available) |
|--|--|--|--|--|--|--|
|Win-Desktop-1| NIC1 | | | | | |
|Ubuntu-CLI-1 | ens3| | | | | |
|Ubuntu-GUI-1| ens3| | | | | |

