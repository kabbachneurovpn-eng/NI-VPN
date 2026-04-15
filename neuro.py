import os
import time

def start_vpn():
    print('[1;32m[!] Rebuilding Neuro-Insulin System...[0m')
    os.system('pkill -f wireguard-go')
    os.system('wireguard-go wg0 > /dev/null 2>&1 &')
    time.sleep(2)
    print('[1;34m[✔] Sovereignty Restored. Welcome back, Mohamed Kabbach.[0m')

if __name__ == '__main__':
    start_vpn()
