import asyncio
import os.path

from g4f.client import AsyncClient
# from g4f.Provider import OpenaiChat
import requests
from io import BytesIO
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog as fd

from translate import Translator


async def generate_image_url():
    global name
    client = AsyncClient()
    response = await client.images.generate(
        # prompt="kittes",
        prompt=nm,
        model="imagen-4",
        # provider=OpenaiChat,
        response_format="url"
        # Add any other necessary parameters
    )

    image_url = response.data[0].url
    print(f"Generated image URL: {image_url}")

    return image_url


def load_image(url):
    global img_s
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        image_data = BytesIO(resp.content)
        img_s = Image.open(image_data)
        # if img:
        #     img.save('image1.png')
        return ImageTk.PhotoImage(img_s)
    except Exception as er:
        print(f'Error loading image - {er}')
    return None


def run_mode():
    global img, nm, translator
    nm = name.get().strip()
    nm = translator.translate(nm.capitalize())
    print(nm)
    url = asyncio.run(generate_image_url())
    if url:
        img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img


def save_picture():
    global img_s
    if img_s is None:
        print('Картинка не генерировалась')
        return
    def_name = os.path.basename(name_file)
    fp = fd.asksaveasfilename(
        defaultextension='.png',
        filetypes=[('PNG files', '*.png'), ('All files', '*.*')],
        initialfile=def_name
    )
    if fp:
        img_s.save(fp)
        print(f'Файл записан')


if __name__ == "__main__":
    img_s = None
    name_file = 'Picture1.png'
    translator = Translator(from_lang='ru', to_lang='en')
    root = tk.Tk()
    root.title('Cats')
    root.geometry('850x650')
    name = tk.Entry(root, width=50, font='Arial 15')
    name.insert(0, 'kittens')
    name.pack(pady=10)
    nm = name.get().strip()
    btn = tk.Button(root)
    btn.config(text='Forward', width=10, command=run_mode)
    btn.pack()
    btn_s = tk.Button(root, text='Save', width=10, command=save_picture)
    btn_s.pack()
    label = tk.Label(root)
    label.pack(pady=10)
    url = asyncio.run(generate_image_url())
    if url:
        img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img

    root.mainloop()
