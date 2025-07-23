# if True/False:
'''
>, <, >=, <=, ==, !=
'''

# x = 5
# y = 5
# z = x > y and x >= y and x != y
# z1 = x < y or x <= y or x == y
# # print(z, z1)
#
# if x > y:
#     print('X > Y')
# elif x < y:
#     print('X < Y')
# else:
#     print('X = Y')
#
# h = int(input('Время суток: '))
# if h >= 4 and h < 12:
#     print('Morning')
# elif 12 <= h < 17:
#     print('Day')
# elif 17 <= h < 24:
#     print('Evening')
# elif h >= 0 and h < 4 or h == 24:
#     print('Night')
# else:
#     print('Нет такого времени суток')

color = 'green1'
match color:
    case 'red': print('Stop')
    case 'green': print('GO')
    case 'green1': print('asdfrewq')
    case _: print(color)