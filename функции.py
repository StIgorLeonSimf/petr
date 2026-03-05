# def name(nm='Александр') -> str:
#     # print('Привет', nm)
#     return f'Вернула {nm}'
#
#
# def summator(x: int = 0, y: int = 0) -> int:
#     global z
#     z += 200
#     print('func', z)
#     n = x**2 + y**2 + 100
#     return n
#
#
# # name('Андрей')
# # name('Петр')
# # name()
# # name1 = name('Андрей')
# # name1 = name(22)
# # print(name1)
# z = 50000
# print(summator(5, 10))
#
# print('Modul', z)
#
# # область видимости переменных

def is_even(number: int) -> bool:
    return number % 2 == 0
    # if number % 2 == 0:
    #     return True
    # else:
    #     return False


def choce_even(x, y):
    for i in range(x, y + 1):
        if is_even(i):
            print(i, end=' ')


# choce_even(100, 140)
# def sm2(n):
#     if n > 1:
#         sm2(n-1)
#     print(n)
#
#
# def sm1(n):
#     if n > 1:
#         sm2(n-1)
#     print(n)


# def sm(n):
#     if n > 1:
#         sm(n-1)
#     print(n, end=' ')
#
# sm(3)

"""
5! = 1*2*3*4*5 = 5 * 4!
4! = 1*2*3*4   = 4 * 3!
3! = 1*2*3     = 3 * 2!
2! = 1 * 2     = 2 * 1!
1! = 1 
n! = n * (n-1)!
"""

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


# print(fact(2))

"""
0 1 1 2 3 5 8 13 21 34 55
"""
# f1 = 0
# f2 = 1
# res = 0
# for i in range(1, 10):
#     res = f1 + f2
#     f1 = f2
#     f2 = res
# print(res)

# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# # print(fib(10))
# cnt = 1000
# def name(nm):
#     cnt = 0
#     def surname(snm):
#         nonlocal cnt
#         cnt += 1
#         print(cnt, nm, snm)
#     return surname
#
# sur = name('Mary')
# sur('Petrova')
# sur('Ivanova')
# sur('Sidorova')
#
#
# def mult(x, y=1):
#     """Функция умножения двух чисел"""
#     return f'{x} * {y} = {x * y}'
#
#
#
# print(mult.__doc__)
# print(mult(3, 5))

def grad(nm):
    target = f'Привет, {nm}!'
    return target

# print(grad('Иван'))
# print(grad('Петр'))
# print(grad('Андрей'))

# d = {'Math': 'A', 'Chem': 'B', 'Art': 'A'}
# def set_default(dic, k, v):
#     if k not in dic:
#         d[k] = v
#     return d[k]
#
# res = set_default(d,'Num', []).append(1000)
# print(res)
# print(d)

def coffee(name, cost):
    name = name.capitalize()
    drinks = {'Горячий шоколад': 120,
              'Чай': 80,
              'Капучино': 100
              }
    if name in drinks:
        if cost == drinks[name]:
            print(f'Вы заказали {name}')
            return name
        elif cost > drinks[name]:
            dif = cost - drinks[name]
            print(f'Вы заказали {name}')
            return f'{name} и сдача - {dif} руб.'
        else:
            print(f'Вы заказали {name} но оплаты недостаточно')
            return f'{cost} рублей'


hand = coffee('Горячий шоколад', 120)
hand = hand.upper()
print(f'В моей руке есть {hand}')
print()
hand = coffee('капучино', 120)
print(f'В моей руке есть {hand}')
print()
hand = coffee('Чай', 60)
print(f'В моей руке есть {hand}')

# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)


# print(fib(10))

"""
0 1 1 2 3 5 8 13 21 34 55
"""

def fib(n, memo={}):

    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    print(memo)
    return memo[n]

memo = {}
print(fib(4, memo))
# print(memo)