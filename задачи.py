"""Написать декоратор который будет
отправлять в текстовый файл ошибки в
функции деления """
import random
import time
from datetime import datetime as dt
from math import sqrt

# def even_zero(func):
#     def wrap(*args, **kwargs):
#         try:
#             res = func(*args, **kwargs)
#             if res != round(res):
#                 raise ValueError('Результат не целое число')
#         except ZeroDivisionError as err:
#             with open('log.txt', 'a', encoding='utf-8') as f:
#                 f.write(f'{dt.now().replace(microsecond=0)} Деление на ноль\n')
#             return 'Деление на ноль'
#         except ValueError as err:
#             with open('log.txt', 'a', encoding='utf-8') as f:
#                 f.write(f'{dt.now().replace(microsecond=0)} {err}\n')
#             return err
#         else:
#             return int(res)
#
#     return wrap
#
#
# @even_zero
# def div():
#     x = random.randrange(0, 100, 2)
#     y = random.randint(0, 5)
#     time.sleep(.7)
#     return x / y
#
#
# # for _ in range(10):
# #     print(div())
# #     time.sleep(1)
# #
# # print(24.0 == 24)
#
# # x2, y2 = map(int, input().split())
# # x3, y3, r = map(int, input().split())
# x2, y2 = 5, 4
# x3, y3, r = 4, 0, 3
# count = 0
# for y in range(y3 - r, y3 + r + 1):
#     for x in range(x3 - r, x3 + r + 1):
#         # print(sqrt((x3 - x) ** 2 + (y3 - y) ** 2))
#         if sqrt((x3 - x) ** 2 + (y3 - y) ** 2) <= r:
#             # print(x, y)
#             if 0 <= x <= x2 and 0 <= y <= y2:
#                 count += 1
# print(count)
# set1 = {(x, y) for y in range(y3 - r, y3 + r + 1) for x in
#         range(x3 - r, x3 + r + 1) if sqrt((x3 - x) ** 2 + (y3 - y) ** 2) <= r }
# set2 = {(x, y) for y in range(0, y2 + 1) for x in range(0, x2 + 1)}
# set3 = set1 & set2
# print(len(set3))

# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# dict3 = dict1 | dict2
# dict3 = dict1.copy()
# dict3.update(dict2)
#
#
# print(dict3)
# print(dict3.setdefault('b', 5))
# words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# world = {}
# for i in words:
#     # world[i] = world.get(i, 0) + 1
#     world[i] = world.setdefault(i, 0) + 1
# print(world)

# print(4 // 4)
# print(3 // 4)
#
# print(8 // 4)
# print(7 // 4)
#
# n = int(input('Место в купе: '))
# if n % 4 == 0:
#     k = n // 4
# else:
#     k = n // 4 + 1
#
# print(f'№ купе: {k}')
# print(f'№ купе: {math.ceil(n / 4)}')
# print(f'№ купе: {(n-1) // 4 + 1}')


# name = ['Mary', 'Alex', 'Mark']
# age = [25, 46, 15]
#
# print(list(zip(name, age)))
# for n, a in zip(name, age):
#     print(f'{n} - {a}')
#
# for i in range(len(age)):
#     print(f'{name[i]} - {age[i]}')
#
# dic = dict([('Mary', 25), ('Alex', 46), ('Mark', 15)])
# print(dic)
# for i in dic.items():
#     print(i)

# dic = {'Mary': 25, 'Alex': 46, 'Mark': 15}
# print(dic['Mary'])
# print(dic.get('Mary1', 1000000))
# dic['Mary'] = 20
# dic['Mary1'] = 30
# dic.setdefault('Mary2', 33)
# print(dic)
# dic = {'Mary': ['Petrova', 20, 'student'],
#        'Alex': ['Petrov', 46, 'director'],
#        'Mark': ['Ivanov', 20, 'student']
#        }
#
# for k, v in dic.items():
#     print(k, v)
#
# for k, v in dic.items():
#     print(k, v[0], v[1], v[2])
#
# for k, (v, c, d) in dic.items():
#     print(k, v, '-', str(c) + ' лет,', d)

