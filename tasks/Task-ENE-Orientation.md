# ENE Orientation

## Goals

- Open the ECT Network Emulator (ENE) and confirm it works in your browser
- Build a minimal topology and observe live network behavior
- Take your first look at a simulated network before working in GNS3

## Resources

- Personal Computer (Desktop or Laptop) with a modern web browser
- Lab notebook document
- ENE URL: https://www.its.ohio.edu/ene/
- ENE Documentation: https://www.its.ohio.edu/ene/docs/

## Environmental Context

- Personal PC and browser — no gHost, no VMs, no install required
- ENE runs entirely in the browser

## ENE Orientation

ENE (ECT Network Emulator) is a browser-based network simulation tool. It supports real network protocols including DHCP, NAT, DNS, and basic routing — all without requiring GNS3 or a gHost VM. You will use it in this introduction and in early course activities to build familiarity with network concepts before moving to GNS3.

### Build a simple topology

1. Open https://www.its.ohio.edu/ene/ in your browser. Confirm that the ENE canvas loads. If you see an error or blank page, check the ENE documentation at https://www.its.ohio.edu/ene/docs/ before asking for help.

2. From the device palette, place the following devices on the canvas:
    - One **Client**
    - One **Router**
    - One **Cloud**

3. Connect the devices:
    - Connect the **Client** to the **Router**
    - Connect the **Router** to the **Cloud**

4. Open the **Client** shell (click on the Client device to access its terminal interface).

5. In the Client shell, run `ifconfig` (or `ip a` if ifconfig is not available) and observe the output.

### Deliverables

6. Take a **screenshot of the ENE canvas** showing your topology with all three devices connected. This is one of the rare cases where a screenshot is the appropriate form of documentation — ENE is a graphical interface.

7. In your lab report, describe what you see in 2–3 sentences:
    - What IP address was assigned to the Client?
    - How did the Client get that address?
    - What does the connection between the Router and Cloud represent?
