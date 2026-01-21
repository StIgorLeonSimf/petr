import re
from string import ascii_letters, digits
import random

""" False = False or False or False"""

# def passw():
#     base = set(ascii_letters + digits) - {'o', 'O', '0', 'I', 'l', '1'}
#     base1: str = re.findall(r'[^0oOIl1]', ascii_letters + digits)
#     # print(base)
#     # print(base1)
#     password = ''
#
#     while (not re.search(r'[A-Z]', password)
#            or not re.search(r'[a-z]', password)
#            or not re.search(r'[2-9]', password)):
#         password = ''.join(random.sample(base1, 8))
#     return password
#
# i = 0
# while i < 10:
#     print(passw())
#     i += 1

res = re.match(r'AV', 'AV Video')
print(res)
if re.match(r'AV', ' AV Video'):
    print('Есть совпадение')
else:
    print('Нет совпадений')

try:
    res = re.match(r'AV', 'AV Video').group(0)
    print(res)
except Exception:
    print('Нет совпадений')
res = re.search(r'V', '1 AV Video').group()
res = re.findall(r'V', '1 AV Video')
print(res)
print(len(res))

s = 'Computuer'
res = re.split('u', s, 2)
print(res)
print(s.split('u', 2))
res = re.sub('u', 'U', s, 1)
print(res)
pattern = re.compile(r'V')
res = re.findall(pattern, '1 AV Video')
print(res)

s = ' кот котик кошечка'
print(s.find('кот'))
print('startswith -', s.startswith('кот'))
print('match -', re.match('кот', s))  # s.startswith('кот')
print('search -', re.search('кош', s).group())
print('findall -', re.findall('ко', s))
print('fullmatch -', re.fullmatch(' кот котик кошечка', s))
print('sub -', re.sub('ко', 'KO', s))
print('split -', re.split(' ', s, 2))
# print('compile -', 'AV')

res = re.compile(r'AV')
print('compile -', res)
result = re.search(res, 'Analytics Vidhya AV')
print(result)

"""Спецсимволы
\d - любая цифра
\D - всё что не число
\s - пробелы
\S - все что не пробелы
\w - буква, цифра, нижнее подчеркивание
\W - все что не буква, цифра, нижнее подчеркивание
. - любой символ, кроме '\n' 
^ - символ с начала строки
$ - послений символ в строке
[abc] - любой символ из скобок
[^abc] - кроме любого символа из скобок
a|b - один или другой
\bcлово\b
КВАНТИФИКАТОРЫ
+ - одно или более повторений предшествующего символа
* - ноль или более повторений предшествующего символа
? - ноль или одно повторение предшествующего символа
{n} - n повторений предшествующего символа
{n, m} - от n до m повторений предшествующего символа
{n,} - n или более повторений предшествующего символа
{,n} - менее или n повторений предшествующего символа 

"""
s = 'aa97,_ bba  2#c 31256'
print(re.search(r'\d\d', s).group())
print(re.findall(r'\D', s))
print(re.findall(r'\s', s))
print(re.findall(r'\S', s))
print(re.findall(r'\w', s))
print(re.findall(r'\W', s))
print(re.findall(r'.', s))
print(re.findall(r'^a97', s))
print(re.findall(r'c 3$', s))
print(re.findall(r'[abc]', s))
print(re.findall(r'[^abc]', s))
print(re.findall(r'a|b', s))
print(re.findall(r'(^.+#)', s))
print(re.findall(r'\S+$', s))
print(re.findall(r'\S{1,}$', s))
print(re.findall(r'\bbba\b', s))
print(re.findall(r'\bbb\b', s))
print(re.findall(r'bb', s))

print()
s = 'sdsd 5djdjd12djd-5C'
print(re.findall(r'\d', s))
print(re.findall(r'\d{1,2}', s))
print(re.findall(r'\d+', s))


