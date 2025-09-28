"""dict"""
"""Словарь - неупорядоченный набор пар ключ-значенние, в которых ключ уникален"""
st = set()
d = {}

# ls = ['свинец', 'Золото']
# print(ls[0])
d = {'Pb': 'свинец',
     'Au': 'Золото'
     }

print(d['Pb'])
print(d.get('Pb2', 'своё значение'))

d['Pb'] = 'Свинец'

d[1] = 111
res = d.setdefault(2, 22)
print(res)
print(d)
d.update({4: 44, 1: 11, 3: 33})
print(d)
n = d.pop(2)
n1 = d.popitem()
print(n, n1)
print(d)

print(d.keys())
print(list(d.keys()))
print(list(d))
for k in d:
    print(k, d[k], end='    ')
print()
print(list(d.values()))
for v in d.values():
    print(v, end=' ')
print()
print(list(d.items()))
for k in d.items():
    print(k[0], k[1], end='     ')
print()
for k, v in d.items():
    print(k, v, end='     ')
print()

# l = [22, 333, 22]
# dd = dict.fromkeys(l, 100)
# print(dd)

lst = [('Pb1', 'Свинец1'), ('Au1', 'Золото1'), (11, 111), (44, 444)]
dd = dict(lst)
print(dd)

d = {}
for i in range(10, 20):
    d[i] = i ** 2
print(d)

dd = {i: i ** 2 for i in range(10, 20)}
print(dd)

s = 'aaaaabaaaaaaanaaaaaasssaaaaaaanaaaaaaaaaaafafaaaaajaaaa'

symb = []
cnt = []
d = {}
cnt1 = 0
for i in set(s):
    symb.append(i)
    cnt.append(s.count(i))
    cnt1 += 1
    d[i] = s.count(i)
print(cnt1, d)
print(symb, cnt)
inns = [111111, 222222, 999888]
names = ['Petr', 'Ivan', 'John']
ages = [18, 19, 23]
rost = [169, 165, 177]
for i, j, k, m in zip(inns, names, ages, rost):
    print(i, j, k, m)
    
humans1 = [(111111, 'Petr', 18, 169)]
for i, j, k, l in humans1:
    print(i, j, k, l)

humans = {111111: ['Petr', 18, 169],
          222222: ['Ivan', 19, 165],
          999888: ['John', 23, 177]
          }
for k, v in humans.items():
    print(k, v[0], v[1], v[2])
