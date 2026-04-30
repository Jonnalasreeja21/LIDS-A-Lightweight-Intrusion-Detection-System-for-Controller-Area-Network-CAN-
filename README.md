# LIDS-A-Lightweight-Intrusion-Detection-System-for-Controller-Area-Network-CAN-
project detects cyberattacks in vehicle networks using a lightweight system based on timing, frequency, and payload analysis

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
├── app.py # Main application
├── init_db.py # Database initialization
├── simulate.py # CAN traffic simulation
├── schema.sql # Database schema
├── database.db # SQLite database
├── requirements.txt # Dependencies
└── README.md # Project documentation


## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/LIDS-A-Lightweight-Intrusion-Detection-System-for-Controller-Area-Network-CAN-.git
   cd LIDS-A-Lightweight-Intrusion-Detection-System-for-Controller-Area-Network-CAN-

2.Install dependencies:
  pip install -r requirements.txt
3.Initialize the database:
  python init_db.py
4.Run the application:
  python app.py
5.(Optional) Simulate CAN traffic:
    python simulate.py
 Features
Lightweight and efficient detection system
Real-time monitoring
Attack logging and analysis
Easy to deploy and extend
 Future Enhancements
Machine learning-based detection
Real-time dashboard visualization
Integration with real CAN hardware
