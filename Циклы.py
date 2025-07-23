# i = 0
# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i, end=' ')

# i = 0
# while i < 10:
#     i += 1
#     if i == 17:
#         break
#     print(i, end=' ')
# else:
#     print('\n OK')

# n = int(input('> '))
# sm = 0
# cnt = 0
# while n != 0:
#     if n % 2 == 0:
#         sm += n
#         cnt += 1
#     n = int(input('> '))
# print(sm, cnt)

""" S = 3 + 2 + 1
    K = 1 + 1 + 1
123 % 10 = 3
    //10 = 12 % 10 = 2
              //10 = 1  % 10 = 1
                        //10 = 0
"""

# n = int(input('> '))
# a = n
# sm = 0
# pr = 1
# k = 0
# while n > 0:
#     m = n % 10
#     sm += m
#     k += 1
#     n //= 10
#
# print(f'В числе "{a}" {k} ц. суммой {sm} ')

# n = int(input('> '))
# res = 0
# while n > 0:
#     m = n % 10
#     res = res * 10 + m
#     n //= 10
# print(res)

# for i in 22, 333, 4:
#     print(i, 'yes')

# print(list(range(10)))  # Start=0, Stop, Step= +1
# for i in range(20, 9, -1):
#     print(i, end='  ')

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f'{j * i:>2}', end=' ')
#     print()

for n in range(100, 200):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n, end=' ')