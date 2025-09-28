# n = int(input('введите код для символа: '))
# print(chr(n), )

# print(chr(128512), '😀')
from tkinter import  *


def from16_to_10(num):
    pass

def showsymb(id):
    symb.config(text=f'{chr(id)}')


def showcode(event):
    global codes
    codes = int(code.get())
    showsymb(codes)


def forward():
    global codes
    codes = int(code.get())
    codes += 1
    code.delete(0, END)
    code.insert(END, codes)
    showcode(codes)


def backward():
    global codes
    codes = int(code.get())
    codes -= 1
    code.delete(0, END)
    code.insert(END, codes)

    showcode(codes)


codes = 128512
fcolor = '4ED05D'
print(int(fcolor, 16))
print(f'{int(fcolor, 16) + 1:X}')

root = Tk()
root.geometry('400x250+450+300')
name = Label(root, text='введите код для символа')
name.config(font='Arial 20')
name.pack(pady=5)

code = Entry(root, width=10, font="arial 15", justify='center')
code.pack()
code.insert(END, codes)

symb = Label(root, text=f'{chr(codes)}', font='Arial 50 bold')
symb.config(fg='#4ED05D', bg='#CDF9D8')
symb.pack(pady=5)

forw = Button(root)
forw.config(width=10, font="arial 10", text='Вперед', command=forward)
forw.pack()
backw = Button(root)
backw.config(width=10, font="arial 10", text='Назад', command=backward)
backw.pack(pady=5)
showsymb(codes)

code.bind('<Return>', showcode)
root.mainloop()