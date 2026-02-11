import math
import time

from decorators import execution_time
import random

ls = [20, 30, 40, 50, 90]
# ls = [30, 40, 50, 90, 20]
# temp = ls[0]
# for i in range(len(ls) - 1):
#     ls[i] = ls[i+1]
# ls[-1] = temp
# print(ls)

# for i in range(len(ls) - 1):
#     ls[i], ls[i+1] = ls[i+1], ls[i]
#     print(ls)
#
# ls = [20, 30, 40, 50, 90]
# n = len(ls)
# temp = ls[-1]
# for i in range(n - 1, 0, -1):
#     ls[i] = ls[i - 1]
# ls[0] = temp
# print(ls)
# for i in range(n - 1, 0, -1):
#     ls[i], ls[i - 1] = ls[i - 1], ls[i]
# print(ls)
# x = 10
# y = 55
#
# z = x
# print(f'X = {x}, Y =  {y}')
# x = y
# print(f'X = {x}, Y =  {y}')
# y = z
# print(f'X = {x}, Y =  {y}')
# x, y = y, x
# print(f'X = {x}, Y =  {y}')

l = [9, 8, 7, 6, 4, 5, 1, 2, 3]


# l = [9, 1, 2, 3, 4, 5, 6, 7, 8]

@execution_time
def bubble_sort(arr):
    """ Сортировка пузырьком"""
    cnt = 0
    cnt_all = 0
    n = len(arr)
    for j in range(n - 1):
        for i in range(n - 1 - j):
            cnt_all += 1
            if arr[i] > arr[i + 1]:
                cnt += 1
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print(f'всего итераций - {cnt_all}\nКол-во замен - {cnt}')
    return arr


@execution_time
def selection_sort(x: list):
    """сортировка выбором"""
    n = len(x)
    for i in range(n - 1):
        m = x[i]
        k = i
        for j in range(i + 1, n):
            if x[j] < m:
                m = x[j]
                k = j
        x[i], x[k] = x[k], x[i]
    return x


@execution_time
def insert_sort(x: list):
    """Сортировка вставками"""
    for i in range(1, len(x)):
        if x[i] < x[i - 1]:
            buff = x[i]
            j = i - 1
            while x[j] > buff and j >= 0:
                x[j + 1] = x[j]
                j -= 1
            x[j + 1] = buff
    return x


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        # q = nums[len(nums) // 2]
        q = random.choice(nums)
        l = [n for n in nums if n < q]
        e = [q] * nums.count(q)
        r = [n for n in nums if n > q]
        return quick_sort(l) + e + quick_sort(r)


# l = random.choices(range(1, 1000000), k=5000)
# l1 = l.copy()
# l2 = l.copy()
# l3 = l.copy()
#
# bubble_sort(l)
# selection_sort(l1)
# insert_sort(l2)
# start = time.perf_counter()
# quick_sort(l3)
# stop = time.perf_counter()
# print('Quick_sort -', stop - start)


# l = [3, 2, 4, 1]
#
# q = 2
# l = [1]
# e = [2]
# r = [3, 4]
# ret = [1] + [2] + [3, 4]
# """.............."""
# ret = [1] + [2] + [3] + [4]

nums = [3, 1, 6, 4, 9, 1]
q = 4
# l = []
# for n in nums:
#     if n < q:
#         l.append(n)
# l = [n for n in nums if n < q]
# print(l)
