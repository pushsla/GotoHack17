import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.token)

id_1 = []
id_2 = int(input("Input your ID : "))
id_1.append(id_2)
len_ = len(id_1)
nickname = []
nn = input("Input your nickname  : ")
nickname.append(nn)
life_status = 1


f = open('data.txt', 'a')

for number in range(len_):
    f.write(str(id_1[number]))
    f.write(",")
    f.write(str(nickname[number]))
    f.write(",")
    f.write(str(life_status))
    f.write("\n")

f.close()

f = open('data.txt', 'r')

#a = int(input("Input ID for information of life status :"))
#for id_2 in range(0, len_):
    #print("Here's your life status - {text}".format(text = life_status))

print("What characteristics do you want to change?")

b = input("")
if b == "ID":
    id_1.insert(1, 1488)
    print("{text}".format(text = id_1))
if b == "nickname":
    nickname.insert(1, "wabbalubbadubdub")
    print("{text}".format(text = nickname))
if b == "life status":
    life_status = 0
    print("{text}".format(text = life_status))




