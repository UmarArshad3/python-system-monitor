

def analyze_logs():
    log_file = "logs/system-monitor.log"

    counts = {
        "INFO": 0,
        "ERROR": 0,
        "WARNING": 0
    }

    try:
        with open(log_file, "r") as file:
            for line in file:
                if "INFO" in line:
                    counts["INFO"] += 1
                elif "ERROR" in line:
                    counts["ERROR"] += 1
                elif "WARNING" in line:   
                    counts["WARNING"] +=1
                    total_messages = sum(counts.values())
        total_messages = sum(counts.values())
        print("===== LOG ANALYSIS =====")
        print(f"INFO messages: {counts['INFO']}")
        print(f"ERROR messages: {counts['ERROR']}")
        print(f"WARNING messages: {counts['WARNING']}")
        print(f"Total log messages: {total_messages}")
    except FileNotFoundError:
        print("Log file not found.")

if __name__ == "__main__":
    analyze_logs()
