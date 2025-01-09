import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

def button_click(value):
    if value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

# Создаем окно и стиль
style = Style(theme="darkly")  # Используем темную тему
root = style.master
root.title("калькулятор")
root.geometry("400x600")

# Создаем поле ввода
entry = ttk.Entry(root, font=("Helvetica", 24), justify="right")
entry.pack(pady=20, padx=10, fill="x")

# Определяем цвета и кнопки
buttons = [
    {"text": "7", "color": "#FFFFFF"}, {"text": "8", "color": "#FFFFFF"}, {"text": "9", "color": "#FFFFFF"}, {"text": "/", "color": "#FFFFFF"},
    {"text": "4", "color": "#0000FF"}, {"text": "5", "color": "#0000FF"}, {"text": "6", "color": "#0000FF"}, {"text": "*", "color": "#0000FF"},
    {"text": "1", "color": "#FF0000"}, {"text": "2", "color": "#FF0000"}, {"text": "3", "color": "#FF0000"}, {"text": "-", "color": "#FF0000"},
    {"text": "C", "color": "#FF0000"}, {"text": "0", "color": "#FF0000"}, {"text": "=", "color": "#00FF00"}, {"text": "+", "color": "#FF0000"},
]

# Создаем кнопки с анимацией
frame = ttk.Frame(root)
frame.pack(expand=True, fill="both")

for i, btn in enumerate(buttons):
    button = tk.Button(
        frame,
        text=btn["text"],
        bg=btn["color"],
        fg="black",
        font=("Helvetica", 18),
        relief="flat",
        activebackground="#444",
        activeforeground="white",
        bd=0,
        command=lambda val=btn["text"]: button_click(val)
    )
    button.grid(row=i // 4, column=i % 4, padx=5, pady=5, sticky="nsew")
    frame.grid_rowconfigure(i // 4, weight=1)
    frame.grid_columnconfigure(i % 4, weight=1)

root.mainloop()
