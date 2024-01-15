#def install():

import os
"""
package_name = 'Pillow'
os.system(f'pip install {package_name}')
package_name = 'pyautogui'
os.system(f'pip install {package_name}')
package_name = 'requests'
os.system(f'pip install {package_name}')
"""
import random
from tkinter import*
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from PIL import Image, ImageTk
import PIL.ImageGrab as ImageGrab
import pyautogui
import requests
import webbrowser
import time

package_name = 'Pillow'
os.system(f'pip install {package_name}')


root = Tk()
root.geometry("700x700+700+100")
root.title("Paint")
url = "https://engine.prod.bria-api.com/v1/generation/gaia-v1/text-to-image"

x = 0
y = 0

def start_drag(event):
    global dragging_photo
    dragging_photo = True
    can.start_x = event.x
    can.start_y = event.y

def enter(event):
    print("Іде процес...")
    payload = {
      "prompt": e1.get(),
      "num_results": 1,
      "style": "photo realistic",
      "atmosphere": "realistic",
      "camera": "portrait",
      "medium": "photography",
      "sync": True
    }

    headers = {
      "Content-Type": "application/json",
      "api_token": "#############"
    }

    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    data = str(data)
    if data[9] == "5" and data[10] == "0" and data[11] == "0":
        print("Помилка, спробуйте пізніше")
    #print(data)



def ac():
    global pen_color
    (rgb, hex) = colorchooser.askcolor(title="Виберіть колір")
    color_c = hex
    pen_color = color_c
    Lab1.config(bg = color_c)

    


def k():
    color_c='#%02x%02x%02x' % (sc1.get(), sc2.get(), sc3.get())
    can.config(bg = color_c)

def a(v):
    color_c='#%02x%02x%02x' % (sc1.get(), sc2.get(), sc3.get())
    Lab1.config(bg = color_c)
def clear():
    can.config(bg = "white")
    can.delete("all")
def s(v):
    global pen_size
    pen_size = sc4.get()
def h():
    global pen_color
    color_c='#%02x%02x%02x' % (sc1.get(), sc2.get(), sc3.get())
    pen_color = color_c



    
def paint(event):
        if not dragging_photo:
            x1, y1 = (event.x - pen_size),(event.y - pen_size)
            x2, y2 = (event.x + pen_size), (event.y + pen_size)
            can.create_oval(x1,y1,x2,y2, fill = pen_color, outline = pen_color)


def save():
    root.attributes("-topmost", True)
    file_name = filedialog.asksaveasfilename(defaultextension = ".png")
    x5 = root.winfo_rootx() + can.winfo_x()
    y5 = root.winfo_rooty() + can.winfo_y()
    x6 = x5 + can.winfo_width()
    y6 = y5 + can.winfo_height()
    ImageGrab.grab().crop((x5,y5,x6,y6)).save(file_name)
    messagebox.showinfo("Paint повідомляє", "Картинка збережена як " + str(file_name))
        


def g():
    global pen_color
    pen_color = "white"


def ran():
    global pen_color
    global pen_size
    a = random.randint(1, 255)
    b = random.randint(1, 255)
    c = random.randint(1, 255)
    sc1.set(a)
    sc2.set(b)
    sc3.set(c)
    color_c='#%02x%02x%02x' % (sc1.get(), sc2.get(), sc3.get())
    pen_color = color_c
    pen_size = random.randint(1, 100)
    sc4.set(pen_size)

def ran1():
    for i in range(random.randint(1, 15)):
        k = random.randint(1, 3)

        a = random.randint(1, 255)
        b = random.randint(1, 255)
        c = random.randint(1, 255)
        sc1.set(a)
        sc2.set(b)
        sc3.set(c)
        color_c='#%02x%02x%02x' % (sc1.get(), sc2.get(), sc3.get())
        pen_color = color_c
        if k == 2:
           can.create_line(random.randint(1, 700),
                             random.randint(1, 700),
                             random.randint(1, 700),
                             random.randint(1, 700), fill = pen_color, width = random.randint(6, 18))
        can.create_rectangle(random.randint(1, 700),
                             random.randint(1, 700),
                             random.randint(1, 700),
                             random.randint(1, 700), fill = pen_color, outline = pen_color)

