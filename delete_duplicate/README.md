#######################		 Duplicate File Cleaner & Log Automation		####################################



A Python-based automation script that **detects and removes duplicate files** safely from a given directory.  
Duplicates are **moved to a backup folder** instead of being deleted permanently.  
The system also **generates detailed log files** and **emails them automatically** for audit purposes.

##############################################################################################################################

#####################	 Features	>>>>>>


- **Checksum-based duplicate detection** using MD5 (via `hashlib`)
- **Automatic logging** with timestamps (`Logs/` folder)
- **Safe cleanup** — duplicates are **moved** to `Backup_Duplicates/`
- **Email automation** using `smtplib` (sends logs via Gmail)
- **Scheduled execution** every minute (via `schedule` library)
- **Cross-platform support** (Windows, Linux, macOS)

##########################################################################

##########	 Requirements	>>>>

Install the required Python libraries:

```bash
pip install schedule
```

> All other modules (`os`, `hashlib`, `smtplib`, `shutil`, etc.) are part of Python’s standard library.

###########################################

#######	Configuration	>>>

Open the Python script and update the following section with your details:

```python
EMAIL_SENDER = "youremail@gmail.com"
EMAIL_PASSWORD = "your-app-password"  # Use Gmail App Password (not normal password)
EMAIL_RECEIVER = "receiver@example.com"
```

#####################################################

#####	Gmail App Password Setup	>>>>>>

1. Go to [https://myaccount.google.com/security](https://myaccount.google.com/security)
2. Turn ON **2-Step Verification**
3. Visit [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
4. Create an **App Password** for "Mail" → "Other (Custom name)" = `Python Script`
5. Copy the 16-character password and paste it in `EMAIL_PASSWORD` (without spaces)

#########################################################


#######	 How to Run	>>>>

### **Command Syntax**
```bash
python duplicate_cleaner_log_email_automation.py <DirectoryPath>
```

### **Example**
```bash
python duplicate_cleaner_log_email_automation.py ganesh
```

### **Help / Usage**
```bash
python duplicate_cleaner_log_email_automation.py --h
python duplicate_cleaner_log_email_automation.py --u
```

###############################################################

#####	 What Happens	>>>>>

Every 1 minute, the script:
1. Scans the given directory for duplicate files  
2. Moves duplicates to `/Backup_Duplicates/`  
3. Creates a detailed log in `/Logs/`  
4. Emails the log file automatically  

################################################################

######	 Folder Structure	>>>>>>>>>>>

```
project/
│
├── duplicate_cleaner_log_email_automation.py
├── Logs/
│   └── MarvellousLog_YYYYMMDD_HHMMSS.log
├── Backup_Duplicates/
│   └── (duplicate files moved here)
└── README.md
```

#####################################################################


######	 Example Log Output	>>>>>

```
------------------------------------------------------------
This is a log file of Marvellous Automation Script
This script moves duplicate files to Backup_Duplicates.
Log Created At: 2025-11-04 12:45:12
------------------------------------------------------------

Original File: ganesh\data1.txt
Moved Duplicate: ganesh\data_copy.txt → Backup_Duplicates\data_copy.txt

Original File: ganesh\notes.txt
No duplicate found.

------------------------------------------------------------
```

######################################################################################

#####	 Notes	>>>>

- The script keeps **only one original copy** and moves all other identical copies.
- Files with **same name but different data** are **not affected**.
- All moved duplicates remain in `Backup_Duplicates/` — nothing is permanently deleted.
- The script runs indefinitely until manually stopped (`Ctrl + C`).

###################################################################################

## Developed By

**Avadhut Yashwant Mote.**  
 Python Automation Project  
📧 Email: [avadhut.m21769277@gmail.com](mailto:avadhut.m21769277@gmail.com)

#######################################################################################
