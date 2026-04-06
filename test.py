import requests
import time
from datetime import datetime
from zoneinfo import ZoneInfo

TOKEN = "8581090817:AAFC1bzXTfJvqHHxFmPzfXECciSjrErbyjM"
CHAT_USERNAME = "@asdqwesszx"
MESSAGE = "ТЕСТ 22:00"
PHOTO_PATH = "photo.png"

def send_message():
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    with open(PHOTO_PATH, "rb") as photo_file:
        payload = {
            "chat_id": CHAT_USERNAME,
            "caption": MESSAGE
        }
        files = {"photo": photo_file}
        r = requests.post(url, data=payload, files=files)
        print("Send status:", r.status_code, r.text)

def wait_and_send():
    sent = False

    while True:
        now = datetime.now(ZoneInfo("Europe/Copenhagen"))

        target = now.replace(
            hour=22,
            minute=0,
            second=0,
            microsecond=0
        )

        if not sent and target <= now < target.replace(minute=1):
            send_message()
            sent = True
            break

        time.sleep(10)

if __name__ == "__main__":
    print("Тестовий бот, очікуємо 22:00 Данія...")
    wait_and_send()