import os
import time
import random

def send_alert(message):
    # محاولة إرسال تنبيه للنظام (إذا كان Termux-API مثبتاً)
    os.system(f"termux-notification -c '{message}' --title 'Neuro-Guard Alert'")
    print(f"\033[1;35m[!] تنبيه مرسل: {message}\033[0m")

def neuro_guard():
    print("\033[1;32m[!] تم تفعيل بروتوكول السيادة... الحارس مستيقظ.\033[0m")
    
    saj_wisdom = [
        "يا من تطلب الرقمية.. صُن حدودك النفسية.",
        "التركيز أساس البناء.. والتشتت داء الضعفاء.",
        "سيادتك في انضباطك.. وفلاحك في حفاظك على أوقاتك.",
        "العين بصيرة.. والهمة كبيرة.. والوجهة واضحة مستنيرة."
    ]
    
    try:
        while True:
            # محاكاة فحص أمني للتركيز
            print("\033[0;36m[#] جارٍ مسح النطاق الرقمي... لا خروقات مسجلة.\033[0m")
            
            # اختيار حكمة عشوائية
            current_wisdom = random.choice(saj_wisdom)
            print(f"\033[1;32m>>> {current_wisdom}\033[0m")
            
            # إرسال التنبيه
            send_alert(current_wisdom)
            
            # الانتظار (يمكنك تقليل الوقت للتجربة، مثلاً 30 ثانية)
            time.sleep(300) 
            
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] تم تعليق البروتوكول... عد سريعاً لعرين السيادة.\033[0m")

if __name__ == "__main__":
    neuro_guard()
