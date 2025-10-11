# import mysql.connector as con
# import tkinter as tk

# # con1 = con.connect(host = "localhost", user = "root", password = "shubham@1234", database = "train")
# # cur1 = con1.cursor()

# # sql = "select * from train"
# # cur1.execute(sql)

# # rec = cur1.fetchall()

# # print(rec[1])

# def prt():
#     print("Hello World!")

# root = tk.Tk()
# root.geometry("500x500")

# can = tk.Canvas(root, width=300, height=300, bg="yellow")
# can.pack(pady=50)

# tk.Label(can, text="Hello World").place(x=50, y=50)

# tk.Button(can, text="Click!", command=prt).place(x=50, y=100)

# root.mainloop()

name = "Deoghar - DGHR"

if "DGHR" in name:
    print('Y')
else:
    print('N')