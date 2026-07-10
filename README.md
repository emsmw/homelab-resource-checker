# Homelab Resource Checker

A modular Python command-line utility designed to monitor server hardware utilization (CPU, memory, and disk percentages) in real time. 

## Features

* **Real-Time Monitoring:** Tracks core system resource metrics dynamically using `psutil`.
* **Modular Architecture:** Cleanly split into individual monitoring modules for simple extensibility.
* **System-Wide CLI Command:** Accessible from anywhere on the server via a custom `resource-check` terminal shortcut.
* **Isolated Environment:** Runs safely within its own Python virtual environment (`.venv`) to ensure system dependency stability.

## Project Structure

```text
homelab-cpu-disk-mem-usage-alerts/
├── config_secret.py     # Sensitive configurations/credentials
├── main.py              # Main execution script
├── requirements.txt     # Python dependencies
├── .gitignore          # Git exclusion rules
├── monitors/            # Modular hardware monitoring scripts
└── .venv/               # Isolated virtual environment
