## 1. Basic File & Directory Commands
 pwd

What it does: Prints the current working directory.

When to use: When you want to know which directory you're currently in.

Example:

$ pwd  
/home/user/Documents

 ls

What it does: Lists files and directories in the current folder.

When to use: To see what files are present in the directory.

Example:

$ ls  
file1.txt  dir1  script.sh

 ls -l

What it does: Lists files with detailed information (permissions, owner, size, date).

When to use: When you want to inspect file metadata.

Example:

$ ls -l  
-rw-r--r-- 1 user user 1024 Sep 10 10:00 file1.txt

 ls -a

What it does: Lists all files, including hidden ones (files starting with ., e.g., .bashrc).

When to use: To view configuration files or hidden data.

 cd <directory>

What it does: Changes the current working directory.

When to use: To navigate the filesystem.

Example:

$ cd /var/log

 mkdir <directory>

What it does: Creates a new directory.

When to use: To organize files by placing them into directories.

Example:

$ mkdir projects

 touch <file>

What it does: Creates an empty file or updates the timestamp of an existing file.

When to use: To quickly create files.

Example:

$ touch newfile.txt

 cp <source> <destination>

What it does: Copies a file or directory to another location.

When to use: When you need a backup or duplicate of a file.

Example:

$ cp file1.txt /home/user/backup/

 mv <source> <destination>

What it does: Moves or renames a file/directory.

When to use: To relocate or rename files.

Example:

$ mv file1.txt file2.txt

 rm <file>

What it does: Deletes a file.

When to use: To remove unnecessary or temporary files.

Example:

$ rm file1.txt

 rm -r <directory>

What it does: Recursively deletes a directory and its contents.

When to use: To remove directories with files inside.

Example:

$ rm -r old_project

 cat <file>

What it does: Outputs the entire content of a file to the terminal.

When to use: To quickly see the whole file content.

Example:

$ cat file1.txt

 more <file>

What it does: Displays file content page by page.

When to use: For large files where content doesn’t fit in one screen.

 less <file>

What it does: Like more but supports scrolling up and down.

When to use: When you need to view large files and navigate them freely.

 head <file>

What it does: Shows the first 10 lines of a file.

When to use: To peek at the start of a log or configuration file.

Example:

$ head access.log

 tail <file>

What it does: Shows the last 10 lines of a file.

When to use: Useful for viewing recent log entries.

 tail -f <file>

What it does: Follows file changes in real time.

When to use: For monitoring live log updates.

Example:

$ tail -f /var/log/syslog

## 2. File Permissions & Ownership
 chmod 755 <file>

What it does: Sets file permissions to read-write-execute for owner, and read-execute for group/others.

When to use: When making a script executable.

Example:

$ chmod 755 script.sh

 chown <user>:<group> <file>

What it does: Changes file owner and group.

When to use: To transfer file ownership, e.g., when deploying files to another user.

Example:

$ chown ramu:developers file1.txt

 ls -l

What it does: View file permissions and ownership.

 ## 3. Process Management
 ps

What it does: Displays running processes of the current shell.

When to use: To see what your terminal is running.

 ps aux

What it does: Shows detailed information about all running processes.

When to use: To troubleshoot processes or check resource usage.

 top

What it does: Shows real-time resource usage and running processes.

When to use: To monitor CPU, memory, and running processes.

 kill <PID>

What it does: Terminates a process by its process ID (PID).

When to use: To stop a misbehaving process.

Example:

$ kill 1234

 killall <process_name>

What it does: Kills processes by name.

When to use: When you don’t know the PID but know the process name.

 bg

What it does: Resumes a suspended process in the background.

When to use: After pressing Ctrl+Z to suspend a process.

 fg

What it does: Brings a background process to the foreground.

## 4. Disk & Storage
 df -h

What it does: Shows disk space usage in human-readable format.

When to use: To check available space on partitions.

 du -sh <directory>

What it does: Displays total size of a directory.

When to use: To find which directories are consuming space.

 mount

What it does: Lists mounted devices or mounts a filesystem.

When to use: To manually mount USB drives or partitions.

 umount <device>

What it does: Unmounts a mounted device.

When to use: Before safely removing external drives.

## 5. User & Group Management
 whoami

What it does: Prints the current logged-in username.

When to use: To confirm your current user.

 id

What it does: Displays user ID, group ID, and group membership.

 adduser <username>

What it does: Creates a new user account.

When to use: To add a new system user.
 passwd <username>

What it does: Sets or changes a user's password.

 usermod -aG <group> <user>

What it does: Adds a user to a group.

 groupadd <groupname>

What it does: Creates a new user group.

## 6. Networking
 ifconfig

What it does: Displays network interfaces (deprecated, use ip a).

 ip a

What it does: Shows network interfaces and IP addresses.

 ping <host>

What it does: Checks network connectivity to a remote host.

 netstat -tuln

What it does: Lists listening TCP/UDP ports.

 ss -tuln

What it does: Displays listening sockets.

 traceroute <host>

What it does: Traces the network path to a host.

 curl <url>

What it does: Transfers data from or to a URL.

 wget <url>

What it does: Downloads files from the web.

## 7. Package Management (Debian/Ubuntu)
 apt update

What it does: Updates package lists.

When to use: Before installing or upgrading packages.

 apt upgrade

What it does: Upgrades installed packages to the latest version.

 apt install <package>

What it does: Installs a package.

 apt remove <package>

What it does: Removes a package.

 dpkg -l

What it does: Lists installed packages.

## 8. Searching & Text Processing
 grep <pattern> <file>

What it does: Searches for a text pattern in a file.

When to use: To find logs or config entries.

 find <path> -name <filename>

What it does: Searches files by name.

 locate <filename>

What it does: Searches files quickly using a database.

 awk '{print $1}' <file>

What it does: Extracts specific columns from file lines.

 sed 's/old/new/g' <file>

What it does: Replaces all occurrences of old with new.

 sort <file>

What it does: Sorts lines in a file.

 uniq <file>

What it does: Removes duplicate lines (use after sort).

## 9. Archive & Compression
 tar -cvf archive.tar <directory>

What it does: Creates an archive.

 tar -xvf archive.tar

What it does: Extracts an archive.

 tar -czvf archive.tar.gz <directory>

What it does: Creates a compressed archive.

 tar -xzvf archive.tar.gz

What it does: Extracts a compressed archive.

 zip file.zip <file>

What it does: Compresses files into a zip.

 unzip file.zip

What it does: Extracts a zip file.

## 10. System Monitoring
 uptime

What it does: Shows system uptime.

 free -h

What it does: Shows memory usage.

 df -h

What it does: Shows disk space usage.

 dmesg

What it does: Shows kernel logs.

**journalctl**

What it does: Shows system logs (for systemd systems).

## 11. Reboot & Shutdown
 reboot

What it does: Reboots the system.

 shutdown -h now

What it does: Shuts down the system immediately.

 shutdown -r now

What it does: Reboots the system immediately.