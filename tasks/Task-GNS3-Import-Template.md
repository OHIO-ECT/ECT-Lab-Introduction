# GNS3 Import Template

## Goals
- Learn to import a new template object into GNS3

## Resources
- Personal Computer (Desktop or Laptop)
- A document you have created to use as a lab notebook
- Assigned gHost (GNS3 Virtual Machine)
- [ECT/ITS Lab Notebook Cheatsheet](https://github.com/OHIO-ECT/Lab-Notebook-Cheat-Sheet)
- [ECT Tech Nuggets Playlist](https://www.youtube.com/playlist?list=PLEA5GnkCPRTlvN_eyR99jOSsBCaV6khRS)
- [GNS3 GUI Documentation](https://docs.gns3.com/docs/using-gns3/beginners/the-gns3-gui)

## GNS3 Template Import

1. Start the GNS3 application. It must be running for the import to work.

2. Open a project or create a new project. Then minimize the GNS3 application.

3. If necessary, review [ECT Tech Nugget N1.1 GNS3](https://www.youtube.com/watch?v=w5qsM3LhpQI)

4. Expand the "All Devices" menu from the "Devices Toolbar" on the left hand side of GNS3.

5. Open a browser window on the gHost machine. Navigate to: [https://www.its.ohio.edu/gns3](https://www.its.ohio.edu/gns3)

6. Download the file "import-template.sh". Save the file to the "Downloads" folder on the gHost machine.

7. Download all files for the template you wish to import. For example, all files that start with "kali" are for the Kali Linux template. They should be downloaded into the "Downloads" folder.

8. Once the downloads are completed. Open a terminal window on the gHost machine.

9. Change to the Downloads folder by typing the following command:
```cd Downloads```

10. Make the script executable by typing the following command (you will be prompted for the itsvm password):
```sudo chmod +x import-template.sh```

11. Run the script, when prompted provide the name of the template you wish to import. For example, to import the Kali Linux template type the following command:
```./import-template.sh```

```Importing GNS3 Template
Get templates from https://www.its.ohio.edu/gns3
Script for use with the itsvm user!
GNS3 is running
This script looks for files in your ~/Downloads folder.
Enter filename (no path, no extensions) : 
```
In our example, type "kali" and press enter.

12. The script will then extract the files and import the template into GNS3.

13. There is a cleanup phase at the end of the script. If you respond ``rm: remove regular file '/home/itsvm/Downloads/kali.7z.001'?`` the script will delete the kali.7z.* files. This is normal and expected. Type "y" and press enter. 

14. The template should now be available in the "All Devices" menu in GNS3. Press 
