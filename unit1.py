from math import sqrt

x = 5  # int
y = 5.45  # float
name = 'Mary'  # str
yes_no = True  # bool (False)

# print(yes_no)
name1 = 'Петр'
name2 = 'Александрович'
names = name1 + ' ' + name2
print(names)
# print(name + str(y))  # конкатенация
print(x, y, name, sep='...', end='****')
print(x, y, name)

# n = input('Введите значение: ')
# n1 = input('Введите значение: ')
# if n.isdigit() and n1.isdigit():
#     n = int(n)
#     n1 = int(n1)
#
# # n = int(n)
# print(' n + n1 =', n + n1)
# print(type(n))


"""
+, -, *, **, /, //, %
"""

print(5 % 2)
print(int(5 / 2))
print(5 // 2)
print(round(33 / 4, 2))
PI = 3.1415926
print(round(PI))

a = 32
b = 46
c = 59
"""
p = (a + b + c) / 2
s = sqrt(p(p-a)(p-b)(p-c))
"""
p = (a + b + c) / 2
s = sqrt(p * (p - a) * (p - b) * (p - c))
print('Площадь = "', round(s, 2), '"', sep='')
f1 = 'Площадь = {:.2f}'.format(s)
f2 = f'Площадь = "{s:.2f}"'
print(f1)
print(f2)

print(31, 18, 79)