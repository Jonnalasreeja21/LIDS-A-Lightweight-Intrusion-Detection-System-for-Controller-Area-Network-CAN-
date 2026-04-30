# LIDS-A-Lightweight-Intrusion-Detection-System-for-Controller-Area-Network-CAN-
project detects cyberattacks in vehicle networks using a lightweight system based on timing, frequency, and payload analysis.
# LIDS: A Lightweight Intrusion Detection System for Controller Area Network (CAN)

## 📌 Overview
LIDS (Lightweight Intrusion Detection System) is a cybersecurity project designed to detect cyberattacks in vehicle Controller Area Network (CAN) systems.  
It uses lightweight techniques such as **timing analysis, frequency monitoring, and payload inspection** to identify abnormal behavior in CAN messages.

## 🚗 Problem Statement
Modern vehicles rely on CAN protocols for communication between ECUs (Electronic Control Units). However, CAN lacks built-in security, making it vulnerable to attacks like:
- Denial of Service (DoS)
- Message Injection
- Replay Attacks

## 💡 Solution
This project implements a lightweight IDS that:
- Monitors CAN traffic
- Detects anomalies based on timing and frequency
- Analyzes payload data for suspicious patterns
- Logs detected intrusions for further analysis

## 🛠️ Technologies Used
- Python
- SQLite (database.db)
- Flask (for web interface)
- CAN simulation scripts

## 📂 Project Structure
