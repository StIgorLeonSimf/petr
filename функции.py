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

print(grad('Иван'))
print(grad('Петр'))
print(grad('Андрей'))
