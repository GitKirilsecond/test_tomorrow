import requests
from datetime import datetime
from zoneinfo import ZoneInfo

TOKEN = "8581090817:AAFC1bzXTfJvqHHxFmPzfXECciSjrErbyjM"
CHAT_USERNAME = "@asdqwesszx"
MESSAGE = "Зупинімося на мить, щоб вшанувати пам’ять Героїв, які поклали своє життя заради нашого майбутнього. Їхній подвиг назавжди залишиться в нашій пам’яті. \n\nВічна Слава і вдячність."
PHOTO_PATH = "photo.png"

def send_scheduled_message():
    # час Києва
    kyiv_time = datetime.now(ZoneInfo("Europe/Kyiv")).replace(
        hour=9,
        minute=0,
        second=0,
        microsecond=0
    )

    # якщо вже пройшло 9:00 — ставимо на завтра
    now_kyiv = datetime.now(ZoneInfo("Europe/Kyiv"))
    if now_kyiv >= kyiv_time:
        kyiv_time = kyiv_time.replace(day=kyiv_time.day + 1)

    timestamp = int(kyiv_time.timestamp())

    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

    with open(PHOTO_PATH, "rb") as photo_file:
        payload = {
            "chat_id": CHAT_USERNAME,
            "caption": MESSAGE,
            "schedule_date": timestamp
        }
        files = {"photo": photo_file}

        r = requests.post(url, data=payload, files=files)
        print("Send status:", r.status_code, r.text)

if __name__ == "__main__":
    print("Створюємо заплановане повідомлення...")
    send_scheduled_message()