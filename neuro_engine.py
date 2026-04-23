import sys
import time

def start_dose(duration):
    print("\033[1;32m[SYSTEM] Initializing Digital Insulin...\033[0m")
    time.sleep(1)
    print(f"\033[1;36m[DOSE] Focus Dose Active: {duration} Minutes\033[0m")
    print("\033[1;31m[FIREWALL] Distractions Blocked.\033[0m")
    # هنا يتم استدعاء أوامر الحظر الحقيقية لاحقاً

if __name__ == "__main__":
    if len(sys.argv) > 1:
        start_dose(sys.argv[1])
    else:
        print("Usage: python neuro_engine.py <minutes>")

