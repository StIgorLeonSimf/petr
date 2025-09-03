"""tuple"""

# tp = (22, 55, 33, 55)
# # tp[0] = 222
# print(tp[1])
# print(tp.index(55))
# print(len(tp))
# print(tp.count(55))
# for i in tp:
#     print(i, end=' ')
# print()
# print(tp)
#
# NUMB = 45,
# print(NUMB[0])
# tp1 = tp[:]
# print(id(tp))
# print(id(tp1), type(tp1))
tp = ('login', 'password')
print(tp)
print(id(tp))
passw = input('введите новый пароль: ')
buf = list(tp)
print(buf)
buf[-1] = passw
tp = tuple(buf)
print(tp)
print(id(tp))