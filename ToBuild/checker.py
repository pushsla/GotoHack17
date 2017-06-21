#!/usr/bin/python
# # HowToUse this defines
# ## Всем функциям передается имя массива, в котором хранятся данные
# ## Для создания массива с данными
# * Вызывается initialise(name), где name -- имя файла со статусами. Функция возвращает массив массивов по строками
# ## Для получения информации о игроке
# * Вызывается get_status(data, id), где data -- имя массива(см. выше), а id -- идентификатор игрока
# ## Для изменения статуса игрока
# * Вызывается set_status(data, id, status), где data -- имя массива, id -- идентификатор, status -- новый статус(0\1)
# ##Для добавления нового пользователя
# * Вызывается add_gamer(data, nick), где data -- имя массива, nick -- имя нового игрока. По умолчанию статус нового игрока -- 1(жив)
# ## Для записи измененных данных в файл
# * Вызывается write_data(data, name), где data -- имя массива, name -- имя файла для записи.<br>
# **При записи данных в файл, он ПЕРЕЗАПИСЫВАЕТСЯ.**


def initialise(name):
    fil = open(name, 'r')
    data = fil.readlines()
    fil.close()
    data = [val.split(',') for val in data]
    for i in range(len(data)):
        for s in range(len(data[i])):
            data[i][s] = data[i][s].split('\n')[0]
    return data


def get_status(data, id_):
    return data[id_][-1]


def set_status(data, id_, st):
    data[id_][-1] = st


def add_gamer(data, nick):
    id_ = len(data)+1
    data.append([id_, nick, 1])


def write_data(data, name):
    fil = open(name, 'w')
    for i in data:
        st = str(i[0])+','+str(i[1])+','+str(i[2])+'\n'
        fil.write(st)
    fil.close()
