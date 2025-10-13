from tkinter import *

root = Tk()
X = root.winfo_screenwidth()
Y = root.winfo_screenheight()
WIDTH = 300
HEIGHT = 300
root.geometry(f'{WIDTH}x{HEIGHT}+{X // 2 - WIDTH // 2}+'
              f'{Y // 2 - HEIGHT // 2}')
root.title('Бронирование')
frame1 = Frame(root)
frame1.config(bg='light blue')
frame1.pack(pady=15)
top = Label(frame1, text='Бронирование мест на рейс .........',
            bg='light blue')

top.pack()
canvas = Canvas(frame1, width=WIDTH * 2 / 3, height=30)
canvas.pack()
canvas.create_line(10, 10, 50, 10, fill='lime', width=4)
canvas.create_text(30, 20, text='1000')
canvas.create_line(80, 10, 120, 10, fill='#ffff00', width=4)
canvas.create_text(100, 20, text='800')
canvas.create_line(150, 10, 190, 10, fill='#0000ff', width=4)
canvas.create_text(170, 20, text='900')
frame2 = Frame(root)
frame2.pack()

for i in range(3):
    for j in range(3):
        num = i * 3 + j + 1
        if i == 0:
            bgr = 'lime'
        elif i == 1:
            bgr = '#ffff00'
        else:
            bgr = '#0000ff'

        btn = Button(frame2)
        btn.config(text=num, font='arial 20', width=3, bg=bgr)
        btn.grid(row=i, column=j)

root.mainloop()
