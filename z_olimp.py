from math import sqrt


def point_in_rectangle(x3, y3, x1, y1, x2, y2):
    return (x1 <= x3 <= x2) and (y1 <= y3 <= y2)


x1, y1, x2, y2 = map(int, input().split())
x3, y3, r = map(int, input().split())

count = 0

for y in range(y3 - r, y3 + r + 1):
    for x in range(x3 - r, x3 + r + 1):
        if sqrt((x - x3)**2 + (y - y3)**2) <= r:
            if point_in_rectangle(x, y, x1, y1, x2, y2):
                count += 1

print(count)