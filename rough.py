import tkinter as tk
from PIL import Image, ImageTk

import mysql.connector as con

con1 = con.connect(host="localhost", user="root", password="shubham@1234", database="train")
cur1 = con1.cursor()

con2 = con.connect(host="localhost", user="root", password="shubham@1234", database="trustbank")
cur2 = con2.cursor()

sql1="select * from login where username = 'Shubham1'"
sql2="select * from cust where acno = 10001"

cur1.execute(sql1)
rec1 = cur1.fetchall()
print(rec1)

cur2.execute(sql2)
rec2 = cur2.fetchall()
print(rec2)