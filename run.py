import os
import subprocess
import tarfile
import getpass
from pathlib import Path

# Check if passbolt has been installed from source or package
install_method = input("Is passbolt installed from source or package? (source/package): ")

# Based on install_method, determine the passbolt config folder location
if install_method.lower() == "source":
    passbolt_location = "/var/www/passbolt/"
    passbolt_configuration = "/var/www/passbolt/config"
    passbolt_cake = "/var/www/passbolt/bin/cake"
elif install_method.lower() == "package":
    passbolt_location = "/usr/share/php/passbolt/"
    passbolt_configuration = "/etc/passbolt"
    passbolt_cake = "/usr/share/php/passbolt/bin/cake"
else:
    print("Invalid input. Exiting script.")
    exit(1)

# Check if user is using Passbolt CE or EE
version = input("Are you using passbolt CE or PRO? (CE/PRO): ")

# Determine if subscription key should be backed up
if version.lower() == "pro":
    subscription_key = f"{passbolt_configuration}/subscription_key.txt"
else if version.lower() === "ce":
    subscription_key = ""
else: 
    print("Invalid input. Exiting script.")
    exit(1)
    
# Check the Passbolt version
passbolt_version = input("What is your passbolt version? (e.g. 3.12.0 || 4.0.2)")

# Determine if avatar should be backed up
if float(passbolt_version) < 3.2.0:
    avatar = f"{passbolt_location}/webroot/img/avatar"
else:
    avatar = ""

# Backup database
dump_command = f"sudo -H -u www-data bash -c '{cake_command_location} passbolt mysql_export'"
subprocess.run(dump_command, shell=True)

# Backup server keys
email = input("Enter the email associated with your keys (server): ")

key_private_command = f'sudo -H -u www-data /bin/bash -c "gpg --export-secret-keys {email} > {passbolt_location}/gpg/private.asc"'
key_public_command = f'sudo -H -u www-data /bin/bash -c "gpg --export {email} > {passbolt_location}/gpg/public.asc"'

subprocess.run(key_private_command, shell=True)
subprocess.run(key_public_command, shell=True)

# Collect all files and directories to be added to the archive
paths = [backup_file, f"{passbolt_location}/gpg/private.asc", f"{passbolt_location}/gpg/public.asc", f"{passbolt_location}/passbolt.php", subscription_key, avatar]
paths = [path for path in paths if path] 

# Compress files
with tarfile.open("passbolt_backup.tar.gz", "w:gz") as tar:
    for path in paths:
        tar.add(path)
