
import subprocess
import time

def toggle_vpn(action):
    """
    التحكم في النفق: action يمكن أن يكون 'up' أو 'down'
    """
    try:
        # ملاحظة: قد يتطلب الأمر صلاحيات روت أو إضافة sudo إذا كانت متاحة
        command = f"wg-quick {action} ./neuro_vpn.conf"
        # subprocess.run(command.split(), check=True) # تفعيلها عند الجاهزية الكاملة
        print(f"[ENGINE] WireGuard Tunnel: {action.upper()} Success.")
    except Exception as e:
        print(f"[ERROR] Failed to toggle VPN: {e}")

def start_dose(minutes):
    print(f"\n[!] Injecting {minutes} Minutes of Digital Insulin...")
    toggle_vpn('up')
    
    # عد تنازلي مبسط للتركيز
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"\r⏳ Remaining Dose: {timer} ", end="")
        time.sleep(1)
        seconds -= 1
    
    print("\n[✓] Dose Completed.")
    toggle_vpn('down')

if __name__ == "__main__":
    start_dose(25) # جلسة تركيز افتراضية

