## SSH Sessions via a Jumphost

### Goals
- Learning to connect to remote SSH sessions through an SSH jumpbox

### Pre-Lab

- Watch the the following [ECT Tech Nuggets](https://www.youtube.com/@ecttechnuggets9126/featured) videos on YouTube:
    - [ECT Tech Nugget - N34.0 - Technology Perspective](https://youtu.be/ixrzbdUu8yQ)

### Resources

- Personal Computer (Destkop or Laptop)
- A document you have created to use as a lab notebook
- Assigned gHost (GNS3 Virtual Machine)
- [ECT/ITS Lab Notebook Cheatsheet](https://github.com/OHIO-ECT/Lab-Notebook-Cheat-Sheet)

### Environmental Context
- Modern SSH client on your personal computer (Windows 11 comes pre-installed)

### SSH Sessions via a Jumphost

More information about the jump host can be found at: 
https://sites.google.com/site/ohioitslab/home/how-to/ssh-jump-box

1. Open a Powershell or CMD session on a Windows PC.
<br>

2. It is common to need to customize commands for them to be used by a particular student. For example, the following command would result connecting to a remote machine `132.235.160.189` through the ssh jumphost `ect-bh-its.ohio.edu` using Professor Saunders' student account `bs257595@ohio.edu`.
<br>
    Professor Saunders Example:

    ````
    ssh -J bs257595@ohio.edu@ect-bh.its.ohio.edu itsvm@132.235.160.189
    ````
    Student Template:

    ````
    ssh -J <OHIOID>@ohio.edu@ect-bh.its.ohio.edu itsvm@<gHost IP>
    ````

2. Using what commands learned above construct an SSH command that connects your the personal computer to your gHost via the Jumphost.