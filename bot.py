import os
import telebot
from flask import Flask, request, abort

TOKEN = os.environ.get("TELEGRAM_TOKEN")
PUBLIC_URL = os.environ.get("PUBLIC_URL")  # e.g. https://your-service.onrender.com

if not TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN env var not set")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.reply_to(message, "👋 Welcome — bot is active (webhook). Use /help.")

@bot.message_handler(commands=['help'])
def cmd_help(message):
    bot.reply_to(message, "Help: /start /help")

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    if request.headers.get("content-type") != "application/json":
        abort(403)
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "", 200

def set_webhook():
    if not PUBLIC_URL:
        print("PUBLIC_URL not set; skipping webhook registration.")
        return
    webhook_url = f"{PUBLIC_URL}/{TOKEN}"
    print("Setting webhook to:", webhook_url)
    ok = bot.set_webhook(url=webhook_url)
    print("set_webhook result:", ok)

if __name__ == "__main__":
    set_webhook()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))