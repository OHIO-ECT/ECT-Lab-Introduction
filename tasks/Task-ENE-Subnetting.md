# ENE Subnetting Exercise

## Goals

- Apply ITS 4750 IP addressing conventions to a live (simulated) network topology
- Assign addresses correctly and verify end-to-end connectivity
- Prime Lab 1 by experiencing the IP planning + configure + verify cycle before GNS3

## Resources

- Personal Computer (Desktop or Laptop) with a modern web browser
- Lab notebook document
- ENE URL: https://www.its.ohio.edu/ene/
- ITS 4750 Lab Network Conventions (in `course_guides/ITS-4750.md`, Section 3)
- Completed Task-Art-of-IP-Assignment (IP plan fluency expected)

## Environmental Context

- Personal PC and browser — no gHost, no VMs, no install required
- ENE runs entirely in the browser

---

> **🚧 INSTRUCTOR NOTE — PENDING DOUG'S ENE SLATE**
>
> This task requires a pre-built ENE slate (a saved topology) with:
> - A single router with two LAN interfaces and one Cloud connection
> - Two client segments (one DHCP, one static)
> - A password-protected answer key
>
> Doug Bowie (bowie@ohio.edu) is developing this slate. When the slate is ready:
> 1. Replace this notice with the slate download link or ENE import instructions
> 2. Add the specific subnet assignment problem (network address, prefix length, host requirements)
> 3. Link or embed the IP grid template students should complete before configuring
> 4. Update the deliverables section with the specific ping targets to verify
>
> Until the slate is available, students who have completed Task-ENE-Orientation and Task-Art-of-IP-Assignment have the necessary background. This task will be released when the slate is ready.

---

## Background

This exercise bridges the paper-and-pencil IP planning you did in Task-Art-of-IP-Assignment with the live configuration work you will do in Lab 1. The steps are the same ones you will follow every week:

1. Receive a network description (addresses, host requirements, topology)
2. Produce an IP plan before touching any device
3. Configure the devices to match the plan
4. Verify connectivity

## The Exercise

*(Full instructions will appear here when Doug's ENE slate is available. The sections below are the intended structure.)*

### Step 1 — Load the ENE slate

Import or open the provided ENE topology file. Do not modify the topology — only configure the addresses.

### Step 2 — Complete the IP grid

Using the provided topology description and the ITS 4750 IP conventions, fill in the IP grid:
- Network addresses and prefix lengths for each subnet
- Default gateway address for each subnet (convention A1)
- Static host addresses (convention B)
- DHCP pool range (convention C)
- DNS servers (convention D)

Submit the completed IP grid as a pre-lab deliverable before configuring anything.

### Step 3 — Configure the devices

Apply the addresses from your IP grid to the devices in ENE.

### Step 4 — Verify connectivity

Using the Client shell in ENE, verify end-to-end connectivity:
- Ping the default gateway from each client
- Ping across the router between the two segments
- Ping an external address through the Cloud connection

### Deliverables

- Completed IP grid (submitted before configuration)
- Screenshot of a successful ping between the two client segments
- Screenshot of a successful ping to an external address
- One-sentence explanation of how the DHCP client received its address
