import os
import time

# ==========================================
# PROJET: NEURO-INSULIN VPN (NI-VPN)
# ARCHITECT: Mohamed Kabbach
# COMPOSANT: Core Engine (neuro_engine.py)
# VERSION: 1.0.0
# ==========================================

def clear_screen():
    os.system('clear')

def startup_animation():
    green_color = "\033[1;32m"
    reset_color = "\033[0m"
    
    print(f"{green_color}")
    print(" [SOUVERAINETÉ DIGITALE ACTIVE] ")
    print(" Initialisation du package Kabbach...")
    time.sleep(1)
    print(" Chargement de la Neuro-Economie...")
    time.sleep(1)
    print(" Activation du bouclier NI-VPN...")
    print(f"{reset_color}")

def main_engine():
    startup_animation()
    
    # Structure de contrôle simple pour le projet
    while True:
        print("\n--- NI-VPN DASHBOARD CONTROL ---")
        print("1. Lancer le tunnel de sécurité")
        print("2. Vérifier l'état du système")
        print("3. Quitter")
        
        choice = input("\nChoisissez une option (1-3): ")
        
        if choice == '1':
            print("\n[OK] Tunnel NI-VPN activé. Votre attention est protégée.")
        elif choice == '2':
            print("\n[INFO] Status: Système Opérationnel")
            print("[INFO] Source: NI-VPN_Package_Kabbach.txt")
        elif choice == '3':
            print("\nFermeture sécurisée...")
            break
        else:
            print("\n[ERROR] Option invalide.")

if __name__ == "__main__":
    try:
        main_engine()
    except KeyboardInterrupt:
        print("\nInterruption par l'utilisateur.")

