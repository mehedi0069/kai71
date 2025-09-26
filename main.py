import time
import requests
import threading

# === Function to repeatedly call a URL ===
def run_bot(name, url, delay):
    while True:
        try:
            response = requests.get(url, timeout=10)
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [{name}] {url} → {response.status_code}")
        except Exception as e:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [{name}] Error: {e}")
        time.sleep(delay)

# === Define bots with their own delays ===
bots = [
    ("jimkar bot", "https://siyamahmmed.shop/jimkarr.php", 3),
    ("talhannc bot", "https://zihadbd.shop/talhannc.php", 2),
    ("clientbot21", "https://zihadbd.shop/clientbot21.php", 3),
]

# === Start each bot in a separate thread ===
for name, url, delay in bots:
    t = threading.Thread(target=run_bot, args=(name, url, delay), daemon=True)
    t.start()

# Keep main thread alive
while True:
    time.sleep(1)
