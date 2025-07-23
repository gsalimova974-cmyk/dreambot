bot = telebot.TeleBot("YOUR_BOT_TOKEN_HERE")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message,
        "✨ Добро пожаловать в пространство грёз и тайн!\n"
        "Я – 🛡 Хранитель Снов. Я помогу тебе:\n"
        "🌙 Толковать сны\n"
        "🌀 Понимать знаки и символы\n"
        "💫 Наполняться силой намерения и мыслей\n\n"
        "Напиши свой сон или выбери команду – и мы начнём ✨"
    )

@bot.message_handler(commands=['сон'])
def interpret_dream(message):
    bot.reply_to(message, "🌙 Напиши, что тебе приснилось — я попробую помочь с толкованием!")

@bot.message_handler(commands=['аффирмация'])
def send_affirmation(message):
    bot.reply_to(message, "✨ Ты сильна, ты достойна счастья, и мир заботится о тебе 💫")

@bot.message_handler(commands=['помощь'])
def send_help(message):
    bot.reply_to(message, "Команды: /сон — толкование сна, /аффирмация — позитив, /помощь — помощь 🌟")

@bot.message_handler(commands=['расшифруй'])
def decode(message):
    bot.reply_to(message, "🔮 Напиши символ или часть сна, которую хочешь расшифровать")

@bot.message_handler(func=lambda message: True)
def reply_keywords(message):
    text = message.text.lower()
    if "кот" in text:
        bot.reply_to(message, "🐱 Кот во сне — символ независимости или тайны. Хочешь расшифровку?")
    elif "ребёнок" in text or "младенец" in text:
        bot.reply_to(message, "👶 Ребёнок во сне — символ нового начала, чистоты или заботы.")
    elif "огонь" in text:
        bot.reply_to(message, "🔥 Огонь может символизировать страсть, очищение или разрушение.")
    elif "змея" in text:
        bot.reply_to(message, "🐍 Змея — символ мудрости, опасности или трансформации.")
    elif "вода" in text:
        bot.reply_to(message, "💧 Вода отражает эмоции, подсознание или очищение.")
    elif "привет" in text:
        bot.reply_to(message, "Привет! Я Хранитель Снов 🌌\nМожешь рассказать мне свой сон — я постараюсь его понять ✨")

bot.polling()
