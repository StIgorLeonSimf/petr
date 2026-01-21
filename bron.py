from tkinter import *

root = Tk()
X = root.winfo_screenwidth()
Y = root.winfo_screenheight()
WIDTH = 600
HEIGHT = 400
root.geometry(f'{WIDTH}x{HEIGHT}+{X // 2 - WIDTH // 2}+'
              f'{Y // 2 - HEIGHT // 2}')
root.title('Бронирование')
frame1 = Frame(root)
frame1.pack(pady=5)
frame2 = Frame(root)
frame2.pack()

top = Label(frame1, text='Экран')
top.pack(padx=60)
canvas = Canvas(frame1, width=WIDTH - 20, height=60)
canvas.pack(side=LEFT, padx=125)
canvas.create_line(50, 10, 350, 10, fill='light blue', width=8)
canvas.create_line(60, 40, 140, 40, fill='lime', width=4)
canvas.create_text(100, 30, text='600')
canvas.create_line(160, 40, 240, 40, fill='#ffff00', width=4)
canvas.create_text(200, 30, text='500')
canvas.create_line(260, 40, 340, 40, fill='#0000ff', width=4)
canvas.create_text(300, 30, text='400')

row = 10
column = 20
for i in range(row):
    r = Label(frame2, text=f'Ряд №{i + 1} ')
    r.grid(row=i, column=0)
    for j in range(column):
        num = i * column + j + 1
        if i >= 0 and i < 3:
            bgr = 'lime'
        elif i >= 3 and i < 7:
            bgr = '#ffff00'
        else:
            bgr = '#0000ff'

        btn = Button(frame2)
        btn.config(text=j + 1, width=2, bg=bgr)
        btn.grid(row=i, column=j + 1)

root.mainloop()
