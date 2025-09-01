import requests
from bs4 import BeautifulSoup
import tkinter as tk

def get_lottery():
    try:
        url = "https://www.lottery.co.th/small"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        buttons = soup.find_all("button", class_="btn-primary")
        numbers = [btn.text.strip() for btn in buttons if btn.text.strip()]
        
        if numbers:
            result_label.config(text="\n".join(numbers))
        else:
            result_label.config(text="No numbers found.")

    except Exception as e:
        result_label.config(text=f"Error: {e}")

root = tk.Tk()
root.title("หวยออก")
root.geometry("300x400")

btn = tk.Button(root, text="หวยออกไร", command=get_lottery)
btn.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(padx=10, pady=10)

root.mainloop()