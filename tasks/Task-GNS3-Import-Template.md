# GNS3 Import Template

## Goals
- Learn to import a new template object into GNS3

## Resources
- Personal Computer (Desktop or Laptop)
- Lab notebook document
- Assigned gHost (GNS3 Virtual Machine)
- [ECT/ITS Lab Notebook Cheatsheet](https://github.com/OHIO-ECT/Lab-Notebook-Cheat-Sheet)
- [ECT Tech Nugget Playlist](https://www.youtube.com/playlist?list=PLEA5GnkCPRTlvN_eyR99jOSsBCaV6khRS)
- [GNS3 GUI Documentation](https://docs.gns3.com/docs/using-gns3/beginners/the-gns3-gui)

## GNS3 Template Import

The `import-template.sh` script does everything automatically. It downloads the template files from the server and imports them into GNS3. There is **no** need to download anything manually from a browser.

1. Review [ECT Tech Nugget N1.1 GNS3](https://www.youtube.com/watch?v=w5qsM3LhpQI) **if necessary.**

2. Start the GNS3 application. It must be running **before** starting the script.

3. Open a project or create a new project. Then minimize the GNS3 application.

4. In GNS3, expand the "All Devices" menu from the "Devices Toolbar" on the left hand side of GNS3. This will show all available templates in GNS3.

5. Open a terminal window on the gHost machine and run the script:
```
./import-template.sh
```

6. The script opens the main menu. Templates already in the `~/Downloads` folder are listed at the top, each with a `[ ]` checkbox; the menu options are at the bottom. A number toggles a template's selection (its box becomes `[X]`); the letter keys perform actions. The `[C] Containers (Docker)` option imports Docker images and is not used in this task. The output looks similar to this:
```
========================================
  GNS3 Template Import Tool
========================================

Available Templates in ~/Downloads:
-----------------------------------
No .7z.001 files found in ~/Downloads

  [I] Import selected (0)             [X] Delete selected (0)
  [A] Select All                      [N] Select None
  [D] Download templates from server  [C] Containers (Docker)
  [R] Refresh List                    [Q] Quit
-----------------------------------

Number to toggle, or I/X/A/N/D/C/R/Q:
```

7. Press **D** to open the Download menu. The script fetches the list of available templates. Type the number next to **opnsense** to mark it `[X]` (more than one template may be marked), then press **G** to download the selected template(s).
```
========================================
  Download Templates from Server
========================================
https://gns3.its.ohio.edu  (N available)   [PIN] = restricted
-----------------------------------
  [ ] [ 19] opnsense          OPNsense firewall appliance
  ...

  Enter a number to toggle its selection.
  [A] Select All   [N] Select None
  [G] Download selected (0)   [B] Back   [Q] Quit
-----------------------------------

Choice (number / A / N / G / B / Q):
```
**Note:** Templates marked with **[PIN]** are restricted. Ask the instructor for the
PIN. A single PIN prompt covers the whole batch if any restricted template is selected. Multi-part templates (`.7z.001`, `.7z.002`, ...) are downloaded automatically; there is no need to fetch each part individually.

8. After the download finishes, the script returns to the main menu with **opnsense** already selected (`[X]`) in the "Available Templates" list. Press **I** to import the selected template(s).

9. The script extracts the archive and imports the template into GNS3. The progress looks similar to this:
```
========================================
Importing: opnsense
========================================

[1/5] Extracting archive...
[SUCCESS] Archive extracted
[2/5] Checking for post-extract script...
[3/5] Copying symbol files...
[4/5] Looking for GNS3 import configuration...
[5/5] Importing template to GNS3...
[SUCCESS] Template imported to GNS3

========================================
Import complete for: opnsense
========================================
```
**Note:** If a post-extract script is detected, a password prompt may appear (sudo). Enter the itsvm password (see the text file on the desktop) to continue.

10. The script imports all selected template(s), then prints a one-line summary such as `Imported 1, failed 0`. A cleanup phase follows: the script offers to delete the downloaded `opnsense.7z.*` files now that the template is imported. This is normal and expected. Type **y** when prompted:
```
Remove the .7z archive files for the imported template(s)? (y/n):
```

11. Press Enter to continue. Import another template or type **Q** to quit.

12. In GNS3, the newly imported **opnsense** template should now be visible in the "All Devices" list of the Devices Toolbar opened in step 4. Confirm it appears there before finishing this task.

13. Open Edit ▸ Preferences ▸ QEMU ▸ QEMU VMs and select the **opnsense** template to confirm it was registered as a QEMU VM. Arrange this window so it is visible next to the "All Devices" list.

## Lab Report Question(s)
The answers to these questions go into a quiz that's in the Learning Management System (LMS) for this course.
> **GNS3 Import Template Report Question:** Attach a screenshot (not with a phone!) showing both **opnsense** entries confirmed in steps 12 and 13, the "All Devices" list of the Devices Toolbar next to the QEMU VMs preferences page.