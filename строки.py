s = ' ЗдраВствуйте, гости! '
# print(s[0])
# print(s[-1])
# print(s[:12])
# for i in range(len(s)):
#     print(s[i], end='  ')
# print()
# for i in s:
#     print(i, end='  ')
# print()
print(s.count('т'))
s1 = '12345'
print(s1.isdigit())
print(s.isalpha())
print(s.islower())
print(s.isupper())
print(s.startswith(' Здр'))
print(s.endswith('!'))

new = s.lower()
print(new, s)
print(s.upper())
print(s.capitalize())
print(s.title())
# print(s.rjust(80))
print('ljust', s.ljust(80))
# print(s.center(80))
print(s.strip('! '))
print(s.rstrip())
print(s.strip())
print(s.index('т', 18))
print(s.find('т', 7))
print(s.replace('т', 'T', 2).replace(' ', ''))
ls = s.split(', ')
print(ls)
print(', '.join(ls))

s1 = 'aaa bbb ccc ddd '
s2 = '111 222 333 444 '

""" aaa 111 bbb 222 ccc 333 ddd 444 """

s = 'АаБбЯя'
for i in s:
    print(ord(i))