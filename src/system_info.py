import logging
import platform
import os
import subprocess
from datetime import datetime

def setup_logging():
    logging.basicConfig(
        filename="logs/system-monitor.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
def get_system_info():
    logging.info("Collecting system information")
    print("===== SYSTEM INFORMATION =====")
    print(f"Date and Time: {datetime.now()}")
    print(f"Operating System: {platform.system()}")
    print(f"OS Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"CPU Cores: {os.cpu_count()}")


def get_disk_info():
    logging.info("Collecting disk information")
    try:
        result = subprocess.run(        
            ["df", "-h", "/"],
            capture_output=True,
            text=True,
            check=True
        )
        print("\n===== DISK INFORMATION =====")
        print(result.stdout)
        usage = subprocess.run(
            ["df", "-h", "/"],
            capture_output=True,
            text=True,
            check=True
        )

        capacity = usage.stdout.splitlines()[1].split()[4]
        usage_percent = int(capacity.rstrip("%"))

        if usage_percent >= 80:
            print("WARNING: Disk usage is critically high!")
        else:
            print("Disk usage is within safe limits.")

    except subprocess.CalledProcessError as error:
        print(f"Disk information error: {error}")
        logging.error("Disk information failed: %s", error)
def get_memory_info():
    logging.info("Collecting memory information")
    try:
        result = subprocess.run(
            ["vm_stat"],
            capture_output=True,
            text=True,
            check=True
        )

        page_size = 16384
        memory_stats = {}

        for line in result.stdout.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                value = value.strip().rstrip(".").replace(",", "")

                if value.isdigit():
                    memory_stats[key.strip()] = int(value)

        free_pages = memory_stats.get("Pages free", 0)
        active_pages = memory_stats.get("Pages active", 0)
        inactive_pages = memory_stats.get("Pages inactive", 0)
        wired_pages = memory_stats.get("Pages wired down", 0)

        free_mb = free_pages * page_size / (1024 ** 2)
        active_mb = active_pages * page_size / (1024 ** 2)
        inactive_mb = inactive_pages * page_size / (1024 ** 2)
        wired_mb = wired_pages * page_size / (1024 ** 2)

        print("\n===== MEMORY INFORMATION =====")
        print(f"Free Memory: {free_mb:.2f} MB")
        print(f"Active Memory: {active_mb:.2f} MB")
        print(f"Inactive Memory: {inactive_mb:.2f} MB")
        print(f"Wired Memory: {wired_mb:.2f} MB")

    except FileNotFoundError:
        print("Memory utility vm_stat not found.")

    except subprocess.CalledProcessError as error:
        print(f"Memory information error: {error}")   
        logging.error("Disk information failed: %s", error)
if __name__ == "__main__":
    setup_logging()
    logging.info("System monitoring completed")
    get_system_info()
    get_disk_info()
    get_memory_info()
    logging.info("System monitoring completed")
