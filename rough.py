# import tkinter as tk
# from PIL import Image, ImageTk

# # Log in / Sign up Window :-
# def log(root):

#     root.maxsize(1000, 600)
#     root.geometry("1000x600")
#     root.title("Train Booking")

#     # icon image
#     icon = tk.PhotoImage(file = "train_icon.png")
#     root.iconphoto(True, icon)

#     # background image
#     image = Image.open("background.jpg")
#     image = image.resize((1000, 600))
#     bg = ImageTk.PhotoImage(image)

#     bg_label = tk.Label(root, image=bg)
#     bg_label.place(x=0, y=0, relwidth=1, relheight=1)

#     # root frame
#     f1 = tk.Frame(root, bd=1, relief="ridge", width=500, height=550, bg="#ffdab9")
#     f1.place(x=10, y=25)


#     # heading
#     head = tk.Label(f1, text="Log in / Sign up", font="lucida 20 bold", bg="#ffdab9", fg="#001f3f")
#     head.place(x=150, y=20) 

#     # user ID and password input
#     user = tk.Label(f1, text="User Name : ", font="lucida 16 bold", padx=10, pady=5, bg="#ffdab9", fg="#333333")
#     user.place(x=20, y=150)    
#     user_value = tk.StringVar()
#     tk.Entry(f1, textvariable=user_value, font="lucida 16 bold").place(x=180, y=155)

#     passwd = tk.Label(f1, text="Password : ", font="lucida 16 bold", padx=10, pady=5, bg="#ffdab9", fg="#333333")
#     passwd.place(x=20, y=250)
#     passwd_value = tk.StringVar()
#     tk.Entry(f1, textvariable=passwd_value, font="lucida 16 bold", show="*").place(x=180, y=255)

#     loginBtn = tk.Button(f1, text="Login", font="licida 16 bold", padx=20, pady=5, bg="#ff6600", fg="white", activebackground="#e65c00", activeforeground="white")
#     loginBtn.place(x=180, y=320)    

#     tk.Label(f1, text="Don't have an Account?\nCreate one!", font="lucida 16 bold",bg="#ffdab9", fg="#006666").place(x=110, y=400)

#     signBtn = tk.Button(f1, text="Sign in", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="white", activebackground="#e65c00", activeforeground="white")
#     signBtn.place(x= 170, y=480)

#     # keyboard press for login and signin


# # MAIN :-

# root = tk.Tk()
# main = log(root)
# root.mainloop()

import mysql.connector as con

con1 = con.connect(host="localhost", user="root", password="shubham@1234", database="train")
cur1 = con1.cursor()

sql="select * from login"

cur1.execute(sql)
rec = cur1.fetchall()
for i in range(len(rec)):
    print(rec[i][1], rec[i][3])