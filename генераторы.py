l = [22, 33, 44, 55]

# def gen():
#     for i in range(22, 56, 11):
#         yield i

def genr():  # функция генератор
    i = 22
    while i <= 55:
        yield i
        i += 11



for i in l:
    print('L', i)


res = genr()
print(res)
for i in res:
    print('F', i)
print()

res1 = []
for i in range(22, 90, 20):
    res1.append(i)
print(res1)
res = [i for i in range(22, 90, 20)]
print(res)
res = (i for i in range(22, 60, 12))  # выражение генератор
print(res)
for i in res:
    print('F', i)

"""итератор это объект у которого есть метод iter()  next()"""

# it = iter(l)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

def full_name(name, last_name):
    return name + " " + last_name

print((lambda name, last_name: name + " " + last_name)('Ivan', 'Ivanov'))
print(full_name('Ivan1', 'Ivanov1'))
