# import tkinter as tk

# root = tk.Tk()

# root.geometry("400x400")
# root.maxsize(400, 400)
# root.minsize(400, 400)

# canva = tk.Canvas(root, bg = "white", width=300, height=300)
# canva.pack(side="left", expand=True, fill="both")

# vs = tk.Scrollbar(root, orient="vertical", command=canva.yview)
# vs.pack(side="right", fill="y")

# canva.configure(yscrollcommand=vs.set)

# canva.config(scrollregion=(0, 0, 1000, 1000))

# for i in range(20):
#     x=50*i
#     y=50*i
#     canva.create_text(x, y, text="shubham "+str(i))

# root.mainloop()

# from datetime import datetime
# import email
import re

a="Shubham Kumar Sah"

b=r'^[a-zA-Z]'

c="abc.defgmaul.com"

# print(re.search(b, c))

if re.search(b, a):
    print("Yes")
else:
    print("No")
