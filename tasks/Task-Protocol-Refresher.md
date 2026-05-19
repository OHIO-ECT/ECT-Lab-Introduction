# Protocol Refresher

## Goals

- Observe IPv4 native connectivity from first principles: addressing, forwarding, and verification
- Identify IPv6 link-local addresses and understand why they appear automatically
- Use the core diagnostic tools (ping, traceroute, link sniffer) to characterize network behavior
- See DHCP from both sides: what the server configures and what the client receives
- Observe NAT in action: how source addresses change as traffic crosses a router boundary
- Resolve names using DNS and understand the client-to-server transaction

## Resources

- Personal Computer (Desktop or Laptop) with a modern web browser
- Lab notebook document
- ENE URL: https://www.its.ohio.edu/ene/
- ENE Docs: https://www.its.ohio.edu/ene/docs/

## Environmental Context

- Personal PC and browser — no gHost, no VMs, no install required
- ENE runs entirely in the browser
- This task uses a single topology to observe all protocol areas

## Build the Topology

Before exploring any protocol, build the following topology in ENE. You will use it for all sections of this task.

1. Open https://www.its.ohio.edu/ene/ and start a new canvas.

2. Place the following devices:
    - 1x **Cloud** (represents the simulated ISP/Internet connection)
    - 1x **Router** — label it `R1`
    - 1x **Switch** — label it `SW1`
    - 1x **Client** — label it `Client1`
    - 1x **DNS Server** — label it `NS1`

3. Connect the devices:
    - `R1` eth0 → `Cloud`
    - `R1` eth1 → `SW1`
    - `Client1` → `SW1`
    - `NS1` → `SW1`

4. Configure `R1`:
    - eth0 (WAN): obtain address from Cloud (DHCP client or the address the Cloud assigns)
    - eth1 (LAN): set a static IP of `10.10.10.254/24`
    - Enable **DHCP server** on eth1: pool range `10.10.10.10` – `10.10.10.200`, gateway `10.10.10.254`, DNS pointing to `NS1`
    - Enable **NAT** (masquerade) toward eth0

5. Configure `NS1`:
    - Static IP: `10.10.10.2/24`, gateway `10.10.10.254`
    - Add at least two A records, for example: `client1.lab` → `10.10.10.11` and `server.lab` → `10.10.10.2`

6. Leave `Client1` set to DHCP — it should receive an address automatically when the topology starts.

7. Start the topology. Confirm that `Client1` has received a `10.10.10.x` address before proceeding.

---

## Part A — IPv4 Native Connectivity

IPv4 is the protocol that identifies every device on the network with a 32-bit address and describes how packets are forwarded from source to destination. Every other protocol in this task depends on IPv4 being functional first.

8. Open the shell on `Client1`. Run `ip a` (or `ifconfig`) and record:
    - The IP address and prefix length assigned to the client's interface
    - The MAC (hardware) address of the interface

9. Run `ip route` (or `route -n`) on `Client1` and record:
    - The default gateway entry
    - What the default gateway IP is, and which device it corresponds to in your topology

10. From `Client1`, ping the gateway: `ping 10.10.10.254`
    - Record the round-trip time (RTT)

11. From `Client1`, ping `NS1` at `10.10.10.2`:
    - Does this ping cross a router, or does it stay on the same network? Explain your reasoning using the subnet mask.

