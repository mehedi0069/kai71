import time
import requests

url = "https://siyamahmmed.shop/jimkarr.php"

while True:
    try:
        response = requests.get(url, timeout=10)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [jimkar bot] {url} → {response.status_code}")
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] [jimkar bot] Error: {e}")
    time.sleep(3)
