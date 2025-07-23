from tkinter import *
from time import strftime
from tkinter import messagebox
import pygame as pg

pg.mixer.init()
pg.mixer.music.load('music.mp3')

root = Tk()
root.geometry('400x250+500+200')
root.config(bg='black')
root.title('Будильник')

time = Label(root, text='00:00:00')
time.config(font='Arial 50', bg='black', fg='lime')
time.pack(pady=15)

alarm = Entry(root, font=('Courier Now', 20), justify='center', width=10)
alarm.pack()

btn_on = Button(root, text='Включить', font=('Courier Now', 10),
                width=10, justify='center')
btn_on.pack(pady=10)
btn_off = Button(root, text='Выключить', font=('Courier Now', 10),
                 width=10, justify='center')
btn_off.pack()

alarm_time = ''


def start(event):
    global alarm_time
    alarm_time = alarm.get().strip()
    messagebox.showinfo('Подтверждение', f'Будильник включен на {alarm_time}!')


def stop(event):
    global alarm_time
    alarm.delete(0, END)
    pg.mixer.music.stop()
    alarm_time = ''
    messagebox.showinfo('Подтверждение', 'Будильник выключен')


def tick():
    global alarm_time
    time_now = strftime('%H:%M:%S')
    if (alarm_time == time_now or alarm_time ==
            strftime('%H:%M') or alarm_time == strftime('H')):
        pg.mixer.music.play()
        alarm_time = ''
    time.config(text=time_now)
    time.after(1000, tick)


tick()

btn_on.bind('<Button-1>', start)
btn_off.bind('<Button-1>', stop)
root.mainloop()
