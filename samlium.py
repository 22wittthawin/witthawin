from tkinter import *

root = Tk()
root.title("โปรแกรมคำนวณพื้นที่สามเหลี่ยม")
root.geometry("300x300")

def calculate_area():
    try:
        base = float(entry_base.get())
        height = float(entry_height.get())
        area = 0.5 * base * height
        result_label.config(text=f"พื้นที่ = {area:.2f} ตารางหน่วย")
    except ValueError:
        result_label.config(text="กรุณากรอกตัวเลขให้ถูกต้อง")

title_label = Label(root, text="คำนวณพื้นที่สามเหลี่ยม", font=('Arial', 16))
title_label.pack(pady=10)

label_base = Label(root, text="ความยาวฐาน:")
label_base.pack()
entry_base = Entry(root)
entry_base.pack()

label_height = Label(root, text="ความสูง:")
label_height.pack()
entry_height = Entry(root)
entry_height.pack()

calc_button = Button(root, text="คำนวณ", command=calculate_area)
calc_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
