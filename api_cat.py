from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        image_data = BytesIO(resp.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as err:
        print(f'Ошибка {err}')
        return None


root = Tk()
root.title('Cats')
root.geometry('700x550')
label = Label()
label.pack()
url = 'https://cataas.com/cat'
img = load_image(url)
if img:
    label.config(image=img)
    label.image = img

root.mainloop()