import math
from tkinter import *


def reduct(res):
    n = res[0]
    d = res[1]
    nod = math.gcd(*res)
    n /= nod
    d /= nod
    return int(n), int(d)


def add(n1, d1, n2, d2):
    if d1 == 0 or d2 == 0:
        return 1, 1
    if d1 != d2:
        n1 *= d2
        n2 *= d1
        n = n1 + n2
        d = d1 * d2

    else:
        n = n1 + n2
        d = d1
    return n, d


def sub(n1, d1, n2, d2):
    if d1 == 0 or d2 == 0:
        return 1, 1
    if d1 != d2:
        n1 *= d2
        n2 *= d1
        n = n1 - n2
        d = d1 * d2
    else:
        n = n1 - n2
        d = d1
    return n, d


def calcul():
    n1 = int(num1.get().strip())
    d1 = int(den1.get().strip())
    n2 = int(num2.get().strip())
    d2 = int(den2.get().strip())

    znak = oper.get().strip()

    if znak == '*':
        res = (lambda n1, d1, n2, d2: (n1 * n2, d1 * d2))(n1, d1, n2, d2)
    elif znak == '/':
        res = (lambda n1, d1, n2, d2: (n1 * d2, d1 * n2))(n1, d1, n2, d2)
    elif znak == '+':
        res = add(n1, d1, n2, d2)

    res = reduct(res)
    if res[0] > res[1]:
        itg = res[0] // res[1]
        n = res[0] % res[1]
        d = res[1]
        integ.config(text=itg)
        num3.config(text=n)
        den3.config(text=d)
    else:
        integ.config(text='   ')
        num3.config(text=res[0])
        den3.config(text=res[1])


root =Tk()
root.title('Калькулятор дробей')
root.geometry('300x200+450+200')
frame = Frame(root)
frame.pack(pady=10)
num1 = Entry(frame)
num1.config(width=3, font='Arial 15', justify='center')
num1.grid(row=0, column=0)
line1 = Label(frame, text='----------', font='Arial 10')
line1.grid(row=1, column=0)
den1 = Entry(frame)
den1.config(width=3, font='Arial 15', justify='center')
den1.grid(row=2, column=0)

oper = Entry(frame)
oper.config(width=1, font='Arial 15', justify='center')
oper.grid(row=1, column=1, padx=5)

num2 = Entry(frame)
num2.config(width=3, font='Arial 15', justify='center')
num2.grid(row=0, column=2)
line2 = Label(frame, text='----------', font='Arial 10')
line2.grid(row=1, column=2)
den2 = Entry(frame)
den2.config(width=3, font='Arial 15', justify='center')
den2.grid(row=2, column=2)

btn = Button(frame, text='=', font='Arial 15', command=calcul)
btn.grid(row=1, column=3, padx=10)

integ = Label(frame)
integ.config(text='   ', font='Arial 20', bg='lightgrey')
integ.grid(row=1, column=4)

num3 = Label(frame)
num3.config(width=3, font='Arial 15', justify='center', bg='lightgrey')
num3.grid(row=0, column=5)
line3 = Label(frame, text='----------', font='Arial 10')
line3.grid(row=1, column=5)
den3 = Label(frame)
den3.config(width=3, font='Arial 15', justify='center', bg='lightgrey')
den3.grid(row=2, column=5)

root.mainloop()