"""Маша готовит ужин и собирает информацию о всех продуктах, которые есть у нее 
дома. Затем выбирает только те, которые нужны по рецепту и считает их калорийность.
ФОРМАТ ВВОДА
Записи о по продуктах, которые есть у Маши, 
вида <название продукта>: <кол-во белков>, <кол-во жиров>, <кол-во углеводов>. 
Каждая запись вводится с новой строки. Количество белков, жиров и углеводов всегда 
являются целыми числами.
В каждой строке указывается информация только об одном продукте.
Гарантируется, что названия продуктов не повторяются.
Когда записи заканчиваются, на отдельной строке вводится слово "СТОП". 
Далее вводится строка, где через запятую и пробел перечислены продукты,
необходимые для блюда. Также в строке указано, сколько (в штуках) нужно 
каждого продукта.
Гарантируется, что все продукты из рецепта есть в нужном количестве у Маши.
Считаем, что калорийность продукта рассчитывается, 
как 4 * кол-во белков + 9 * кол-во жиров + 4 * кол-во углеводов.
ФОРМАТ ВЫВОДА 
Строки вида "Продукт: <название продукта из рецепта>, 
калорийность: <суммарная калорийность>".
Под суммарной калорийностью подразумевается 
следующее: если калорийность огурчика равна 50, а Маше их нужно 3 штуки, 
то суммарно калорийность будет равна 150. 
Строки должны выводиться в зависимости от количества белков в продукте 
(от меньшего к большему).
Для примера:
Ввод 
Результат
арахис: 187, 378, 28
киви: 189, 72, 222
банан: 156, 782, 875
рыба: 76, 98, 82
СТОП
арахис-2, рыба-4, банан-1 

Продукт: рыба, калорийность: 6056
Продукт: банан, калорийность: 11162
Продукт: арахис, калорийность: 8524

икра: 76, 20, 89
СТОП
икра-10 
Продукт: икра, калорийность: 8400"""

# prods = {}
# name, *calories = input('> ').split()
#
# while name != 'СТОП':
#     name = name[:-1] if name[-1] == ':' else name
#     calories = [int(i[:-1]) if i[-1] == ',' else int(i) for i in calories]
#     prods[name] = calories
#     name, *calories = input('> ').split()
#
# # print(prods)
# prods = sorted(prods.items(), key=lambda x: x[1][0])
# # prods = dict(prods)
# # print(prods)
#
# result = input('>> ').split(', ')
# result = {i.split('-')[0]: int(i.split('-')[1]) for i in result}
# # print(result)
#
# for k, (b, g, u) in prods:
#     if k in result:
#         calories = (b * 4 + 9 * g + 4 * u) * result[k]
#         print(f'Продукт: {k},'
#               f' калорийность: {calories}')

        # print(k, b, g, u)

#
# tp = ((22, 'first'), (33, 'second'), (44, 'third'))
# print(set(tp))
# print(list(tp))
# # d = dict.fromkeys(tp, 'one')
# d = dict(tp)
# print(d)

"""Музыкальные критики составили некоторую подборку песен разных 
исполнителей, для каждой песни известно количество ее прослушиваний
 на стриминговом сервисе. Найдите в подборке исполнителя с наибольшим
  суммарным количеством прослушиваний.
ФОРМАТ ВВОДА
Структурированный текстовый файл music.csv в кодировке utf-8.
 На каждой строке файла записаны имя исполнителя, название песни,
  название жанра и количество прослушиваний. Например,
   "Bruno Mars;Grenade;pop;5648"
Разделителем данных выступает точка с запятой (";").
Гарантируется, что в файле есть как минимум одна строка с данными.
ФОРМАТ ВЫВОДА
Исполнитель, песни которого имеют наибольшее суммарное количество прослушиваний.
Гарантируется, что такой исполнитель только один."""
res = {}
for i in open('music.csv', encoding='utf-8'):
    name, song, style, cnt = i.strip().split(';')
    res[name] = res.get(name, 0) + int(cnt)
    # if name not in res:
    #     res[name] = int(cnt)
    # else:
    #     res[name] += int(cnt)

# mx = 0
# nm = ''
# for k, v in res.items():
#     if v > mx:
#         mx = v
#         nm = k
nm = max(res, key=lambda x: res[x] )
# obj = max(res.items(), key=lambda x: x[1])
# nm = obj[0]

print(nm)