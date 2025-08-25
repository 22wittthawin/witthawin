from tkinter import *
import pyqrcode
import png
from PIL import ImageTk, Image

root = Tk()
root.title("QRCode Generator")
canvas = Canvas(root, width=400, height=500)
canvas.pack()

app_label = Label(root, text="QRCode Generator", font=('Arial', 20, 'bold'))
canvas.create_window(200, 50, window=app_label)

name_label = Label(root, text="ชื่อคิวอาร์โค้ด")
canvas.create_window(200, 100, window=name_label)

name_entry = Entry(root)
canvas.create_window(200, 130, window=name_entry)

link_label = Label(root, text="URL")
canvas.create_window(200, 160, window=link_label)

link_entry = Entry(root)
canvas.create_window(200, 190, window=link_entry)

def generate_qr():
    qr_name = name_entry.get()
    qr_link = link_entry.get()
    
    if qr_name and qr_link:
        qr = pyqrcode.create(qr_link)
        qr.png(f"{qr_name}.png", scale=8)

        img = Image.open(f"{qr_name}.png")
        img = img.resize((200, 200))
        img = ImageTk.PhotoImage(img)

        img_label = Label(root, image=img)
        img_label.image = img 
        canvas.create_window(200, 400, window=img_label)

button = Button(text="สร้างคิวอาร์โค้ด", command=generate_qr)
canvas.create_window(200, 230, window=button)

root.mainloop()