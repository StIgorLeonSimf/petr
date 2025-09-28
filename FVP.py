"""map"""

lst = ['22', '33', '44']
# res = [int(i) for i in lst]
# res1 = []
# for i in lst:
#     res1.append(int(i))
# print(lst)
# print(res)
# print(res1)
# res = map(int, lst)
# for i in res:
#     print(1, i)
# for i in res:
#     print(2, i)
# print(res)
# def power(n):
#     return n * n
#
# lst = [22, 33, 44]
# # res = list(map(power, lst))
# res = list(map(lambda n: n * n, lst))
# print(res)
# res = list(map(lambda n: n + n, lst))
ls = [2, 3, 4, 5]
# res = list(map(lambda n, m: n - m, lst, ls))
# res = list(map(lambda n, m: n > m, lst, ls))

"""filter"""

res = list(filter(lambda x: x > 3, ls))
# res = list(filter(lambda x: x % 2 == 0, ls))
res1 = []
for i in ls:
    if i > 3:
        res1.append(i)

res2 = [i for i in ls if i > 3]
print(res)
print(res1)
print(res2)