import requests
import time

# بيانات السيادة الرقمية
TOKEN = 'تـوكن_غومرود_الجديد_هنا'
BASE_URL = "https://api.gumroad.com/v2/products"

def welcome_banner():
    print("\033[1;32m" + "="*45)
    print("      NEURO-INSULIN VPN: MASTER CONTROL")
    print("      المقر الرئيسي: كازابلانكا، المغرب")
    print("="*45 + "\033[0m")

def get_market_status():
    params = {'access_token': TOKEN}
    try:
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            products = response.json().get('products', [])
            for p in products:
                price = p['price'] / 100
                print(f"📦 المنتج: {p['name']}")
                print(f"💰 السعر: {price} {p['currency']}")
                print(f"📈 المبيعات: {p['sales_count']}")
                print(f"🔗 الرابط: {p['short_url']}")
                print("-" * 30)
        else:
            print(f"⚠️ تنبيه: فشل الاتصال (كود {response.status_code})")
    except Exception as e:
        print(f"❌ خطأ تقني: {e}")

if __name__ == "__main__":
    welcome_banner()
    print("جاري فحص حالة السوق الرقمي...")
    time.sleep(1)
    get_market_status()
