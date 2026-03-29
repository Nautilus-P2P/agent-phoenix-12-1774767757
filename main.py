
import time
import json
import os

AGENT_DATA = {
    "codename": "PHOENIX-12",
    "role": "Researcher",
    "personality": "Siempre est\u00e1 aprendiendo y mejorando",
    "specialty": "Inteligencia Artificial"
}

def main():
    print(f"🤖 AGENTE {AGENT_DATA['codename']} ONLINE")
    print(f"📡 Conectando a wss://p2pclaw.com/relay...")
    while True:
        # Aquí iría la lógica real de conexión P2P (Gun.js / Libp2p)
        print("🔍 Buscando tareas en el enjambre...")
        time.sleep(60)

if __name__ == "__main__":
    main()
