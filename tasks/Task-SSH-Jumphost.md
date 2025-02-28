# SSH Sessions via a Jumphost

## Goals
- Learning to connect to remote SSH sessions through an SSH jumpbox.

## Resources
- [ECT Tech Nugget - N34.0 - Technology Perspective](https://youtu.be/ixrzbdUu8yQ)
- [ECT SSH Jumpbox Docs](https://sites.google.com/site/ohioitslab/home/how-to/ssh-jump-box)
- [ECT/ITS Lab Notebook Cheatsheet](https://github.com/OHIO-ECT/Lab-Notebook-Cheat-Sheet)
- Personal Computer (Desktop or Laptop)
- Assigned gHost (GNS3 Virtual Machine)

- Modern SSH client on your personal computer (Windows 10 and Windows 11 comes pre-installed)

## Lab Security and Addressing

SSH is a service commonly ran in on Linux systems to provide remote management, and is enabled by default on the gHosts and virtual machines inside of GNS3.  The well know username and passwords for these lab systems make them a significant security risk to attack from the outside world.  To protect the the lab inbound SSH connections are not allowed.  

Many of the addresses used in the lab equipment like the gHost use RFC 1918 addresses that are not accessible from outside of the lab networks.

An SSH jump box (AKA SSH gateway) will create an encrypted SSH connection tunnel between your SSH client and the target SSH server. This allows connection from the outside world to hosts that are not normally visible because of addresses or security. 

Access is controlled through two layers.  The first uses the OHIO ID and password (to pass through the jump host) and the second is the individual hosts local username and password (to login to the destination host).

## SSH Sessions via the ECT Jumphost

1. Open a Powershell or CMD session on a Windows PC or a Shell in an Apple computer.

2. It is common to need to customize commands for them to be used by a particular student. For example, the following command would result connecting to a remote machine `132.235.207.189` through the ssh jumphost `ect-bh-its.ohio.edu` using Professor Saunders' student account `bs257595@ohio.edu`.

The use of multiple @ as part of the command is due to the use of OHIO IDs for connections through the SSH jump box.

Professor Saunders Example:

```
ssh -J bs257595@ohio.edu@ect-bh.its.ohio.edu itsclass@132.235.207.189
```

Student Template:

```
ssh -J <OHIOID>@ohio.edu@ect-bh.its.ohio.edu <username>@<server IP>
```

Different SSH clients will have different settings that may need to be used to access this feature. The standard OpenSSH client uses a "-J" option to specify the jump box.

3. Using what commands shown above construct an SSH command that connects your the personal computer to your gHost via the Jumphost.  If prompted to accept a security key it is safe to accpet the key with a ```yes``` in this situation.



