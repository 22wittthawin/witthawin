import tkinter as tk

full_name = "วิธวินท์ หอมอ่อน"
nickname = "ที"
classroom = "ม.5/8"
study_plan = "วิทย์-คณิต"
kana = "วิศวกรรมศาสตร์"

root = tk.Tk()
root.title("กิจกรรมในชั้นเรียนที่ 7")

label = tk.Label(root, text="", font=("Arial", 30))
label.pack(pady=30)

count = 10

def countdown():
    global count
    if count > 0:
        label.config(text=str(count))
        count -= 1
        root.after(1000, countdown)
    else:
        show_info()

def show_info():
    info = f"""ชื่อ - นามสกุล: {full_name}
ชื่อเล่น: {nickname}
ห้องเรียน: {classroom}
แผนการเรียน: {study_plan}
อยากเรียนคณะ: {kana}"""
    label.config(text=info, font=("Arial", 20), justify="left")

countdown()

root.mainloop()