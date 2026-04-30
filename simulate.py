import sqlite3
import time
import random

def run_simulation():
    # Connect to the same database as Flask
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    can_ids = ['0x1A0', '0x2B5', '0x30C', '0x4F1', '0x081']
    detectors = ['Interval', 'Frequency', 'Payload']
    
    print("🚀 LIDS Simulator Started...")
    print("Press Ctrl+C to terminate.")

    try:
        while True:
            # Pick a random CAN ID
            cid = random.choice(can_ids)
            
            # Determine if this iteration is an attack (25% chance)
            is_attack = random.random() < 0.25
            
            if is_attack:
                # Randomly pick which detector "caught" it for the demo
                # These strings MUST match the keys in dashboard.html and app.py
                attack_type = random.choice(detectors)
                
                cursor.execute('''
                    INSERT INTO alerts (can_id, alert_type, data_summary, is_anomaly)
                    VALUES (?, ?, ?, ?)
                ''', (cid, attack_type, f"Malicious {attack_type} pattern detected", True))
                
                print(f"🚨 ALERT: {attack_type} Anomaly on {cid}")
            else:
                # Normal benign traffic
                cursor.execute('''
                    INSERT INTO alerts (can_id, alert_type, data_summary, is_anomaly)
                    VALUES (?, ?, ?, ?)
                ''', (cid, 'None', 'Normal Traffic', False))
                
                print(f"✅ OK: {cid} - Standard Frame")

            # Commit changes to DB so the Flask API sees them
            conn.commit()
            
            # Wait between 0.5 to 1.5 seconds to simulate real bus traffic timing
            time.sleep(random.uniform(0.5, 1.5))

    except KeyboardInterrupt:
        print("\n🛑 Simulation stopped by user.")
    finally:
        conn.close()

if __name__ == "__main__":
    run_simulation()