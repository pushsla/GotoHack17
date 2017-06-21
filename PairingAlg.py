
# coding: utf-8

#  # Надо:
# * Считать данные из текстового файла
# * Переделать в numpy array(2 размерности)
# * **ОБЯЗАТЕЛЬНО** нагенерить данных для обучения
# * Разбить на выборки
# * Обучить модель
# * Перевести предсказания в пары

# In[69]:


import numpy as np
import pandas as ps


# In[70]:


dtt = open('userset.txt', 'r')
dt = dtt.readlines()
dtt.close()
dat = [] # Будущие данные о пользователях
for usr in dt:
    dat.append(usr.split(','))  # ВАЖНО! разделитель данных -- ЗАПЯТАЯ

#''' Данные о пользователе: [id, nickname, room_number, direction, (sports...)]
#                           [0,  kllllevo, 13,           1,         0,1,0,0]
#'''


# In[71]:


data = {}
for usr in dat:
    data[usr[0]] = list(usr[1:])

#''' Данные о пользователях: {'id':[Данные о пользователе, кроме id]} 
#'''
#data


# In[72]:


drata = []
for i in list(data.keys()):
    a = list(data.keys())
    a.remove(i)
    drata.append([val for val in a])

#''' Данные вида [another users id] -- this for user with id=0
#                [another users id] -- for id=1
#                [another users id] -- for id=2
#'''
#drata


# In[73]:


final_data = []
nmb = 1 # id юзера(см. ниже)
for lst in drata:
    top_ids= [] #здесь хранятся id
    with_ids = [] # тут -- число совпадений
    top = []
    for u in lst:
        u_data = np.array(data[u][1:])# Вся дата того, кого проверяем, кроме nickname
        usr_data = np.array(data[str(nmb)][1:])# Вся дата того, ДЛЯ кого проверяем, кроме nickname
        with_ids.append(len(np.where(u_data == usr_data)[0]))
        top_ids.append(u)
    args_by_sort = np.argsort(np.array(with_ids))
    #print('top_ids',top_ids)
    #print('with_ids',with_ids)
    #print('args_by_sort',args_by_sort)
    for arg in args_by_sort:
        top.append(top_ids[arg])
    final_data.append(top)
    nmb += 1
#'''Вот это то, ради чего мы все тут собрались. Данная клетка воплощает идею о том,
#Чтобы составить все возможные пары киллер-жертва, и отсортировать потенциальных жертв по
#кол-ву совпадений по признакам. Выхлоп -- внизу
#'''
#print(final_data[0])


# In[74]:


weighted_data = []
for lst in final_data:#Не забыть nmb += 1
    weighted = []
    cloned_final = list(final_data)
    cloned_final.remove(lst)
    for u in lst:   
        weight = 0
        for sub_lst in cloned_final:
            for sub_u in sub_lst:
                if sub_lst.index(sub_u) <= lst.index(u) and u == sub_u:
                    weight += 1#0.5*(int(lst.index(u)) - int(sub_lst.index(sub_u))) + int(lst.index(u)) - int(sub_lst.index(sub_u))
        weighted.append(weight)
    weighted_data.append(weighted)
#''' Данная чудо-ячейка возвращает нам матрицу с "весами" id ,где каждому элементу этого массива
#сопоставляется id из final_data
#'''
#weighted_data


# In[75]:


pairs = []
forbidden = []
nmb = 0
for killer in weighted_data:
    min_index = None
    min_d = (len(weighted_data)+1)**(len(weighted_data))
    for victim in killer:
        if victim <= min_d:
            min_d = victim
            min_index = killer.index(victim)
    pairs.append([str(final_data.index(final_data[nmb])+1), final_data[nmb][min_index]])
    forbid_weight = weighted_data[int(final_data[nmb][min_index])-1]# Массив весов для чувака, которого мы выбрали в качестве жертвы
    forbid_arr = final_data[int(final_data[nmb][min_index])-1]# Массив пар для чувака, которого мы выбрали в качестве жертвы
    forbid_index = forbid_arr.index(str(nmb+1))# Индекс(номер в массиве) чувака, который является киллером вон того ^
    forbid_weight[forbid_index] = (len(weighted_data)+1)**(len(weighted_data))# Для того, чтобы не было: А убив. Б, а Б убив. А
    weighted_data[int(final_data[nmb][min_index])-1] = forbid_weight# заносим изменения в таблицу весов
    
    victimed = final_data[nmb][min_index] # Все вот это делается для того, чтобы игрок не был жертвой двух киллеров
    for killer in final_data:
        try:
            vic_index = killer.index(victimed)
            kil_index = final_data.index(killer)
            weighted_data[kil_index][vic_index] = (len(weighted_data)+1)**(len(weighted_data))
        except ValueError:
            pass
    
    nmb += 1
#print(pairs)
#''' А вот здесь, мой дорогой читатель, если ты еще не умер от обилия говнокода, ты можешь видеть
#механизм распределения на пары киллер-жертва, ради которого и делался весь вот этот ^^^^^^ говнокод.
#Возвращает пары по id
#'''
weighted_data


# In[76]:


fil = open('pairs.txt', 'w')
for i in pairs:
    fil.write(data[i[0]][0]+','+data[i[1]][0]+"\n")
fil.close()

