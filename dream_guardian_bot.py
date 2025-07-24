import telebot
from telebot import types

# ⬇️ ВСТАВЬ СВОЙ ТОКЕН между кавычками:
bot = telebot.TeleBot("7706170101:AAHGTixRKGcwn3R7m6omRvfodS4gdbWfhtM")

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔮 Толкование сна")
    btn2 = types.KeyboardButton("🌙 Аффирмации")
    btn3 = types.KeyboardButton("📘 Справочник по снам")
    btn4 = types.KeyboardButton("📝 Истории снов")
    btn5 = types.KeyboardButton("❓ Помощь")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    markup.add(btn5)
    bot.send_message(message.chat.id,
                     "Привет! Я 🌙 Хранитель Снов.\nВыбери, с чего начнём:",
                     reply_markup=markup)

# Обработка кнопок
@bot.message_handler(func=lambda msg: msg.text == "🔮 Толкование сна")
def interpret_dream(message):
    bot.send_message(message.chat.id, "Напиши мне, что тебе приснилось — и я попробую помочь с толкованием! 💤")

@bot.message_handler(func=lambda msg: msg.text == "🌙 Аффирмации")
def send_affirmations(message):
    bot.send_message(message.chat.id, "Вот аффирмация на ночь:\n✨ Я отпускаю тревоги и погружаюсь в мирный сон.")

@bot.message_handler(func=lambda msg: msg.text == "📘 Справочник по снам")
def send_guide(message):
    bot.send_message(message.chat.id, "Пиши первую букву интересующего тебя символа — и я покажу, что означает твой сон 📖")

@bot.message_handler(func=lambda msg: msg.text == "📝 Истории снов")
def send_stories(message):
    bot.send_message(message.chat.id, "Скоро здесь появятся удивительные истории, где сны сбывались...")

@bot.message_handler(func=lambda msg: msg.text == "❓ Помощь")
def help_info(message):
    bot.send_message(message.chat.id,
                     "Я могу помочь:\n🔹 растолковать сон\n🔹 подобрать аффирмацию\n🔹 поделиться справочником символов\n\nНапиши или выбери из меню ниже 💬")

# Остальные текстовые сообщения
@bot.message_handler(func=lambda msg: True)
def fallback(message):
    bot.send_message(message.chat.id, "Я тебя слышу! 😊 Напиши сон или выбери пункт из меню ниже.")

bot.infinity_polling()
