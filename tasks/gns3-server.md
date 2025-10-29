# WARNING - DO NOT THIS TASK UNLESS YOU ARE EXPLICTLY DIRECTED TO.
Failure to heed that warning will open your GNS3 to unauthenticated access and plausible distruction.

# The gHost that will serve as the GNS3 server with the shared project.

1. Gracefully save configurations and shutdown any project that is running in GNS3.

2. Shutdown GNS3 and restart it and select "cancel" in the open project dialog.  DO NOT open a project.

3. Select the Edit -> Preferenced Menu and select "Server" from the left hand navigation

4. Change the "Host binding" from `localhost` to `0.0.0.0`.

5. Get the password from the server `rep password ~/.config/GNS3/2.2/gns3_server.conf`

# On each gHost that will serve as a client. 

6. Un-check "Enable local server"

7. Enter the internal IP address of the gHost that will function as the server.

![](./images/gns3-server-settings.png)

8. Save the configuration.

9. Close and reopen GNS3.

10. The open projects dialog should show the projects from the "server" gHost.



# Loading local projects again
To reopen projects on each client gHost.  

1. Select the Edit -> Preferenced Menu and select "Server" from the left hand navigation

2. Check "Enable local server"

3. Save the configuration.

4. Close and reopen GNS3.
