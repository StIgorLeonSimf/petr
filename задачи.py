"""Написать декоратор который будет
отправлять в текстовый файл ошибки в
функции деления """
import random
import time
from datetime import datetime as dt
from math import sqrt


def even_zero(func):
    def wrap(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            if res != round(res):
                raise ValueError('Результат не целое число')
        except ZeroDivisionError as err:
            with open('log.txt', 'a', encoding='utf-8') as f:
                f.write(f'{dt.now().replace(microsecond=0)} Деление на ноль\n')
            return 'Деление на ноль'
        except ValueError as err:
            with open('log.txt', 'a', encoding='utf-8') as f:
                f.write(f'{dt.now().replace(microsecond=0)} {err}\n')
            return err
        else:
            return int(res)

    return wrap


@even_zero
def div():
    x = random.randrange(0, 100, 2)
    y = random.randint(0, 5)
    time.sleep(.7)
    return x / y


# for _ in range(10):
#     print(div())
#     time.sleep(1)

# print(24.0 == 24)
#
# x2, y2 = map(int, input().split())
# x3, y3, r = map(int, input().split())
# count = 0
# for y in range(y3 - r, y3 + r + 1):
#     for x in range(x3 - r, x3 + r + 1):
#         # print(sqrt((x3 - x) ** 2 + (y3 - y) ** 2))
#         if sqrt((x3 - x) ** 2 + (y3 - y) ** 2) <= r:
#             # print(x, y)
#             if 0 <= x <= x2 and 0 <= y <= y2:
#                 count += 1
# print(count)


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = dict1 | dict2
dict3 = dict1.copy()
dict3.update(dict2)


print(dict3)
print(dict3.setdefault('b', 5))
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
world = {}
for i in words:
    # world[i] = world.get(i, 0) + 1
    world[i] = world.setdefault(i, 0) + 1
print(world)