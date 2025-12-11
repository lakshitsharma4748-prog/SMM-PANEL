import os
import telebot

# Get token from environment variable
BOT_TOKEN = os.environ.get("TELEGRAM_TOKEN")

if not BOT_TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN not set in Railway Variables!")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_cmd(message):
    bot.reply_to(message, "👋 Bot is running 24/7 on Railway!\nSend /help for more.")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "Available commands:\n/start - check bot is working\n/help - show help menu")

print("🔥 Bot is running on Railway (polling)...")
bot.infinity_polling()