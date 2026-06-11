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

The `import-template.sh` script does everything automatically. It downloads the template
files from the server and imports them into GNS3. There is **no** need to download
anything manually from a browser.

1. Start the GNS3 application. It must be running **before** starting the script.

2. Open a project or create a new project. Then minimize the GNS3 application.

3. Review [ECT Tech Nugget N1.1 GNS3](https://www.youtube.com/watch?v=w5qsM3LhpQI) if necessary.

4. In GNS3, expand the "All Devices" menu from the "Devices Toolbar" on the left hand side of GNS3. This will show all available templates in GNS3.

5. Open a terminal window on the gHost machine and run the script:
```
./import-template.sh
```

6. The script opens the main menu. Templates already in the `~/Downloads` folder are
listed at the top; the menu options are at the bottom. The output looks similar to this:
```
========================================
  GNS3 Template Import Tool
========================================

Available Templates in ~/Downloads:
-----------------------------------
No .7z.001 files found in ~/Downloads

  [D] Download templates from server   [R] Refresh List
  [Q] Quit
-----------------------------------

Select a template number (or D to download, R/Q):
```

7. Type **D** and press Enter to download from the server. The script fetches the list
of available templates. Find **opnsense** in the list and type its number, then press Enter.
```
========================================
  Download Templates from Server
========================================
https://gns3.its.ohio.edu  (N available)   [PIN] = restricted
-----------------------------------
  [ 1] opnsense              OPNsense firewall appliance
  ...

  [B] Back to main menu
-----------------------------------

Select a template number to download (or B):
```
**Note:** Templates marked with **[PIN]** are restricted. Ask the instructor for the
PIN. If prompted, enter the PIN to download. Multi-part templates (`.7z.001`, `.7z.002`,
...) are downloaded automatically; there is no need to fetch each part individually.

8. After the download finishes, press Enter to return to the download list, then press
**B** to go back to the main menu. **opnsense** now appears in the "Available Templates"
list. Type its number and press Enter to import it.

9. The script extracts the archive and imports the template into GNS3. The progress
looks similar to this:
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
**Note:** If a post-extract script is detected, a password prompt may appear (sudo). Provide that your itsvm password (see text file on the desktop!)
Enter the password to continue.

10. There is a cleanup phase at the end. The script offers to delete the downloaded
`opnsense.7z.*` files now that the template is imported. This is normal and expected.
Type **y** when prompted:
```
Remove the .7z archive files? (y/n):
```

11. Press Enter to continue. Import another template or type **Q** to quit.

12. In GNS3, the newly imported **opnsense** template should now be visible in the GNS3 template list. Confirm it appears before finishing this task.
