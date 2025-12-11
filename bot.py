import os
import telebot
from flask import Flask, request, abort

TOKEN = os.environ.get("TELEGRAM_TOKEN")
PUBLIC_URL = os.environ.get("PUBLIC_URL")

if not TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN not set")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_cmd(message):
    bot.send_message(message.chat.id, "🔥 Bot is working! You sent /start")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.send_message(message.chat.id, "Help menu here.")

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    print("📩 Incoming update received!")
    if request.headers.get("content-type") != "application/json":
        abort(403)
    data = request.get_data().decode("utf-8")
    print("Raw update:", data)
    update = telebot.types.Update.de_json(data)
    bot.process_new_updates([update])
    return "", 200

def set_webhook():
    url = f"{PUBLIC_URL}/{TOKEN}"
    print("Setting webhook to:", url)
    bot.set_webhook(url=url)

if __name__ == "__main__":
    set_webhook()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))