def drag(event):
    global dragging_photo
    if dragging_photo:
        # Обчислюємо різницю між поточною позицією миші та початковою
        dx = event.x - can.start_x
        dy = event.y - can.start_y
        
        # Переміщуємо фото на відстань dx та dy
        can.move(tk.CURRENT, dx, dy)
        
        # Оновлюємо початкову позицію для наступної ітерації
        can.start_x = event.x
        can.start_y = event.y

def o():
    root.attributes("-topmost", False)

    






def ap():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")])
    
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        




        if file_path:
                image = Image.open(file_path)
                photo = ImageTk.PhotoImage(image)
        
                # Створюємо фото на canvas і додаємо його до списку фотографій
                photo_id = can.create_image(0, 0, anchor=tk.NW, image=photo)
                photos.append((photo, photo_id))
        
                # Додаємо обробники подій для переміщення фото
                can.tag_bind(photo_id, "<ButtonPress-1>", start_drag)
                can.tag_bind(photo_id, "<B1-Motion>", drag)
                can.tag_bind(photo_id, "<ButtonRelease-1>", end_drag)

def end_drag(event):
    global dragging_photo
    dragging_photo = False





can = Canvas(bg = "white", width = 640, height = 440)
can.pack()
pen_color = "black"
pen_size = 5

sc1 = Scale(bg = "red", orient = HORIZONTAL, tickinterval = 30, from_=0, to = 255, length = 255, command = a)
sc1.place(x = 10, y = 450)
sc2 = Scale(bg = "green", orient = HORIZONTAL, tickinterval = 30, from_=0, to = 255, length = 255, command = a)
sc2.place(x = 10, y = 510)
sc3 = Scale(bg = "blue", orient = HORIZONTAL, tickinterval = 30, from_=0, to = 255, length = 255,  command = a)
sc3.place(x = 10, y = 570)
sc4 = Scale(orient = HORIZONTAL, tickinterval = 20, from_=0, to = 100, length = 150, command = s, bg = "#b5543c")
sc4.place(x = 300, y = 450)
Lab1 = Label(text = "Колір", bg = "white", width = 5, height = 3)
Lab1.place(x = 460, y = 450)
b1 = Button(text = "Змінити колір тла", command = k, fg = "#e8d243", bg = "#b5543c")
b1.place(x = 300, y = 510)
b2 = Button(text = "Змінити колір пензлика", command = h, fg = "#e8d243", bg = "#b5543c")
b2.place(x = 300, y = 570)
b3 = Button(text = "Очистити", command = clear, fg = "#e8d243", bg = "#b5543c")
b3.place(x = 10, y = 630)
b4 = Button(text = "Зберегти", command = save, fg = "#e8d243", bg = "#b5543c")
b4.place(x = 300, y = 630)
b5 = Button(text = "Гумка", command = g, fg = "#e8d243", bg = "#b5543c")
b5.place(x = 10, y = 660)
b6 = Button(text = "Чистий рандом", command = ran, fg = "#e8d243", bg = "#b5543c")
b6.place(x = 300, y = 660)
b6 = Button(text = "Рандомний малюнок", command = ran1, fg = "#e8d243", bg = "#b5543c")
b6.place(x = 10, y = 660)
b6 = Button(text = "Додати фотографію", command = ap, fg = "#e8d243", bg = "#b5543c")
b6.place(x = 160, y = 630)
e1 = Entry()
e1.place(x = 160, y = 660)
e1.insert(0, "Пишіть англійською!")
b8 = Button(text = "Зручний вибір кольору", fg = "#e8d243", bg = "#b5543c",  command = ac)
b8.place(x = 400, y = 660)




photos = []  # Список для збереження фотографій
dragging_photo = False  # Флаг для переміщення фото
root.configure(bg='#3e5f94')

b7 = Button(text = "Опустити(здатність ставити не на передній план)", fg = "#e8d243", bg = "#b5543c",  command = o)
b7.place(x = 300, y = 600)



can.bind("<B1-Motion>", paint)
root.bind("<Return>", enter)
root.mainloop()









