# Python System Monitor

A Python-based system monitoring and log analysis project. This learning project demonstrates Python fundamentals, system administration, file handling, exception handling, and logging.

## Features

### System Monitor (`src/system_info.py`)
- Displays the current date and time.
- Reports operating system, version, processor, machine architecture, and CPU cores.
- Checks root filesystem usage.
- Displays a warning when disk usage reaches 80% or above.
- Collects macOS memory statistics using `vm_stat`.
- Records monitoring events in a log file.

### Log Analyzer (`src/log_analyzer.py`)
- Reads the system monitor log file.
- Counts INFO, ERROR, and WARNING messages.
- Calculates the total number of log messages.
- Handles a missing log file.

## Requirements

- Python 3
- macOS for the current memory-reporting implementation (`vm_stat`)
- Standard Python libraries; no external packages required.

## Project structure

```text
python-system-monitor/
├── src/
│   ├── system_info.py
│   └── log_analyzer.py
├── logs/
├── README.md
└── .gitignore
```

## Setup

Clone the repository and enter the project directory:

```bash
git clone <your-repository-url>
cd python-system-monitor
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

## Run the System Monitor

```bash
python src/system_info.py
```

The script displays system information and appends monitoring events to:

```text
logs/system-monitor.log
```

## Run the Log Analyzer

```bash
python src/log_analyzer.py
```

The analyzer reads `logs/system-monitor.log` and displays the number of INFO, ERROR, and WARNING messages, along with the total.

Run the system monitor at least once before running the analyzer.

## Verify Python syntax

```bash
python -m py_compile src/system_info.py src/log_analyzer.py
```

## Python concepts demonstrated

- Variables and data types
- Conditional statements
- Loops
- Functions
- Lists and dictionaries
- File handling
- Exception handling
- Virtual environments
- Logging
- Subprocess execution

## Limitations

- Memory reporting currently uses macOS `vm_stat` and is not yet implemented for Linux.
- The disk warning threshold is fixed at 80%.
- The project reports system health but does not automatically change system settings or restart services.
- Log analysis counts messages by their severity labels; it does not perform advanced log parsing.

## Project purpose

This project was built to practise Python fundamentals and basic system administration through practical monitoring and log analysis utilities.
