# Goals 
-   Orient the student to the basics of the Linux operating system
-   Utilize the SSH protocol to remotely connect to a remote system.

# Toolkit 
-   Student personal computer
-   gHost
-   Remote Desktop
-   SSH
-   GSN3

# Guides
-   [Tech Nugget N25.0 - Ubuntu 20.04 Intro](https://youtu.be/X4bfK24sbzM)

# Deploy the Ubuntu GUI

1. Return to GNS3 

![](media/nestedVMs.png)

Figure 1 - Nested Virtual Machines



# Configure the server hostname

29. DNS names are descriptive to the function of the server, but DNS
    servers are also sensitive critical infrastructure. This causes
    organizations, including Ohio University, to be very cautious with
    the administration of that system. The ITS department is one of a
    few departments in the University that has access to make changes
    within its own domain, its.ohio.edu. The department has been granted
    the authority to create generic DNS names for the IP addresses used
    in this class. The format of this name is its-160-X.its.ohio.edu
    where X is equal the last octet in the 132.235.160.X address.

For example, the name its-160-150.its.ohio.edu is associated with the IP
address 132.235.160.150.

30. Server hostnames do NOT have to be equal to DNS names. Some
    applications do leverage the hostname to simplify their
    configuration. The application, Apache HTTP, which will be used in
    the remainder of this lab does this. RDP into the GNS3 system and on
    a terminal in the VM and use the following command to set the
    hostname. Replace the X with the number from the public IP address
    that is assigned via Blackboard and used in previous labs.

> sudo hostnamectl set-hostname its-160-X.its.ohio.edu

31.  In a new terminal window on the student PC SSH to this
    domain name using the jump host. Observe that the prompt on the
    terminal has changed to incorporate this new hostname. Supply a
    screenshot of the resulting terminal.
