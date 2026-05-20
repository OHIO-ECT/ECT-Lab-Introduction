# ECT Lab Introduction - Lab Reports

# Section 6 - Documentation Standards

Documentation is not optional and not an afterthought. The ability to draw a clear, annotated network diagram and to shut down infrastructure cleanly are professional skills you will use on day one of any network engineering job.

## Task 6a - Drawing Diagrams

- [Task 6a - Drawing Diagrams](../tasks/Task-Drawing-Diagrams.md)  
    Draw.io is required. Screenshots and image exports from GNS3 are NEVER a substitute for a drawn diagram. A drawn diagram shows design intent and network relationships in a way that a screenshot never can.

    Every lab diagram must include: network numbers, subnet masks (or prefix lengths), interface IP addresses, and device names. Missing any of these is a recurring rubric deduction.
    
## Course conventions - read these now

These conventions apply to every submission in this course, starting with Lab 1.

- Lab reports must be submitted as Microsoft Word Word.
- **Drawn diagrams always.** Network diagrams must be drawn using Draw.io or equivalent. Screenshots or image exports from GNS3 are never a substitute for a drawn diagram. See [Diagrams vs. Pictures Policy](../Documentation/000%20-%20Diagrams%20vs%20pictures%20policy.docx) for the full rationale.
- **CLI output in fixed-width font.** All command-line output in your lab report must use a monospace font (Courier New or equivalent). Output in a proportional font is unreadable and will be penalized.
- **Concise answers.** Faculty and graders will not search for needles in haystacks. Show exactly what was asked - no more. Dumping full Wireshark captures when a single summary line was requested is a recurring failure mode.
- **Read the rubric.** Check the grading rubric for each submission. Consider every prompt carefully before writing your answer.

```
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                READ THAT PART AGAIN
                IGNORE AT YOUR OWN RISK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

Full documentation standards are at [ITS Lab Reports](../tasks/ITL-Lab-Report.md)

# Task 5 - Documentation Standards

Documentation is not optional and not an afterthought. The ability to draw a clear, annotated network diagram and to shut down infrastructure cleanly are professional skills you will use on day one of any network engineering job.

- [Task 6a - Drawing Diagrams](../tasks/Task-Drawing-Diagrams.md)  
Draw.io is required. Screenshots and image exports from GNS3 are NEVER a substitute for a drawn diagram. A drawn diagram shows design intent and network relationships in a way that a screenshot never can.

Every lab diagram must include: network numbers, subnet masks (or prefix lengths), interface IP addresses, and device names. Missing any of these is a recurring rubric deduction.

## Industry impetus

The criteria for lab reports in this class are defined by the following observations:

- ALL well maintained enterprise networks are highly documented.
- Network engineers are regularly called upon to identify, resolve, and document complex problems.
- Network engineers must be able to effectively communicate with non-technical contributors (Board of Directors, CEO, CIO, manager, customer, support, purchasing, sales, etc.)

Examples of documents that network engineers may encounter in the industry:

- Proposed changes to an existing network
- Documentation of major outages
- Purchasing requests
- Request for Proposals (RFP)
- Design documentation for new networks.

Lab Reports are to be written individually (no group work). Reports will be uploaded to Canvas electronically as a **PDF** (ONLY!). Reports do not generally need to be more than several pages. Officially, they need to be "long enough to answer the questions".

An example lab report format doc: https://github.com/OHIO-ECT/ECT-Lab-Introduction/blob/main/files/ITL%20-%20Lab%20Report%20Example.pdf

There is also a Wireshark Exporting Guide: https://github.com/OHIO-ECT/Wireshark-Export-Guide

It is expected that students will read and follow these guidelines and examples.

Each lab report must have a header (**no cover pages!**) on the first page that includes:
- Student Name
- Lab section attended
- Student program affiliation (CS ugrad, CS grad, ITS ugrad, ITS grad, etc.)
- No cover sheets!
- Number your answers with the same numbers as the Lab Report Questions.
- No appendixes! 
- For terminal window data (ping, traceroute, netstat etc.) data should be formatted with a fixed width font like courier to preserve the columns and displayed as shown on screen.
- Absolutely **NO SCREEN SHOTS!** (with your phone camera or screen shot tool) There are extremely rare cases when a screen shot (usually for a web interface) will be required. This will be noted in the assignment instructions.
- Wireshark: It is absolutely NOT acceptable to provide screen shots of any kind for Wireshark data ever! Export to text.
- Terminal window (CLI) data needs to be reformatted to remove the extra line breaks. While this report is long future ones will be **much** longer. Removing the extra line breaks will save much space. A smaller font can also be used for terminal window data or adjust margins for that data to stop line wrapping.
