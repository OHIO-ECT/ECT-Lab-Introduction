# Debugging Framework

## Goals

- Learn the structured network debugging methodology used in ITS 4750
- Apply the framework to a broken network scenario (no lab environment required)
- Internalize the process so it appears naturally in your lab reports this semester

## Resources

- Personal Computer (Desktop or Laptop)
- Lab notebook document
- No network environment required for this task

## Environmental Context

- No gHost, no GNS3, no ENE needed — this is a reasoning exercise

## The Debugging Framework

When something does not work on a network, the worst thing you can do is start randomly changing settings. The best thing you can do is follow a structured process. The framework used in ITS 4750 is:

1. **Gather** — Know what you have before you touch anything.  
   Run `ip a`, `ip route`, `ping <local gateway>`, `show interfaces` (on VyOS).  
   Document the current state. You cannot diagnose a problem you have not measured.

2. **Isolate** — Identify which layer the problem is at.  
   Work from the bottom up: Physical → Data Link → IP/Routing → DNS → Application.  
   Can you ping the local gateway? (IP works.) Can you ping 8.8.8.8? (Routing works.) Can you ping google.com? (DNS works.) Can you load a web page? (Application works.)

3. **Hypothesize** — Based on what you gathered and where it breaks, form a specific theory.  
   "The routing table has no default route" is a hypothesis. "Something is wrong" is not.

4. **Test** — Make **one change at a time** and observe the result.  
   If you change three things and it starts working, you do not know which one fixed it.

5. **Document** — Record what you tried and what happened, whether it worked or not.  
   Failed attempts are data. "I tried X and it did not help" is useful information for the next engineer (or future you).

Faculty and graders expect to see this process reflected in your lab reports. "I configured the interface and it worked" is not documentation. "I ran `ip a` and found no address on eth0, confirmed the interface was not configured, added the address, and verified connectivity with `ping`" is documentation.

## Apply the Framework

Read the following scenario and work through the framework in writing. There is no live environment — this is a reasoning exercise. Your answer should show your thinking, not just your conclusion.

---

**Scenario:**

A student has a GNS3 topology with:
- One VyOS router (R1)
- One Linux client (PC1) connected to R1's `eth0` interface
- R1's `eth1` interface connected to a Cloud node (simulated Internet access)

The student configured R1 and PC1 last week. Today, PC1 cannot reach the Internet (`ping 8.8.8.8` fails), but PC1 can still ping R1's `eth0` interface address (10.0.0.254).

---

Answer the following in your lab report:

1. What does the fact that PC1 can ping R1's eth0 but not 8.8.8.8 tell you about which layer the problem is at? Explain your reasoning.

2. Using the Gather step: list three specific commands you would run on R1, and three commands you would run on PC1, to collect information. State what each command tells you.

3. Using the Isolate step: given what you know so far, which two or three causes are the most likely explanations? (There is more than one plausible answer — show your reasoning.)

4. For your most likely hypothesis: what is the one change you would make to test it? What result would confirm it worked? What result would rule it out?

5. Write a two-sentence documentation entry in your lab report format summarizing what you found and what you did. Use CLI output formatting conventions (monospace font, concise).
