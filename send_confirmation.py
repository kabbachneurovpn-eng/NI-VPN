import datetime
import time
import random

# 1. دالة فحص الاتصال 🎲
def check_vpn_status():
    print("🔍 Checking VPN connection...")
    time.sleep(1.5)
    return random.choice([True, False])

# 2. تشغيل الفحص والحصول على الوقت 🕒
is_connected = check_vpn_status()
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 3. تحديد الحالة والرسالة
if is_connected:
    status_text = "ONLINE"
    log_message = f"[{current_time}] ✅ Status: {status_text} - Confirmation Sent.\n"
else:
    status_text = "OFFLINE"
    log_message = f"[{current_time}] ❌ Status: {status_text} - Connection Failed.\n"

# 4. حفظ النتيجة في ملف سجل (Log File) 📁
with open("system_logs.txt", "a") as log_file:
    log_file.write(log_message)

# 5. عرض النتيجة على الشاشة 🖥️
print("----------------------------------------")
print("   Neuro-Insuline VPN Security System   ")
print("----------------------------------------")
print(f"Status: {status_text}")
print("Log saved to: system_logs.txt")
print("----------------------------------------")

