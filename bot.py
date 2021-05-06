from decouple import config
import telebot
import time
bot_token = config('TOKEN')

USED_WORDS = []


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Привет! Я могу создать 'Облако' из слов, похожих на то, что вы ввведете. Попробуем? (/yes, /no)")


    @bot.message_handler(commands=["yes"])
    def start_message(message):
        try:
            bot.send_message(message.chat.id, 
            """Отлично, напишите мне слово или словосочетание (Любимый фильм/музыкант/автомобиль - что угодно!), начиная со слова 'Поиск' (Поиск - .........)
            Пойдем дальше? (/next)"""
            )
        except Exception as ex:
            print(ex)
            bot.send_message(message.chat.id, "Что-то пошло не так((")

    @bot.message_handler(commands=["no"])
    def start_message(message):
        try:
            bot.send_message(message.chat.id, "Окей. Если надумаете, перезапустите меня командой /start")
        except Exception as ex:
            print(ex)
            bot.send_message(message.chat.id, "Что-то пошло не так((")

    @bot.message_handler(commands=["next"])
    def start_message(message):
        try:
            bot.send_message(message.chat.id, 
            """
            Пришлите мне ссылку на картинку, в форме которой будет облако


            Совет! Для лучшего результата возьмити картинку с белым фоном и черный объектом на нем
            """)
        except Exception as ex:
            print(ex)
            bot.send_message(message.chat.id, "Что-то пошло не так((")    
    link = None

    @bot.message_handler(content_types=["text"])
    def save_link(message):   
        if "http" in message.text:
            try:
                bot.send_message(message.chat.id, "Окей. Если надумаешь, перезапусти меня командой /start")
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Что-то пошло не так((")

    @bot.message_handler(content_types=["text"])
    def send_wordcloud(message):
        a = message.text
        bot.send_message(f"Ты написал: {a}", chat_id=message.from_user.id)   
        # if "Поиск" in str(message.text):
        #     try:
        #         to_search = message.text.split('-')
        #         print(to_search)
        #         bot.send_message(message.chat.id, "Окей. Если надумаете, перезапустите меня командой /start")
        #     except Exception as ex:
        #         print(ex)
        #         bot.send_message(message.chat.id, "Что-то пошло не так((")

    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e) 

telegram_bot(bot_token)