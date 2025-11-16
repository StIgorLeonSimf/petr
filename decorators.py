import random
import time


def decor(func):
    def wrapper():
        print('Before')
        func()
        print('After')

    return wrapper


def in_out(func):
    def wrapper(*args, **kwargs):
        print(f'На входе функции {func.__name__}: {args}, {kwargs}')
        res = func(*args, **kwargs)
        print(f'На выходе функции {func.__name__}: {res}')
        return res
    return wrapper


def execution_time(func):
    def wrap(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        stop = time.perf_counter()
        duration = round(stop - start, 2)
        print(f'Время выполнения функции {func.__name__} - {duration} сек.')

    return wrap


@decor
def proba():
    print('PROBA')


@execution_time
def etalon(n, m):
    print('Эталон начал работу')
    time.sleep(n + m)


@in_out
def sumr(x, y):
    return x + y


# print(__name__)
if __name__ == '__main__':
    # proba()
    # etalon(3, 2)
    res = 134 / sumr(random.randint(10, 1000), random.randint(10, 1000)) * .35
    print(res)
