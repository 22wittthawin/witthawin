import tkinter as tk

def on_button_click():
    output_text.set("วิธวินท์\n5/8\n22")

window = tk.Tk()
window.title("Simple Tkinter App")
window.geometry("300x200")

output_text = tk.StringVar()

output_label = tk.Label(window, textvariable=output_text, font=("Arial", 14), justify="left")
output_label.pack(pady=20)

button = tk.Button(window, text="XXX", command=on_button_click)
button.pack()

window.mainloop()