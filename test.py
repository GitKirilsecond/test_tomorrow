import requests
import datetime
import time

TOKEN = "8581090817:AAFC1bzXTfJvqHHxFmPzfXECciSjrErbyjM"
CHAT_USERNAME = "@asdqwesszx"
MESSAGE = "TEST Зупинімося на мить, щоб вшанувати пам’ять Героїв, які поклали своє життя заради нашого майбутнього. Їхній подвиг назавжди залишиться в нашій пам’яті. \n\nВічна Слава і вдячність."
PHOTO_PATH = "photo.png"  # твій файл фото

TARGET_HOUR = 5  
TARGET_MINUTE = 0

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

def wait_until_target():
    while True:
        now = datetime.datetime.now()
        target = now.replace(
            hour=TARGET_HOUR,
            minute=TARGET_MINUTE,
            second=0,
            microsecond=0
        )

        if now >= target:
            send_message()
            break

        time.sleep(5)  # перевірка кожні 5 секунд

if __name__ == "__main__":
    print("Бот запущений, очікуємо до 9:00...")
    wait_until_target()
