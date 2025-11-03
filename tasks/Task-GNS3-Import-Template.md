# GNS3 Import Template

## Goals
- Learn to import a new template object into GNS3

## Resources
- Personal Computer (Desktop or Laptop)
- A document you have created to use as a lab notebook
- Assigned gHost (GNS3 Virtual Machine)
- [ECT/ITS Lab Notebook Cheatsheet](https://github.com/OHIO-ECT/Lab-Notebook-Cheat-Sheet)
- [ECT Tech Nugget Playlist](https://www.youtube.com/playlist?list=PLEA5GnkCPRTlvN_eyR99jOSsBCaV6khRS)
  - [ECT Tech Nugget N46.0 - GNS3 - ECT GNS3 Template Import](https://www.youtube.com/watch?v=rSlpnUUqfz8&t=4s)
- [GNS3 GUI Documentation](https://docs.gns3.com/docs/using-gns3/beginners/the-gns3-gui)

## GNS3 Template Import

1. Start the GNS3 application. It must be running for the import to work.

2. Open a project or create a new project. Then minimize the GNS3 application.

3. Review [ECT Tech Nugget N1.1 GNS3](https://www.youtube.com/watch?v=w5qsM3LhpQI) if necessary.

4. Expand the "All Devices" menu from the "Devices Toolbar" on the left hand side of GNS3.

5. Open a browser window on the gHost machine. Navigate to: [https://gns3.its.ohio.edu](https://gns3.its.ohio.edu)

6. At the top of the file listing find the yellow box for "import-template.sh". To update the import script run the following command in a terminal window on the gHost machine:
``` 
wget -O import-template.sh.tmp http://gns3.its.ohio.edu/import-template.sh && cat import-template.sh.tmp > import-template.sh && rm import-template.sh.tmp
```

7. Use the search bar to filter the list of templates to import. For example, all files that start with "kali" are for the Kali Linux template. Click on download and the files will be downloaded into the "Downloads" folder.<br>
**Note:** Some templates have multiple files. All files for the template must be downloaded for the import.<br>

9. Once the downloads are completed. Open a terminal window on the gHost machine.

10. Change to the Downloads folder by typing the following command:
```cd Downloads```

1.  Run the script, when prompted provide the name of the template to import. **For example,** to import the Kali Linux template type the following command:
```bash import-template.sh```

Output should look like this:
```Importing GNS3 Template
Get templates from https://www.its.ohio.edu/gns3
Script for use with the itsvm user!
GNS3 is running
This script looks for files in your ~/Downloads folder.
Enter filename (no path, no extensions) : 
```
In our example, type "kali" and press enter.

11. The script will then extract the files and import the template into GNS3.

12. There is a cleanup phase at the end of the script. If prompted with ``rm: remove regular file '/home/itsvm/Downloads/kali.7z.001'?`` the script will delete the kali.7z.* files. This is normal and expected. Type "y" and press enter. 

13. The template should now be available in the "All Devices" menu in GNS3. Press 
