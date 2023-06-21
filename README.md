# Backup script

This Python script provides a systematic method for backing up a Passbolt password manager installation. It was designed with the goal of consolidating several backup tasks into one convenient script, which can be run as needed to create a comprehensive backup.

## Disclaimer
Please note that this script is a user-created tool and is not officially affiliated with, maintained, authorized, endorsed, or sponsored by [Passbolt](https://github.com/passbolt/). The script is provided "as-is", without any guarantees or liability. Use of the script is at your own risk. The author is not responsible for any damage or data loss that may occur from using this script.

## Script Features
- User-guided interaction to customize the backup process based on the specifics of your Passbolt installation.
- Support for both From Source and Package installations of Passbolt.
- Automated backup of your Passbolt database using Passbolt's built-in command.
- Automated backup of the server's public and private OpenPGP keys.
- Automated backup of the Passbolt application configuration file (passbolt.php).
- Optional backup of the Passbolt subscription key for EE users.
- Optional backup of user avatars for Passbolt versions less than 3.12.
- Consolidation of all backup files into a single compressed .tar.gz file for easy storage and retrieval.

## Usage
Before running the script, please make sure you have the necessary permissions for executing the script and accessing the files and directories involved in the backup process.

To run the script, navigate to the directory containing the script and use the following command:

```bash
python3 passbolt_backup.py
``` 

## Expectation
Upon successful execution, the script will create a .tar.gz file named passbolt_backup.tar.gz in the same directory as the script. This file contains all the backup files, which you can then move to your preferred storage location.

Please ensure that you store your backups in a safe and secure location, as they contain sensitive data.

**WARNING:** This script does not include robust error handling. In a production environment, you should modify this script to include appropriate error checking and exception handling