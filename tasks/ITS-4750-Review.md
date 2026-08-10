# ITS 4750 Labs

This introduction is **async primer material** - Even through is not a graded exercise students should read and review this document thoroughly.  Students are encouraged to engage with these online learning tools and resources in this Introductory "lab" to review prime concepts from ITS 2300 and ITS 3100.  

Successful Students will have an understanding of these tools and networking concepts prior to starting this class.  (This will be your last warning)

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

# IP Addressing Conventions

Organization or a network within an organization is given a "block" of IP address space.  A network administrator will take that IP space  and further divid it based on the demands of the sub-networks (subnets) that are within the network being constructed.  This class is "dual-stack" and will use both IPv4 and IPv6.  Subnetting each of these address types have slighly different techniques.

For IPv4 the [ECT Visual Subnet Calculator](https://www.its.ohio.edu/ipcalc/) is a handy tool to automate this process.  For IPv6, Professor Saunders, recommends that students NOT use a subnet calculator.  See the IPv6 Intro TechNugget for the basics of subnetting in IPv6.  More advanced subnetting techniques will be discussed in class.

Within a subnetwork this class requires a set of policies that must be adhered to.  These policies might differ from the practices of other organizations.

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

Dr. Bowie has also produced a set of Ene based ITS-2300 labs.  Students who wish to gain access to those labs must complete the [GitHub Account Creation](../tasks/Task-GitHub-Account-Creation.md) and EMAIL their account name to Professor Saunders


