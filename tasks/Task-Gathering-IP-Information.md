# Gathering IP Information

## Goals
- Using command line (CLI) tools to discover IP configuration information

## Pre-Lab
- Watch the the following [ECT Tech Nuggets](https://www.youtube.com/@ecttechnuggets9126/featured) videos on YouTube:
    - [ECT Tech Nugget N0.1 Basic Diagnostic Tools 1](https://youtu.be/OtpzbVz7Ay8)
    - [ECT Tech Nugget N11.0 NMCLI](https://youtu.be/43F51qVz9Ds)

## Resources
- Personal Computer (Desktop or Laptop)
- A document you have created to use as a lab notebook
- Assigned gHost (GNS3 Virtual Machine)
- [ECT/ITS Lab Notebook Cheatsheet](https://github.com/OHIO-ECT/Lab-Notebook-Cheat-Sheet)

## Environmental Context
- Connection to gHost VM
- Running "98 - Intro Lab" GNS3 project
- Child VMs are started and ready for use

## Gathering IP Information

1. Network interfaces have two parts, outside of the computer will be a connection to the larger network, and inside of the computer the configuration for the card. Depending on the context Network interfaces are referred to in this course as an "ethernet card" or an "interfaces" or "NIC" (network interface card).
<br>

2. GNS3 represents the outside connection as a red or green dot attached to the GNS3 object and a text identifier like ``e0``.
<br>

3. Inside the guest GNS3 object, Interface names vary by OS vendor and by the type of technology, like ethernet, that the interface supports. Typically names are a few letters (2-6) followed by a number especially when there is more than one of the same type of interface. CAUTION: Rarely do the NIC numbers on the inside match NIC numbers on the outside. For example ``e0`` in GNS3 might be:
     - Ubuntu (Linux):`ens160`
     - VyOS:`eth0` and `eth1`
     - Windows has "helpful" names: `Ethernet Card (1)`
<br>

4. Many network systems have two representations of network configurations. The most fundamental is the resultant or current configuration. In Ubuntu-GUI-1 open a terminal window (AKA CLI or bash shell) and issue the commands ``ip address`` and ``ip route``. These commands output a lot of data about the current network configuration.

5. In modern linux' the "Network Manager" application is used to configure the network cards and can show the same fundamental information. Run the command ``nmcli`` on the Ubuntu-GUI-1 and note the similarities and differences.
<br>

6. Repeat the previous steps on Ubuntu-CLI-1 to show that systems information. 
<br>

7. The ip and nmcli commands are in use in many Linux distributions and have an extensive number of flags that both show and configure the computers network stack. Search engines and man pages are necessary resources to fully leverage these tools.

8. On the Windows-Desktop-1 Left-Click on the Start Button and type `powershell.exe` OR Start Button and type `cmd` [Windows has several CLI environments... Oh yippy]. In this case either CLI type will work.
    - In either type of Windows CLI enter `ipconfig /all` to show network information.
<br>

9. In Windows the command ``netstat -nr`` is also used to show more detailed routing information similar to ``ip route`` in linux.

10. Use the correct command for the each GNS3 object (`ip a` / `nmcli` / `ipconfig /all`) to **create a table/chart** (Excel or Google Sheets) like the chart below that correlates the following information for each computer. Fill out as much as you can find out. This will be part of your lab report. *Be lazy*, copy the ipconfig output from Powershell by highlight the text and then right click within the highlight. This copy/paste concept should work pretty well in most CLI environments.
<br>

|Computer Name &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Adapter Name | Description | IPv4 Address | Subnet Mask | Default Gateway | IPv6 Address (if available) |
|--|--|--|--|--|--|--|
|Win-Desktop-1| NIC1 | | | | | |
|Ubuntu-CLI-1 | ens3| | | | | |
|Ubuntu-GUI-1| ens3| | | | | |

