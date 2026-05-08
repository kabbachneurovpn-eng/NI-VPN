import time
import os

def get_network_bytes():
    # قراءة إحصائيات الشبكة من ملفات النظام مباشرة
    with open("/proc/net/dev", "r") as f:
        lines = f.readlines()
    
    total_bytes = 0
    for line in lines:
        if "wlan0" in line or "rmnet" in line: # واجهة الواي فاي أو بيانات الهاتف
            parts = line.split()
            # العمود الثاني هو المستلم (Receive) والتاسع هو المرسل (Transmit)
            total_bytes += int(parts[1]) + int(parts[9])
    return total_bytes

def start_monitor():
    print("\033[92m[!] Neuro-Insulin Kernel Monitor: ACTIVE\033[0m")
    last_bytes = get_network_bytes()
    
    try:
        while True:
            time.sleep(1)
            current_bytes = get_network_bytes()
            diff = current_bytes - last_bytes
            
            # التحويل إلى كيلوبايت
            kb_speed = diff / 1024
            
            os.system('clear')
            print(f"--- NEURO-INSULIN SYSTEM [V1.0] ---")
            print(f"Interface: Active Network Nodes")
            print(f"Real-time Flow: {kb_speed:.2f} KB/s")
            
            if kb_speed > 100:
                print("\033[91m[!] STATUS: Focus Under Pressure\033[0m")
            else:
                print("\033[94m[!] STATUS: Sovereignty Maintained\033[0m")
                
            last_bytes = current_bytes
    except KeyboardInterrupt:
        print("\n[!] Monitor Paused.")

if __name__ == "__main__":
    start_monitor()

