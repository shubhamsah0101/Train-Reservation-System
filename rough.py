import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry("300x300")

f = tk.Frame(root)
f.pack(fill="both", expand=True)

c = tk.Canvas(f)
c.pack(side="left", fill="both", expand=True)

sb = tk.Scrollbar(c, orient="vertical", command=c.yview)
sb.pack(side="right", fill="y")

sf = tk.Scrollbar(c)
sf.pack()

# sel = tk.StringVar()
# sel.set("Select")

# def com():
#     value = sel.get()
#     print(value)

# tk.Button(root, text="Print", command=com).pack(padx=50, pady=50)



# cb = ttk.Combobox(root, textvariable=sel, values=("A", "B", "C"))
# cb.pack(padx=20, pady=20)

root.mainloop()

