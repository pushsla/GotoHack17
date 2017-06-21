import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.token)

id_1 = []#количество должно быть равно 4
id = int(input("Input your ID : "))
id_1.append(id)
len_ = len(id_1)
nickname = []#количество должно быть равно 4
nn = input("Input your nickname  : ")
nickname.append(nn)
life_status = [1, 1, 1, 1]


f = open('data.txt', 'a')

for number in range(len_):
    f.write(str(id_1[number]))
    f.write(",")
    f.write(str(nickname[number]))
    f.write(",")
    f.write(str(life_status[number]))
    f.write("\n")

f.close()

f = open('data.txt', 'r')

a = int(input("Input ID for information of life status :"))
for id in range(0, id_1):
    print(life_status)

#f = open('data.txt', 'r')
#file = f.readlines()
#parsed = []
#n = 0s
#for string in file:
#    parsed.append(string.split(','))
#print("")
#for i in range(len(parsed) - 1):
#    if parsed[i + 1][2] > parsed[i][2]:
#        for j in range(i + 1, 0, -1):
#            if parsed[j][2] > parsed[j - 1][2]:
#                m = parsed[j - 1]
#                parsed[j - 1] = parsed[j]
#                parsed[j] = m
#for number in range(len(parsed)):
#    for i in range(len(parsed[number])):
#        print(parsed[number][i], end='')
#        if i + 1 != len(parsed[number]):
#            print(", ", end = '')
#        else: print("")
#f.close()
#f = open('data.txt', 'w')
#for number in range(len(parsed)):
#    f.write(str(parsed[number][0]))
#    f.write(",")
#    f.write(str(parsed[number][1]))
#    f.write(",")
#    f.write(str(parsed[number][2]))
#    f.write("\n")
#f.close()

#'''Он выдает в переменную parsed массив, в котором
#элементами являются массивы [id,nickname,status]
#'''


