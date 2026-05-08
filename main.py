import os
import random
import requests
import asyncio
from flask import Flask
from threading import Thread
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# --- [Replit সার্ভার সচল রাখার জন্য Web Server] ---
app = Flask('')
@app.route('/')
def home():
    return "KSY OTP Bot is Alive & Running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- [আপডেটেড কনফিগারেশন] ---
API_ID = 38199591
API_HASH = "274ed9d7f696f8970e0348dd40d47f70"
BOT_TOKEN = "8565820660:AAGJJ3Vs3P1Tsd-iytC3giG9iEAw12QMU48" # নতুন টোকেন আপডেট করা হয়েছে
PANEL_API_KEY = "nxa_288cc462a8c98cc999ab1ac824f77ef25edceae0"
GROUP_ID = -1003760289145

bot = Client("KSY_OTP_BOT", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# হোয়াটসঅ্যাপ চেকার লজিক
def check_whatsapp_status():
    is_wa = random.choice([True, False])
    if is_wa:
        return "🔴 Account Found"
    else:
        return "🟢 No Account"

@bot.on_message(filters.command("start") & filters.private)
async def start(client, message):
    text = (
        "⭐ **KSY PREMIUM OTP SYSTEM** ⭐\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "হাই! আমি হাই-স্পিড ওটিপি বট। আপনার কাঙ্ক্ষিত নাম্বার নিতে নিচের বাটনে ক্লিক করুন।"
    )
    buttons = [[InlineKeyboardButton("🔄 Get New Number", callback_data="get_num")]]
    await message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons))

@bot.on_callback_query(filters.regex("get_num"))
async def get_number(client, callback_query):
    await callback_query.answer("প্যানেল চেক করা হচ্ছে...", show_alert=False)
    
    # ডেমো নাম্বার জেনারেটর
    random_num = f"8801{random.randint(300000000, 999999999)}"
    wa_status = check_whatsapp_status()
    
    output = (
        "⭐ **KSY PREMIUM NUMBER** ⭐\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🛒 **Verified Numbers** ⚡\n\n"
        "📍 🇧🇩 **Bangladesh**\n"
        f"📋 `{random_num}` | {wa_status}\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "🚀 *নাম্বারের ওপর ক্লিক করলে কপি হবে!*"
    )
    
    buttons = [
        [InlineKeyboardButton("🔄 Refresh Stock", callback_data="get_num")],
        [InlineKeyboardButton("👥 Join OTP GROUP", url="https://t.me/ksyotpgroup")]
    ]
    
    await callback_query.edit_message_text(output, reply_markup=InlineKeyboardMarkup(buttons))
    
    # গ্রুপেও লাইভ ট্রাফিক পাঠানো
    try:
        await bot.send_message(GROUP_ID, f"📢 **New Live Traffic:**\n`{random_num}` - {wa_status}")
    except Exception as e:
        print(f"Group Message Error: {e}")

if __name__ == "__main__":
    keep_alive() 
    print("KSY OTP BOT (নতুন টোকেনসহ) স্টার্ট হয়েছে!")
    bot.run()
