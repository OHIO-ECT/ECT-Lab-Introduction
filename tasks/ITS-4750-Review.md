# ITS 4750 Labs

This introduction is **async primer material** - Even through is not a graded exercise students should read and review this document thoroughly.  Students are encouraged to engage with the online learning tools and resources documented in this Introductory lab to review to prime concepts from ITS 2300 and ITS 3100.  Students should have an advanced understanding of these tools and networking concepts prior to starting this class.  (This will be you last warning)

# Tech Nuggets

The ECT Tech Nuggets are short instructional videos produced by the department.  These are meant to complement lectures not replace them.

**Channel:** https://www.youtube.com/@ecttechnuggets9126

| Watch | Topic |
|-------|-------|
| [N0.1](https://www.youtube.com/watch?v=OtpzbVz7Ay8) | Basic Diag Tools - NIC Setting Discovery |
| [N0.2](https://www.youtube.com/watch?v=hWeJlNVaUbU) | Basic Diag Tools - Ping and Traceroute |
| [N0.3](https://www.youtube.com/watch?v=PMk53TngTio) | Basic Diag Tools - Netstat |
| [N0.4](https://www.youtube.com/watch?v=gD-Tk1Bk7x0) | Basic Diag Tools - Dig and Nslookup |
| [N0.5](https://www.youtube.com/watch?v=QTIbS9wyfag) | Basic Diag Tools - Wireshark |
| [N0.6](https://www.youtube.com/watch?v=Vu1CeJIXMnk) | Basic Diag Tools - NIC Config |
| [N1.1](https://www.youtube.com/watch?v=w5qsM3LhpQI) | GNS3 |
| [N1.2](https://www.youtube.com/watch?v=X_LX4MCR1do) | GNS3 |
| [N1.3](https://www.youtube.com/watch?v=5ZZjxAYcy5Q) | GNS3 |
| [N2.1](https://www.youtube.com/watch?v=uwa7w37LhF0) | IPv4 Subnetting pt1 |
| [N2.2](https://www.youtube.com/watch?v=K-yAX1OHNSI) | IPv4 Subnetting pt2 |
| [N2.3](https://www.youtube.com/watch?v=A_JbKcmjyts) | Binary Subnetting |
| [N3.0](https://www.youtube.com/watch?v=nx7PfG7_Fks) | Routing pt1 |
| [N3.1](https://www.youtube.com/watch?v=gVAEopOYGa0) | Routing pt2 |
| [N4.0](https://www.youtube.com/watch?v=POqlACy94ys) | VyOS + GNS3 pt1 |
| [N4.1](https://www.youtube.com/watch?v=xtt3UO4gW7A) | VyOS + GNS3 pt2 |
| [N5.0](https://www.youtube.com/watch?v=uyUL9UQugek) | NAT |
| [N6.0](https://www.youtube.com/watch?v=p9ARba9keE8) | DHCP |
| [N6.1](https://www.youtube.com/watch?v=ja_n-MZZxD4) | DHCP |
| [N8.0](https://www.youtube.com/watch?v=igPK1aZo4m8) | IPv6 Intro |
| [N11.0](https://www.youtube.com/watch?v=43F51qVz9Ds) | nmcli |

## Lab IP Addressing Conventions

As show in the IPv4 Subnetting and IPv6 Intro technuggets, as a generalized process an organization or a network within an organization is given an IP address space which a network administrator will take and further subnet based on the demands of the sub-networks (subnets) that are within the network being constructed.  The [ECT Visual Subnet Calculator](https://www.its.ohio.edu/ipcalc/) is a handy tool to automate this process.  A network administrators ability to properly manage IP space is a direct reflection of their 

TODO: Brandon Stopped here.



These conventions MUST be used for IP address assignment in all ITS 4750 assignments for the entire semester.

- A1. IPv4 default gateway (Router) will use the **last usable address** in the IP Network
- A2. IPv6 default gateway (Router) will use **::1** IP
- B. All other static assigned IPs (including other routers that are not the default gateway) start at the **beginning of the range**
- C. DHCP pools are between the statically addressed clients and the Default Gateway
- D. Unless stated otherwise use the following DNS Name servers: **132.235.9.75, 132.235.200.41**



# Section 3 - ENE: Network Simulation Without GNS3

**New this semester:** Confirm that the ECT Network Emulator (ENE) loads in your browser - open https://www.its.ohio.edu/ene/ and verify you can see the canvas. ENE requires no install, no VMs, and no gHost access. You will use it in Section 3.

The ECT Network Emulator (ENE) runs entirely in your browser. No installation, no VMs, no gHost required. You will use it here to explore basic network concepts and observe the protocols that underpin every lab this semester - all before you touch GNS3.

**ENE URL:** https://www.its.ohio.edu/ene/  
**ENE Docs:** https://www.its.ohio.edu/ene/docs/

## Task 3a - ENE Orientation

- [Task 3a - ENE Orientation](../tasks/Task-ENE-Orientation.md)  
    Open ENE, build a small topology, and observe the results. This is your first look at a live (simulated) network before GNS3.

## Task 3b - ENE Subnetting Exercise

- [Task 3b - ENE Subnetting Exercise](../tasks/Task-ENE-Subnetting.md)  
    Apply the IP conventions below to a simple topology in ENE. This is the first time you will use the class IP addressing rules in a live context - the same rules appear on every lab rubric for the rest of the semester.

## Task 3c - Protocol Refresher

- [Task 3c - Protocol Refresher](../tasks/Task-Protocol-Refresher.md)  
    Using the ENE topology you built in Tasks 3a and 3b, work through six protocol areas: IPv4 native connectivity, IPv6 link-local addressing, core diagnostic tools (ping, traceroute, link sniffer), DHCP, NAT, and DNS. Each section asks you to observe the protocol from both the server/router side and the client side.


## Task 4b - Terminal Shell and File Management

- [Task 4b - Terminal Shell and File Management](../tasks/Task-Terminal-Shell-and-File-Management.md)  
    Students will master a number of CLI interfaces to network and server equipment. Identify a command or tip not presented in this task.

# Section 5 - Network Diagnostics and Problem Solving

The tools in this section are the first things you reach for when something does not work. The debugging framework below is explicitly how faculty and graders expect you to approach lab problems - model it in your lab reports.

## Task 5a - Gathering IP Information

- [Task 5a - Gathering IP Information](../tasks/Task-Gathering-IP-Information.md)  
    Before you change anything, know what you have. Gather and document the network interface information for the interfaces connected to the cloud. Different runs of a particular network are very unlikely to reproduce the same results, particularly on client machines.

    This is **Step 1 of the debugging process.** You cannot diagnose a problem you have not first measured.

## Task 5b - Network Diagnostic Tools and Debugging Framework

- [Task 5b - Network Diagnostic Tools](../tasks/Task-Advanced-Network-Diagnostic-Commands.md)  
    These are must-have tools. Give example data from each tool and explain its operation.

- [Task 5b - Debugging Framework](../tasks/Task-Debugging-Framework.md)  
    The structured process for isolating and resolving network problems. Learn this framework now - faculty expect to see it applied in every lab report this semester.

    The framework is:
    1. **Gather** - What do I have? (`ip a`, `ip route`, `ping` local GW)
    2. **Isolate** - Layer by layer: physical? IP? routing? DNS? application?
    3. **Hypothesize** - What could cause this symptom?
    4. **Test** - Make one change at a time.
    5. **Document** - What did you try and what happened?

    **Brutally direct hint:** Don't ask for help without having worked through at least the first three steps.

## Task 5c - Wireshark

- [Task 5c - Wireshark](../tasks/Task-Wireshark.md)  
    Packet capture tools let the network engineer see what is actually on the wire. Show the packet capture data using the proper export format, nicely presented. Highlighting critical data in a packet capture is always appreciated.

    Speaking of needles and haystacks: show exactly the packets relevant to the task. Do not dump a full capture when a filtered summary was asked for.

---

# Section 6 - Documentation Standards

Documentation is not optional and not an afterthought. The ability to draw a clear, annotated network diagram and to shut down infrastructure cleanly are professional skills you will use on day one of any network engineering job.

## Task 6a - Drawing Diagrams

- [Task 6a - Drawing Diagrams](../tasks/Task-Drawing-Diagrams.md)  
    Draw.io is required. Screenshots and image exports from GNS3 are NEVER a substitute for a drawn diagram. A drawn diagram shows design intent and network relationships in a way that a screenshot never can.

    Every lab diagram must include: network numbers, subnet masks (or prefix lengths), interface IP addresses, and device names. Missing any of these is a recurring rubric deduction.

## Task 6b - Shutdown GNS3

- [Task 6b - Shutdown GNS3](../tasks/Task-Shutdown-GNS3.md)  
    Why would we ask students to shut down a project when the work is complete? Be concise in your answer.

---

# Proper Submissions

Unless otherwise specifically noted, students MUST submit PDF formatted documents!

---

# Miscellaneous Tasks (For Information Only)

- [SSH Jump Host](../tasks/Task-SSH-Jumphost.md)  
    gHosts and devices in projects can be accessed via SSH through a security bastion described in this task. This option is NOT normally used.
