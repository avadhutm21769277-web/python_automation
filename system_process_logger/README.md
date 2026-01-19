####################		 System Process Logger with Scheduling		###############################################



A lightweight Python tool that automatically logs all running system processes — including PID, process name, user, and memory usage — at regular intervals.  
Each log is saved in a timestamped file for easy tracking and analysis.

###############################################################################################################################


## Features

- Logs **all active system processes** with detailed info:
  - Process ID (PID)
  - Process name
  - User/owner
  - Memory usage (in MB)
- **Automatic scheduling** at user-defined intervals (default: 1 minute)
- **Timestamped log files** stored in a configurable directory
- Handles inaccessible or zombie processes gracefully
- Simple console interface — no setup required

#################################################################################

###### Log Output Example

```
----------------------------------------------------------------------
System Process Log - 2025-11-06 15:42:01
----------------------------------------------------------------------

PID       Process Name            User                Memory(MB)
----------------------------------------------------------------------
1234      chrome.exe              user1                 210.45
5678      python.exe              user2                  50.23
...
----------------------------------------------------------------------
End of Process Log
----------------------------------------------------------------------
```

###################################################################################



#################################################################################

 Installation


1. **Install dependencies:**
   ```bash
   pip install psutil schedule
   ```

2. **Run the script:**
   ```bash
   python process_logger.py
   ```



############################################################################################

When you run the script, you’ll be prompted to enter:

1. **Log folder name** (default: `Process_Logs`)
2. **Interval (in minutes)** (default: `1`)

Example:
```
Enter log folder name (default: Process_Logs):
Enter interval (in minutes, default: 1): 5
```

Output:
```
Logs will be saved in: /path/to/Process_Logs
Process logging scheduled every 5 minute(s)

[15:42:01] Log created: /path/to/Process_Logs/ProcessLog_20251106_154201.log
```

The logger will continue running indefinitely until stopped manually (`Ctrl + C`).

---

##  Optional Improvements

If you’d like to enhance functionality, consider adding:
- **Graceful shutdown** on `Ctrl + C`
- **Log rotation** (auto-delete oldest logs)
- **CSV export** for easier data analysis

#########################################################################################

## Requirements

- **Python:** 3.7 or newer  
- **Libraries:**
  - [`psutil`](https://pypi.org/project/psutil/)
  - [`schedule`](https://pypi.org/project/schedule/)

Install all at once:
```bash
pip install -r requirements.txt
```

*(Create a `requirements.txt` with: `psutil` and `schedule`)*

---

##### Stopping the Logger

To safely stop the logger, press:
```
Ctrl + C
```
You’ll see:
```
Logging stopped by user. Exiting gracefully.
```

---

####################################################################################

---

## Author

Avadhut Yashwant Mote

########################################################################3########### 

