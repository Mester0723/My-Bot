import config
import telebot
from random import choice, randint

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f"Привет, добро пожаловать в бота {config.bot_name}!\n"
                           "Напиши /help, чтобы узнать, что я умею.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "/emoji - отправить эмодзи\n"
                          "/weather - узнать погоду\n"
                          "/news - получить последние новости\n"
                          "/joke - рассказать анекдот\n"
                          "/quote - получить цитату\n"
                          "/info - информация о боте")

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, f"Я бот {config.bot_name}, созданный для помощи пользователям. Мой разработчик - @nektery. Моя версия - 1.0. Я умею делать много интересного, просто напиши /help, чтобы узнать больше.")

@bot.message_handler(commands=['emoji'])
def send_emoji(message):
    bot.reply_to(message, "Доступные эмодзи: \n"
                          "😀 - Улыбающееся лицо /fun_f\n"
                          "😂 - Лицо со слезами радости /laugh_f\n"
                          "😍 - Лицо с сердечками /hrts_f\n"
                          "😎 - Лицо в солнцезащитных очках /gls_f\n"
                          "🤔 - Задумчивое лицо /ps_f\n"
                          "😢 - Плачущая улыбка /sad_f\n"
                          "😡 - Сердитое лицо /angry_f\n"
                          "🥳 - Лицо с вечеринкой /party_f"
                          "? - Случайный эмодзи из предложенных /face")
    
@bot.message_handler(commands=['fun_f'])
def send_fun_f(message):
    bot.reply_to(message, "😀")

@bot.message_handler(commands=['laugh_f'])
def send_laugh_f(message):
    bot.reply_to(message, "😂")
                 
@bot.message_handler(commands=['hrts_f'])
def send_hrts_f(message):
    bot.reply_to(message, "😍")
                 
@bot.message_handler(commands=['gls_f'])
def send_gls_f(message):
    bot.reply_to(message, "😎")

@bot.message_handler(commands=['ps_f'])
def send_ps_f(message):
    bot.reply_to(message, "🤔")

@bot.message_handler(commands=['sad_f'])
def send_sad_f(message):
    bot.reply_to(message, "😢")

@bot.message_handler(commands=['angry_f'])
def send_angry_f(message):
    bot.reply_to(message, "😡")

@bot.message_handler(commands=['party_f'])
def send_party_f(message):
    bot.reply_to(message, "🥳")

@bot.message_handler(commands=['face'])
def send_face(message):
    faces = choice(["😀", "😂", "😍", "😎", "🤔", "😢", "😡", "🥳"])
    bot.reply_to(message, faces)

@bot.message_handler(commands=['weather'])
def send_weather(message):
    bot.reply_to(message, "Этой функцией я пока не обладаю, но скоро она появится!")
                 
@bot.message_handler(commands=['news'])
def send_news(message):
    bot.reply_to(message, "Этой функцией я пока не обладаю, но скоро она появится!")

@bot.message_handler(commands=['joke'])
def send_joke(message):
    joke = randint([1, 10])
    if joke == 1:
        bot.reply_to(message, "Почему Java-программисты носят очки?\n"
                     "— Потому что они не C#.")
    elif joke == 2:
        bot.reply_to(message, "— Сколько программистов нужно, чтобы вкрутить лампочку?\n"
                     "— Ни одного. Это проблема железа.")
    elif joke == 3:
        bot.reply_to(message, "— У тебя снова деплой в пятницу?!\n"
                     "— Ага, я люблю острые ощущения.")
    elif joke == 4:
        bot.reply_to(message, "Реальный страх программиста —\n"
                     "Это когда код, который не должен работать, начинает работать.")
    elif joke == 5:
        bot.reply_to(message, "— Почему ты удалил весь свой код?\n"
                     "— Потому что в нем было слишком много багов. Я решил, что багов не будет, если не будет и кода.")
    elif joke == 6:
        bot.reply_to(message, "— Почему Python-разработчики такие спокойные?\n"
                     "— Потому что у них всё try: и ничего except:.")
    elif joke == 7:
        bot.reply_to(message, "Python — это когда код читается как английский…\n"
                     "Пока ты не начнёшь его запускать.")
    elif joke == 8:
        bot.reply_to(message, "— Кто твой любимый супергерой?\n"
                     "— Тот, кто закрывает все теги.")
    elif joke == 9:
        bot.reply_to(message, "— Как HTML просит CSS о помощи?\n"
                     "— Я голый без тебя!")
    elif joke == 10:
        bot.reply_to(message, "Не пугай HTML-разработчика:\n"
                     "Просто скажи, что у тебя браузер отключил CSS.")
        
@bot.message_handler(commands=['quote'])
def send_quote(message):
    quotes = [
        "«Программирование — это искусство, а не наука.» — Джон Фаулер",
        "«Программисты — это люди, которые решают проблемы, о которых вы не знали, способами, которые вы не понимаете.» — Джефф Атвуд",
        "«Самый лучший способ предсказать будущее — это создать его.» — Алан Кей",
        "«Код должен быть написан так, чтобы его могли читать люди, а не машины.» — Мартин Фаулер",
        "«Программирование — это не только наука, но и искусство.» — Бен Хорowitz"
    ]
    bot.reply_to(message, choice(quotes))