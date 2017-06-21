import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.token)

len = 6
id = [1, 2, 3, 4, 5, 6]
nickname = ['fluttershy', 'pinkiepie', 'rainbowdash', 'twilightsparkle', 'applejack', 'rarity']
life_status = [0, 1, 0, 0, 1, 0]
f = open('data.txt', 'w')

for number in range(len):
    f.write(str(id[number]))
    f.write(", ")
    f.write(str(nickname[number]))
    f.write(", ")
    f.write(str(life_status[number]))
    f.write("\n")

f.close()

f = open('data.txt', 'r')
file_readed = f.read()
f.close()
f = open('data.txt', 'w')
f.write()



