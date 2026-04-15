pkg update -y && pkg upgrade -y && pkg install wireguard-go wireguard-tools python -y && echo -e "\n[✔] ALL DONE: YOUR SYSTEM IS NOW CLEAN & PRO"
# توليد المفاتيح
PK=$(wg genkey); PB=$(echo $PK | wg pubkey)
# إنشاء ملف الإعدادات Neuro-Insulin
echo -e "[Interface]\nPrivateKey = $PK\nAddress = 10.0.0.1/24\nListenPort = 51820\nDNS = 1.1.1.1\n\n[Peer]\nPublicKey = $PB\nAllowedIPs = 0.0.0.0/0\nEndpoint = 127.0.0.1:51820" > neuro_vpn.conf
echo -e "\n[✔] Neuro-Insulin Configuration Created."
import os
def start_neuro_vpn():
if __name__ == "__main__":;     start_neuro_vpn()  cat <<EOF > neuro.py
import os
import time
def start_vpn():
if __name__ == "__main__":;     start_vpn() EOF
python neuro.py
echo "alias run-vpn='python ~/neuro.py'" >> ~/.bashrc
source ~/.bashrc
pkg install python -y
echo -e "import os\nimport time\n\ndef start_vpn():\n    print('\033[1;32m[!] Initializing Neuro-Insulin Engine...\033[0m')\n    os.system('pkill -f wireguard-go')\n    os.system('wireguard-go wg0 > /dev/null 2>&1')\n    time.sleep(2)\n    os.system('wg setconf wg0 ./neuro_vpn.conf')\n    print('\033[1;34m[✔] Digital Sovereignty Active. Welcome, Mohamed Kabbach.\033[0m')\n\nif __name__ == '__main__':\n    start_vpn()" > neuro.py
python neuro.py
pkg install wireguard-tools -y
python neuro.py
# استخراج المفاتيح الحالية وتنظيفها من أي فراغات
PK=$(grep PrivateKey neuro_vpn.conf | cut -d'=' -f2 | tr -d ' ')
PB=$(grep PublicKey neuro_vpn.conf | tail -n1 | cut -d'=' -f2 | tr -d ' ')
# إعادة كتابة الملف بتنسيق wg الصارم
echo -e "[Interface]\nPrivateKey = $PK\nListenPort = 51820\n\n[Peer]\nPublicKey = $PB\nAllowedIPs = 0.0.0.0/0\nEndpoint = 1.1.1.1:51820" > neuro_vpn.conf
echo -e "\n[✔] Configuration Polished."
python neuro.py
PK=$(wg genkey); PB=$(echo $PK | wg pubkey); echo -e "[Interface]\nPrivateKey = $PK\nListenPort = 51820\n\n[Peer]\nPublicKey = $PB\nAllowedIPs = 0.0.0.0/0\nEndpoint = 1.1.1.1:51820" > neuro_vpn.conf && echo -e "\n[✔] ENGINE RE-CALIBRATED WITH NEW KEYS"
python neuro.py
# 1. قتل أي محرك قديم
pkill -f wireguard-go
# 2. تشغيل المحرك مع تحديد مسار المستخدم (وهذا هو السر)
wireguard-go -f neuro-tun &
# فحص الاتصال عبر النفق
curl --interface neuro-tun https://ifconfig.me
curl -L https://github.com/kabbach-mohamed/bins/raw/main/wireguard-go -o ./wireguard-go && chmod +x ./wireguard-go && echo -e "\n[✔] ENGINE DOWNLOADED LOCALLY"
./wireguard-go -f neuro-tun &
echo -e "import os\nimport time\n\ndef start_vpn():\n    print('\033[1;32m[!] Launching Neuro-Insulin Local Engine...\033[0m')\n    os.system('pkill -f wireguard-go')\n    # التشغيل من المجلد الحالي\n    os.system('./wireguard-go neuro-tun > /dev/null 2>&1 &')\n    time.sleep(2)\n    print('\033[1;34m[✔] Digital Sovereignty Active. Welcome, Mohamed Kabbach.\033[0m')\n\nif __name__ == '__main__':\n    start_vpn()" > neuro.py
rm ./wireguard-go && pkg clean
termux-change-repo
pkg update -y && pkg install wireguard-go -y
echo -e "import os\nimport time\n\ndef start_vpn():\n    print('\033[1;32m[!] Launching Neuro-Insulin VPN...\033[0m')\n    os.system('pkill -f wireguard-go')\n    # تشغيل المحرك الرسمي\n    os.system('wireguard-go wg0 > /dev/null 2>&1 &')\n    time.sleep(2)\n    print('\033[1;34m[✔] System Operational. Welcome Back, Mohamed Kabbach.\033[0m')\n\nif __name__ == '__main__':\n    start_vpn()" > neuro.py
ls
echo -e "import os\nimport time\n\ndef start_vpn():\n    print('\033[1;32m[!] Launching Neuro-Insulin VPN...\033[0m')\n    os.system('pkill -f wireguard-go')\n    # تشغيل المحرك الرسمي\n    os.system('wireguard-go wg0 > /dev/null 2>&1 &')\n    time.sleep(2)\n    print('\033[1;34m[✔] System Operational. Welcome Back, Mohamed Kabbach.\033[0m')\n\nif __name__ == '__main__':\n    start_vpn()" > neuro.py
pkg install wireguard-go -y || (apt-get update && apt-get install wireguard-go -y)
echo "deb https://grimler.se/termux-packages-24 stable main" > $PREFIX/etc/apt/sources.list && pkg update -y
pkg install wireguard-go -y
exit
