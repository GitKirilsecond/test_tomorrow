from flask import Flask
import requests
import os

app = Flask(__name__)

TOKEN = "8581090817:AAFC1bzXTfJvqHHxFmPzfXECciSjrErbyjM"
CHAT_USERNAME = "@asdqwesszx"
MESSAGE = "Зупинімося на мить, щоб вшанувати пам’ять Героїв, які поклали своє життя заради нашого майбутнього. Їхній подвиг назавжди залишиться в нашій пам’яті.\n\nВічна Слава і вдячність."
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
        print(r.status_code, r.text)

@app.route("/send")
def send():
    send_message()
    return "OK"

@app.route("/")
def home():
    return "Bot is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))