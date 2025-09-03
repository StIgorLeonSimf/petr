from datetime import datetime, date, time  # , timedelta

# d = date(2024, 7, 14)
# print(d, type(d))
t = time(10, 25, 33)
# print(t, type(t))
# # dt = d + t - нельзя
# dt = datetime.combine(d, t)
# print(dt, type(dt))
# dn = date.today()
# print(dn)
# dn = date.today().year
# print(dn)
# dn = date.today().month
# print(dn)
# dn = date.today().day
# print(dn)
# print(f'Сегодня {(date.today().year - 1) // 100 + 1} век.')
# dtn = datetime.now()
# print(dtn)
# dtutc = datetime.utcnow()
# print(dtutc)
# print(dtn.strftime('%A %d %B %y  %I:%M %p'))
# print(dtn.strftime('%A %d.%m.%Y  %H:%M:%S'))
# print(dtn.strftime('%A %d.%m.%Y  %X'))
# print(dtn.weekday())
# dday = dtn.isoweekday()
# # if dday == 1:
# #     print('Пн')
# wd = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
# dday = dtn.weekday()
# print(wd[dday])

"""Кол-во дней до дня рождения"""
bd = input('Введите дату рождения (дд.мм.гггг): ')
bd = datetime.strptime(bd, '%d.%m.%Y').date()
dn = date.today()
duration = dn - bd
print(f'Вами прожито в этом мире - {duration.days} дней!')
year_n = dn.year
bd = bd.replace(year=year_n)
if bd < dn:
    bd = bd.replace(year=year_n + 1)
duration = bd - dn
print(f'До дня рождения осталось - {duration.days} дней!')