import json
from tkinter import *


# d = {'black': 'черный',
#      'red': 'красный'
#      }
with open('dict.json', 'r', encoding='utf-8') as fl:
    d = json.load(fl)

# while True:
#     print()
#     word = input('Введите слово для перевода: ')
#     if word in d:
#         print(f'{word} - {d[word]}')
#     elif word == '123':
#         break
#     else:
#         transl = input(f'Введите перевод для слова {word} ')
#         d[word] = transl
#         with open('dict.json', 'w', encoding='utf-8') as fl:
#             json.dump(d, fl)


def add_word(transl=None, inp_transl=None):
    new_word = word.get().strip()
    d[new_word] = transl
    with open('dict.json', 'w', encoding='utf-8') as fl:
        json.dump(d, fl)
    inp_transl.destroy()
    answer.config(text=transl)


def translate(event):
    read_word = word.get().strip()
    if read_word in d:
        answer.config(text=d[read_word])
    else:
        def submit_translation():
            trans = transl.get().strip()
            add_word(trans, inp_transl)
        inp_transl = Toplevel(root)
        inp_transl.title('Введите перевод слова')
        inp_transl.geometry('400x100+600+100')
        transl = Entry(inp_transl, width=30, font='Arial 15',
                       justify='center')
        transl.pack(pady=10)
        button_submit = Button(inp_transl, text="Подтвердить", command=submit_translation)
        button_submit.pack(pady=10)
        inp_transl.wait_window()


root = Tk()
root.title('Словарь')
root.geometry('400x200+400+200')

top = Label(root, text='Введите слово на английском языке')
top.config(font='Arial 15')
top.pack(pady=10)
word = Entry(root, width=30, font='Arial 15', justify='center')
word.pack()

answer = Label(root, text=' ', bg='lightgray', width=30, font='Arial 15')
answer.pack(pady=10)
word.bind('<Return>', translate)

root.mainloop()