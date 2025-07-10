import telebot

bot = telebot.TeleBot("7931213390:AAHXig_t0Gn87APVHFyUj92L9710OOHgEKI")

waiting_users = []

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "سلام! به ربات ناشناس ماندگار خوش اومدی. برای شروع /search رو بزن.")

@bot.message_handler(commands=['search'])
def search(message):
    user_id = message.chat.id
    if user_id not in waiting_users:
        waiting_users.append(user_id)
        bot.send_message(user_id, "منتظر طرف مقابل...")
    else:
        partner_id = waiting_users.pop(0)
        bot.send_message(user_id, "طرف پیدا شد! شروع کنید 👌")
        bot.send_message(partner_id, "طرف پیدا شد! شروع کنید 👌")

bot.polling()
