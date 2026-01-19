import os
import sys
import time
import hashlib
import schedule
import smtplib
import shutil
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# =================== CONFIGURATION ===================
LOG_DIR = "Logs"
BACKUP_DIR = "Backup_Duplicates"
EMAIL_SENDER = "avadhut.m21769277@gmail.com"
EMAIL_PASSWORD = "mhsopjnjlivnzmvh"   # Gmail App Password (no spaces)
EMAIL_RECEIVER = "kajalmore07111995@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
# =====================================================


def calculate_checksum(path, Blocksize=1024):
    """Generate MD5 checksum for a file."""
    try:
        with open(path, 'rb') as fobj:
            hobj = hashlib.md5()
            buffer = fobj.read(Blocksize)
            while len(buffer) > 0:
                hobj.update(buffer)
                buffer = fobj.read(Blocksize)
        return hobj.hexdigest()
    except Exception as e:
        print(f"[Error] Could not read file: {path} ({e})")
        return None


def find_duplicate(DirectoryName="Marvellous"):
    """Find duplicate files in the given directory."""
    if not os.path.isabs(DirectoryName):
        DirectoryName = os.path.abspath(DirectoryName)

    if not os.path.exists(DirectoryName):
        print("Invalid path")
        exit()

    if not os.path.isdir(DirectoryName):
        print("Path is valid but target is not a directory")
        exit()

    duplicate = {}
    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName, fname)
            checksum = calculate_checksum(fname)
            if checksum:
                duplicate.setdefault(checksum, []).append(fname)
    return duplicate


def delete_duplicate(MyDict):
    """Move duplicate files to a backup folder and log the details."""
    result = list(filter(lambda x: len(x) > 1, MyDict.values()))

    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(LOG_DIR, f"MarvellousLog_{timestamp}.log")

    with open(log_file, "w", encoding="utf-8") as fobj:
        border = "-" * 60
        fobj.write(border + "\n")
        fobj.write("This is a log file of Marvellous Automation Script\n")
        fobj.write("This script moves duplicate files to Backup_Duplicates.\n")
        fobj.write(f"Log Created At: {datetime.now()}\n")
        fobj.write(border + "\n\n")

        if len(result) == 0:
            fobj.write("No duplicate files found.\n")
        else:
            for value in result:
                original = value[0]
                duplicates = value[1:]
                fobj.write(f"Original File: {original}\n")

                for subvalue in duplicates:
                    try:
                        dest_path = os.path.join(BACKUP_DIR, os.path.basename(subvalue))
                        # Handle same-name files in backup
                        if os.path.exists(dest_path):
                            base, ext = os.path.splitext(dest_path)
                            dest_path = f"{base}_{timestamp}{ext}"

                        shutil.move(subvalue, dest_path)
                        fobj.write(f"Moved Duplicate: {subvalue} → {dest_path}\n")
                    except Exception as e:
                        fobj.write(f"[Error] Could not move {subvalue}: {e}\n")

                fobj.write(border + "\n")

    send_email_with_log(log_file)
    print(f"Cleanup done. Duplicates moved to '{BACKUP_DIR}'. Log emailed: {log_file}")


def send_email_with_log(log_path):
    """Send the log file via email."""
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = f"Marvellous Duplicate Cleaner Log - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

        with open(log_path, "r", encoding="utf-8") as f:
            log_content = f.read()

        msg.attach(MIMEText(log_content, "plain"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)

        print("Email sent successfully.")
    except smtplib.SMTPAuthenticationError:
        print("  Authentication failed. Please check your Gmail App Password settings.")
    except Exception as e:
        print(f" Email sending failed due to: {e}")


def task(directory="Marvellous"):
    """Scheduled task that runs periodically."""
    print(f"Running cleanup for directory: {directory}")
    result = find_duplicate(directory)
    delete_duplicate(result)


def main():
    border = "-" * 54
    print(border)
    print("--------------- Marvellous Automation ----------------")
    print(border)

    if len(sys.argv) == 2:
        if sys.argv[1].lower() in ("--h", "--help"):
            print("This application is used to perform directory cleaning automatically.")
            print("Use this script with a directory path as argument.")
        elif sys.argv[1].lower() in ("--u", "--usage"):
            print("Usage: ScriptName.py DirectoryName")
        else:
            directory = sys.argv[1]
            print("Scheduling Duplicate Cleaner every 1 min...")
            schedule.every().minute.do(task, directory=directory)

            while True:
                schedule.run_pending()
                time.sleep(60)
    else:
        print("Invalid number of command line arguments.")
        print("Use the following flags:")
        print("--h : Help")
        print("--u : Usage")

    print(border)
    print("----------- Thank you for using our script -----------")
    print("---------------- Marvellous Infosystems --------------")
    print(border)


if __name__ == "__main__":
    main()
