import tkinter as tk
from tkinter import ttk
root = tk.Tk()

root.geometry("300x300")

sel = tk.StringVar()
sel.set("Select")

def com():
    value = sel.get()
    print(value)

tk.Button(root, text="Print", command=com).pack(padx=50, pady=50)



cb = ttk.Combobox(root, textvariable=sel, values=("A", "B", "C"))
cb.pack(padx=20, pady=20)

root.mainloop()