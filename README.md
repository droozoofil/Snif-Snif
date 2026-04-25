# 🔍 Python Port Scanner (GUI + CLI)

## 📌 Overview
A lightweight Python-based port scanner capable of scanning both single hosts and entire networks.  
Includes a graphical user interface (GUI) for ease of use.

## 🚀 Features
- Scan a single IP address
- Scan a network range (CIDR notation)
- Detect open TCP ports
- Multi-threaded scanning
- Simple GUI using Tkinter

## 🧰 Technologies Used
- Python
- socket (network connections)
- threading (performance)
- ipaddress (network parsing)
- tkinter (GUI)

## 📦 How It Works
The scanner attempts to establish a TCP connection to each target port:
- If the connection succeeds → port is **open**
- If it fails → port is **closed or filtered**

## ▶️ Usage

### Run the program:
```bash
python scanner_gui.py
