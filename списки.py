"""list"""

"""   0   1   2   3   4    """
l = [22, 33, 44, 55, 99]
"""  -5  -4  -3  -2  -1   """

# l[2] = 444
# l[1:1] = [333, 444, 555]
# print(l)
# l[1] = [333, 444, 555]
# print(l)
# print(l[2])
# print(l[-3])
# print(len(l))
# print(l[2:])
# print(l[2::-1])
# # l[1:3] = [111, 222, 333, 444]
# # l[1:1] = [111, 222, 333, 444]
# print(id(l))
# # l1 = l.copy()
# l1 = l[:]
# l[1] = 333
# print(id(l1))
print(l)
# print(l1)
# print(l[::-1])
l = [22, 33, 44, 55, 44]
print(len(l))
print(l)
print(l.count(44))
l.append(100)  # O(1)
l.insert(1, 200)  # O(n)
print(id(l))
# l.extend([44, 4])
l += [44, 4]
# l = l + [44, 4]
print(id(l))

print(l)
n = l.pop()
n1 = l.pop(1)
print(n, n1)
# while 44 in l:
#     l.remove(44)

print(l.count(44))
print(l.index(44, 5, 7))
print(l)

# l.append(100)  # O(1)
# l.insert(1, 200)  # O(n)
# l.extend([1, 2])
# print(l)

for i in range(len(l)):
    print(i, l[i], end='    ')
print()
cnt = 0
for i in l:
    print(cnt, i, end='    ')
    cnt += 1
print()
for i in enumerate(l):
    print(i[0], i[1], end='    ')
print()
for i, j in enumerate(l, 5):
    print(i, j, end='    ')
print()
# v, *m = 22, 3, 4, 5
# print(v, m)
names = ('Dasha', 'Masha', 'Sasha', 'Glasha', 'Pedro')
age = (12, 13, 11, 12, 22)
marks = (4.5, 4.2, 3.8, 5.0, 4.75)
# names.sort()
for k, i in enumerate(names, 1):
    print(f'{k}. {i}')

for i, j, a in zip(names, age, marks):
    print(f'{i:6} - {j} ср.балл - {a}')
# проверить еnumerate с zip. cделать пронумерованный список




# import math
#
# positive_infinity = math.inf
#
# T = (-273, positive_infinity)
T = (-273, float('inf'))
while T != str(T):
    T = input("Введите значение температуры воды: ")

    if T.isdigit() and T[0] <= T < T[1]:
        T = int(T)
        if T <= 0:
            print("Озеро замерзло")

        elif T > 0 and T < 10:
            print("Ледяная вода")

        elif T >= 10 and T < 15:
            print("Жуть как холодно")

        elif T >= 15 and T < 18:
            print("Прохладно, но можно искупаться")

        elif T >= 18 and T < 24:
            print("кайф")

        elif T >= 24 and T < 30:
            print("Полный кайф")

        elif T >= 30 and T < 36:
            print("Горячая вода")

        elif T >= 36:
            print("Кипяток")

else:
    print("Ошибка ввода данных")