12. From `Client1`, ping an external address through the Cloud (use a destination provided by ENE's Cloud device, such as `8.8.8.8` or the address shown in the Cloud config).
    - Record whether the ping succeeds and the approximate RTT.

**Deliverable A:** In your lab report, describe the IP address assignments in this topology and explain the path a ping from Client1 to 8.8.8.8 takes — which devices does it pass through, and at which point does the source address change?

---

## Part B — IPv6 Native Connectivity

IPv6 uses 128-bit addresses. One of its key features is **link-local auto-configuration**: every IPv6-capable interface automatically generates a link-local address in the `fe80::/10` range without any manual configuration or DHCP. These addresses are only valid on the local link segment.

13. On `Client1`, run `ip a` again and look for an address beginning with `fe80::`. Record the full link-local address.

14. On `NS1`, run `ip a` and record its link-local address.

15. From `Client1`, ping `NS1` using its IPv6 link-local address. The syntax on Linux is:
    `ping6 <fe80::address>%<interface-name>`
    For example: `ping6 fe80::1%eth0`

    Record whether the ping succeeds. If it does not, note what error you receive.

> **Note:** ENE's Router does not currently support IPv6 routing between subnets. Full IPv6 routing — including stateless address autoconfiguration (SLAAC), DHCPv6, and OSPFv3 — is covered in the GNS3 lab environment starting with Lab 7. What you observed here is IPv6 **link-local only**: automatic and always present, but limited to the local segment.

**Deliverable B:** Record the link-local address on Client1 and NS1. Explain in one sentence why they appeared without any configuration.

---

## Part C — Core Diagnostic Tools

These are the first tools you reach for when something doesn't work. You will use them in every lab this semester.

### Ping

Ping sends ICMP echo requests and measures whether the destination is reachable and how long the round trip takes.

16. From `Client1`, run: `ping 10.10.10.254` and `ping 10.10.10.2`
    - What does a successful ping tell you? What does a failed ping tell you?
    - Ping is a **binary answer**: yes it responds, or no it does not. It does not tell you *why* something is unreachable.

### Traceroute

Traceroute maps the path from source to destination hop by hop, using the TTL (Time to Live) field in the IP header.

17. From `Client1`, run: `traceroute -n 8.8.8.8` (the `-n` flag suppresses DNS lookups, which keeps the output clean during diagnostics).
    - How many hops are shown?
    - Which hop is R1? How do you know?

18. Run `traceroute -n 10.10.10.2` from `Client1`.
    - How is this traceroute different from the one to 8.8.8.8? Why?

### Link Sniffer (Wireshark-style)

ENE includes a per-link packet sniffer. It shows you the actual frames and packets on a given link — the same view Wireshark gives you on a physical interface.

19. Click on the link between `Client1` and `SW1` to open the link sniffer. Start the capture.

20. From `Client1`, run one ping to `10.10.10.254`. Stop the sniffer capture.
    - Find the ICMP echo request and echo reply in the capture.
    - Note the source and destination IP addresses in each direction.
    - Note the source and destination MAC addresses. Whose MAC address is in the "destination" field of the request?

> The detailed use of Wireshark in GNS3 is covered in Task 5c. What you're doing here is learning to read a packet capture at the most basic level.

**Deliverable C:** In your lab report: (1) state what a failed ping to the default gateway tells you about the problem and what it does NOT tell you, (2) interpret one line from your traceroute output, and (3) identify the source and destination MAC addresses in your ping capture and explain why the destination MAC is R1's, not NS1's, even though the destination IP is NS1's.

---

## Part D — DHCP

DHCP (Dynamic Host Configuration Protocol) automates IP address assignment. Rather than manually configuring every host, a DHCP server maintains a pool of addresses and hands them out on request. The exchange follows a four-step process: **Discover → Offer → Request → Acknowledge (DORA)**.

21. On the link between `Client1` and `SW1`, open the link sniffer and start a new capture.

22. On `Client1`, force a DHCP renewal: run `dhclient -r eth0 && dhclient eth0` (release, then re-request).

23. Stop the sniffer. Look for the DHCP exchange in the capture.
    - Identify which packet is the Discover and which is the Offer.
    - What source IP does the Discover use, and why? (Hint: the client does not have an IP yet.)
    - What destination IP does the Discover use, and why?
    - What address did the server offer to the client?

24. Examine the R1 DHCP server configuration. Note:
    - The pool start and end addresses
    - The default gateway value distributed to clients
    - The DNS server value distributed to clients

**Deliverable D:** In your lab report, draw or describe the DORA exchange in your capture. For each of the four steps, identify the source IP, destination IP, and what information is being exchanged.

---

## Part E — NAT

NAT (Network Address Translation) allows many hosts on a private network to share a single public (routable) IP address. When a packet from `Client1` crosses R1 to reach the Cloud, R1 rewrites the source IP from `Client1`'s private address to R1's WAN address. The return packet is translated back.

25. Record R1's WAN IP address (eth0). You can see it in R1's configuration or by running `ip a` on R1 if ENE provides CLI access to routers.

26. Open the link sniffer on the link between `R1` and the Cloud. Start a capture.

27. From `Client1`, ping `8.8.8.8` (or the Cloud's external address).

28. Stop the sniffer. Find the ICMP packets on the R1→Cloud link.
    - What is the source IP address of the ping as it leaves R1's WAN interface?
    - Compare this to Client1's IP address. Are they the same?

29. Now open the link sniffer on the link between `SW1` and `R1` (the LAN side). Repeat the ping.
    - What is the source IP address of the ping on the LAN side?
    - At which device and interface does the address translation happen?

**Deliverable E:** In your lab report, state Client1's IP, R1's WAN IP, and the source IP seen on the WAN link when Client1 pings 8.8.8.8. Explain in two sentences why NAT exists and what problem it solves.

---

## Part F — DNS

DNS (Domain Name System) translates human-readable names (like `server.lab`) into IP addresses. The client sends a query to its configured DNS server; the server looks up the name and returns the address. Without DNS, every application would require users to remember IP addresses.

30. On `Client1`, run: `nslookup client1.lab`
    - What IP address is returned?
    - What server answered the query? (nslookup shows the server that responded.)

31. Run: `nslookup server.lab`
    - What IP address is returned?

32. Run: `dig server.lab`
    - Find the **ANSWER SECTION** in the dig output.
    - What is the TTL value shown? What does TTL mean in the context of a DNS record?

33. Examine the NS1 DNS server configuration in ENE.
    - What are the A records configured on NS1?
    - What do A records do?

34. From `Client1`, run: `nslookup 10.10.10.2`
    - This is a **reverse lookup** — translating an IP back to a name.
    - Does NS1 have a reverse record configured? What happens when it does not?

**Deliverable F:** In your lab report: (1) show the dig output for `server.lab` with the ANSWER SECTION highlighted, (2) identify the DNS server that responded, and (3) explain in one sentence the difference between an A record and a reverse (PTR) record.
