import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    if length < 8:
        messagebox.showwarning("Uyarı", "Şifre en az 8 karakter uzunluğunda olmalı!")
        return ""
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate():
    try:
        length = int(entry.get())
        password = generate_password(length)
        if password:
            result_label.config(text=f"Oluşturulan Şifre: {password}")
            copy_button.config(state=tk.NORMAL)
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin!")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text").replace("Oluşturulan Şifre: ", ""))
    messagebox.showinfo("Başarılı", "Şifre kopyalandı!")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')


root = tk.Tk()
root.title("Şifre Oluşturucu")


window_width = 300
window_height = 250
center_window(root, window_width, window_height)
root.resizable(False, False)  

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="Şifre uzunluğunu girin (en az 8 karakter):")
label.pack(pady=5)

entry = tk.Entry(frame, width=5)
entry.pack(pady=5)

generate_button = tk.Button(frame, text="Şifre Oluştur", command=generate)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

copy_button = tk.Button(root, text="Kopyala", state=tk.DISABLED, command=copy_to_clipboard)
copy_button.pack(pady=5)

root.mainloop()
