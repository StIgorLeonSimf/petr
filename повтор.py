"""list"""
# names = ['Sasha', 'Masha', 'Glasha', 'Dasha']
# names.append('Пётр')  # 1
# names.insert(1, 'Grisha')  # 2
# # print(id(names))
# names.extend(('Ivan', 'Dmitry'))  # 3
# # names += ['Ivan', 'Dmitry']
# # names = names + ['Ivan', 'Dmitry']
# # print(id(names))
#
# n = names.pop()
# n1 = names.pop(3)
# names.remove('Sasha')
# print(n, n1)
# print(names)
# for i in range(len(names)):  # 0, 1, 2, 3, 4
#     print(i, names[i], sep=' --- ')
#
# for k, nm in enumerate(names):
#     print(k, nm, sep=' --- ' )

# Множества
"""set"""
l = ['Sasha', 'Sasha', 'Sasha']
st = set(l)
st.add('Zara')  # 1
st.add('Gena')
st.update(['Bob', 'Andre'])  # 2

# n = st.pop()
# print(n)
try:
    st.remove('Zara1')
except Exception as err:
    print('Нет такого значения')
st.discard('Zara')
print(st)
grass = {(1, 2), (2, 2), (3, 3)}
water = {(2, 2), (2, 3), (1, 3)}

print(grass | water)
print(grass & water)
print(grass ^ water)
stt = set()
d = {}
st = {'black', 'white'}
"""dict"""
d = {'black': 'черный', 'white': 'белый'}
d1 = {'black': 'ЧЕРНЫЙ', 'blue': 'синий'}
print(d | d1)

d1['black'] = 'черный'
d1[1] = 100
d1.setdefault(2, 22)
n = d1.setdefault(3, 33)
# d1.update({0: '007', 1: 11})
d1.update([(0, '007'), (1, 11)])

n = d1.pop(0)
n1 = d1.popitem()
print(d1, n, n1)




