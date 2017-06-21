#!/usr/bin/python
import telebot
from telebot import types

token = "449785571:AAGk5QYoPiNdeshBHUsA_PNp-oNsoloSNgQ"

bot = telebot.TeleBot(token=token)

users = {}

truth = [True, True, False, False, False, False, False]

i = 0
string = '0'

data = []

def initialise(name):
    fil = open(name, 'r')
    data = fil.readlines()
    fil.close()
    data = [val.split(',') for val in data]
    for i in range(len(data)):
        for s in range(len(data[i])):
            data[i][s] = data[i][s].split('\n')[0]
    return data


def get_status(id_):
    return data[id_][-1]


def set_status(id_, st):
    data[id_][-1] = st


def add_gamer(nick):
    id_ = len(data)+1
    data.append([id_, nick, 1])


def write_data(name):
    fil = open(name, 'w')
    for i in data:
        st = str(i[0])+','+str(i[1])+','+str(i[2])+'\n'
        fil.write(st)
    fil.close()

@bot.message_handler(commands=["start"])
def DIRECTION(message):
    if truth[0] == True:
        print("Succes!")
        bot.send_message(message.chat.id, "Хочешь сыграть в киллера?  Да/Нет")
        truth[0] = False

def exactly(message, string, f, i):
    print (f)
    bot.send_message(message.chat.id, "Подтверди...")
    while f == '0':
        f = message.text
    print (f)
    if f != string:
        bot.send_message(message.chat.id, "Не совпадают, повторим операцию...")
        truth[i] = False
        truth[i-1] = True
    else:
        truth[i] = False
        truth[i + 1] = True
    return f

@bot.message_handler(content_types=["text"])
def start(message):
    global string, i
    if truth[1] == True and (message.text == "Да" or i == 1):
        bot.send_message(message.chat.id, "Здравствуй, у меня есть для тебя заказ. Сообщи свои данные чтобы я мог назначить тебя подальше от врагов.")
        bot.send_message(message.chat.id, "Назови своё имя:")
        truth[1] = False
        truth[2] = True
    elif truth[1] == True and message.text == "Нет":
        bot.send_message(message.chat.id, "Заходи в другой раз, каждый день в 14:00.")
    elif truth[2] == True:
        string = message.text
        bot.send_message(message.chat.id, "Подтверди:")
        f = '0'
        i = 2
        truth[2] = False
        truth[5] = True
    elif truth[3] == True:
        add_gamer(string)
        bot.send_message(message.chat.id, "Номер комнаты:")
        truth[3] = False
        truth[4] = True
    elif truth[4] == True:
        keyboard = types.InlineKeyboardMarkup()
        callback_button0 = types.InlineKeyboardButton(text="РОБОТОТЕХНИКА", callback_data="1")
        callback_button1 = types.InlineKeyboardButton(text="ПРИКЛАДНОЕ ПРОГРАММИРОВАНИЕ", callback_data="2")
        callback_button2 = types.InlineKeyboardButton(text="АНАЛИЗ ДАННЫХ", callback_data="3")
        callback_button3 = types.InlineKeyboardButton(text="БИОИНФОРМАТИКА", callback_data="4")
        keyboard.add(callback_button0)
        keyboard.add(callback_button1)
        keyboard.add(callback_button2)
        keyboard.add(callback_button3)
        bot.send_message(message.chat.id, "ВАШЕ НАПРАВЛЕНИЕ:", reply_markup=keyboard)
    elif truth[5] == True:
        f = message.text
        print(f)
        if f != string:
            bot.send_message(message.chat.id, "Не совпадают, повтори операцию...", "\n", "Нажмите на любую кнопку (+ enter)...")
            i -= 1
            truth[i] = True
        else:
            i += 1
            truth[i] = True
            bot.send_message(message.chat.id, "Нажмите на любую кнопку (+ enter)...")


@bot.callback_query_handler(func=lambda call: True)
def CALL(call):
    if call.message:
        if call.data == "1":
            D = 1
            print(D)
        if call.data == "2":
            D = 2
            print(D)
        if call.data == "3":
            D = 3
            print(D)
        if call.data == "4":
            D = 4
            print(D)

bot.polling(none_stop=True)
