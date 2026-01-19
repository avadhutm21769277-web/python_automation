

import os
import time
import psutil
import schedule
from datetime import datetime

# =================== CONFIGURATION ===================
DEFAULT_LOG_DIR = "Process_Logs"
DEFAULT_INTERVAL = 1  # in minutes
# =====================================================


def create_log_directory(folder_name):
    """Ensure the log directory exists."""
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return os.path.abspath(folder_name)


def log_system_processes(folder_name=DEFAULT_LOG_DIR):
    """Log all running processes with details."""
    folder_path = create_log_directory(folder_name)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"ProcessLog_{timestamp}.log"
    log_path = os.path.join(folder_path, log_filename)

    with open(log_path, "w", encoding="utf-8") as log_file:
        border = "-" * 70
        log_file.write(border + "\n")
        log_file.write(f"System Process Log - {datetime.now()}\n")
        log_file.write(border + "\n\n")

        log_file.write(f"{'PID':<10}{'Process Name':<25}{'User':<20}{'Memory(MB)':>10}\n")
        log_file.write("-" * 70 + "\n")

        for proc in psutil.process_iter(['pid', 'name', 'username', 'memory_info']):
            try:
                pid = proc.info['pid']
                name = proc.info['name'] or "N/A"
                user = proc.info['username'] or "N/A"
                memory = proc.info['memory_info'].rss / (1024 * 1024)  # Convert bytes to MB
                log_file.write(f"{pid:<10}{name:<25}{user:<20}{memory:>10.2f}\n")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

        log_file.write("\n" + border + "\n")
        log_file.write("End of Process Log\n")
        log_file.write(border + "\n")

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Log created: {log_path}")


def main():
    print("-" * 60)
    print("System Process Logger with Scheduling ")
    print("-" * 60)

    folder_name = input(f"Enter log folder name (default: {DEFAULT_LOG_DIR}): ") or DEFAULT_LOG_DIR
    try:
        interval = int(input(f"Enter interval (in minutes, default: {DEFAULT_INTERVAL}): ") or DEFAULT_INTERVAL)
    except ValueError:
        print("Invalid interval. Using default (1 minute).")
        interval = DEFAULT_INTERVAL

    print(f"\nLogs will be saved in: {os.path.abspath(folder_name)}")
    print(f"Process logging scheduled every {interval} minute(s)\n")

    schedule.every(interval).minutes.do(log_system_processes, folder_name=folder_name)

    # Run scheduler indefinitely
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
