import telebot
from telebot import types

token = "449785571:AAGk5QYoPiNdeshBHUsA_PNp-oNsoloSNgQ"

bot = telebot.TeleBot(token=token)

users = {}

truth = [True, True, False, False, False, False, False, False, False, False, False, False, False, False, False]

i = 0
string = '0'

data = []

def initialise(name):
    global data
    fil = open(name, 'r')
    data = fil.readlines()
    fil.close()
    data = [val.split(',') for val in data]
    for i in range(len(data)):
        for s in range(len(data[i])):
            data[i][s] = data[i][s].split('\n')[0]


def get_status(id_):
    global data
    return data[id_][-1]


def set_status(id_, st):
    global data
    data[id_][-1] = st


def add_gamer(nick):
    global data
    id_ = len(data)+1
    data.append([id_, nick, 1])


def write_data(name):
    global data
    fil = open(name, 'w')
    for i in data:
        st = ''
        for bi in i:
            st+=(bi+',')
        fil.write(st)
    fil.close()

x = False

@bot.message_handler(commands=["start"])
def DIRECTION(message):
    if truth[0] == True:
        print("Success!")
        initialise('userset.txt')
        data.append([])
        bot.send_message(message.chat.id, "Хочешь сыграть в киллера?  Да/Нет")
        truth[0] = False
        
@bot.message_handler(content_types=["text"])
def start(message):
    global string, i, x
    if truth[1] == True and (message.text.lower() == "да" or i == 1):
        bot.send_message(message.chat.id, "Здравствуй, у меня есть для тебя заказ. Сообщи свои данные чтобы я мог назначить тебя подальше от врагов.")
        bot.send_message(message.chat.id, "Назови своё имя:")
        truth[1] = False
        truth[2] = True
    elif truth[1] == True and message.text.lower() == "нет":
        bot.send_message(message.chat.id, "Заходи в другой раз, каждый день в 14:00.")
    elif truth[2] == True:
        string = message.text
        bot.send_message(message.chat.id, "Подтверди:")
        f = '0'
        i = 2
        truth[2] = False
        truth[6] = True
    elif truth[3] == True:
        add_gamer(string)
        bot.send_message(message.chat.id, "Номер комнаты:")
        truth[3] = False
        truth[4] = True
    elif truth[4] == True:
        string = message.text
        bot.send_message(message.chat.id, "Подтверди:")
        truth[4] = False
        truth[6] = True
        i = 4
    elif truth[5] == True:
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
        bot.send_message(message.chat.id, "Нажмите любую кнопку (+enter) для продолжения...")
    elif truth[6] == True:
        f = message.text
        print(f)
        if f != string:
            bot.send_message(message.chat.id, "Не совпадают, повтори операцию...")
            bot.send_message(message.chat.id, "Нажмите на любую кнопку (+ enter)...")
            i -= 1
            truth[6] = False
            truth[i] = True
        else:
            truth[6] = False
            i += 1
            data[len(data) - 1].append(f)
            truth[i] = True
            bot.send_message(message.chat.id, "Нажмите любую кнопку (+enter) для продолжения...")
            x = True
    elif truth[7] == True:
        keyboard = types.InlineKeyboardMarkup()
        callback_button0 = types.InlineKeyboardButton(text="Да", callback_data="1")
        callback_button1 = types.InlineKeyboardButton(text="Нет", callback_data="0")
        keyboard.add(callback_button0)
        keyboard.add(callback_button1)
        bot.send_message(message.chat.id, "Играешь в настольный теннис?:", reply_markup=keyboard)
        truth[7] = False
        truth[4] = True
        bot.send_message(message.chat.id, "Нажмите любую кнопку (+enter) для продолжения...")
    elif truth[8] == True:
        keyboard = types.InlineKeyboardMarkup()
        callback_button0 = types.InlineKeyboardButton(text="Да", callback_data="1")
        callback_button1 = types.InlineKeyboardButton(text="Нет", callback_data="0")
        keyboard.add(callback_button0)
        keyboard.add(callback_button1)
        bot.send_message(message.chat.id, "Играешь в футбол?", reply_markup=keyboard)
        truth[8] = False
        truth[3] = True
        bot.send_message(message.chat.id, "Нажмите любую кнопку (+enter) для продолжения...")
    elif truth[9] == True:
        keyboard = types.InlineKeyboardMarkup()
        callback_button0 = types.InlineKeyboardButton(text="Да", callback_data="1")
        callback_button1 = types.InlineKeyboardButton(text="Нет", callback_data="0")
        keyboard.add(callback_button0)
        keyboard.add(callback_button1)
        bot.send_message(message.chat.id, "Играешь в волейбол?", reply_markup=keyboard)
        truth[9] = False
        truth[2] = True
        bot.send_message(message.chat.id, "Нажмите любую кнопку (+enter) для продолжения...")
        
@bot.callback_query_handler(func=lambda call: True)
def CALL(call):
    if truth[5] == True:
        while True:
            if call.message:
                d = call.data
                break
        print(d)
        data[len(data) - 1].append(d)
        truth[5] = False
        truth[7] = True
    elif   truth[4] == True:
        d = '0'
        while True:
            if call.message:
                d = call.data
                break
        print(d)
        data[len(data) - 1].append(d)
        truth[4] = False
        truth[8] = True
    elif truth [3] == True:
        while True:
            if call.message:
                d = call.data
                break
        print(d)
        data[len(data) - 1].append(d)
        truth[3] = False
        truth[9] = True
    elif truth [2] == True:
        while True:
            if call.message:
                d = call.data
                break
        print(d)
        data[len(data) - 1].append(d)
        truth[2] = False
        write_data('userset.txt')
        truth[0] = True

bot.polling(none_stop=True)