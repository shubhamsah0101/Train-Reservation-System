import tkinter as tk
from PIL import Image, ImageTk
import  tkinter.messagebox as tmsg

import mysql.connector as con

con1 = con.connect(host="localhost", user="root", password="shubham@1234", database="train")
cur1 = con1.cursor()

class loginWindow:

    def __init__(self, root):
        
        self.root = root

        # title of App
        self.root.title("Log In")

        # geometry of window
        self.root.maxsize(1000, 600)
        self.root.minsize(1000, 600)
        self.root.geometry("1000x600")

        # icon 
        icon = tk.PhotoImage(file="train_icon.png")
        self.root.iconphoto(True, icon)

        # background image
        image=Image.open("background.jpg")
        image=image.resize((1000, 600))
        self.bg=ImageTk.PhotoImage(image)
        bg_label=tk.Label(root, image=self.bg)
        bg_label.place(x=0, y=0, relheight=1, relwidth=1)

        # root frame
        f1=tk.Frame(root, bd=1, relief="ridge", width=500, height=550, bg="#ffdab9")
        f1.place(x=10, y=25)

        head=tk.Label(f1, text="Log in/ Sign Up", font="lucida 16 bold", bg="#ffdab9", fg="#001f3f")
        head.place(x=150, y=20)

        # user id
        tk.Label(f1, text="User Name : ", font="lucida 16 bold", padx=10, pady=5, bg="#ffdab9", fg="#333333").place(x=20, y=150)
        self.user=tk.Entry(f1, font="lucida 14 bold")
        self.user.place(x=180, y=155)

        # password
        tk.Label(f1, text="Password : ", font="lucida 14 bold", padx=10, pady=5, bg="#ffdab9", fg="#333333").place(x=20, y=250)
        self.password=tk.Entry(f1, font="lucida 14 bold", show="*")
        self.password.place(x=180, y=255)

        # log in button
        loginBtn = tk.Button(f1, text="Log in", font="licida 16 bold", padx=20, pady=5, bg="#ff6600", fg="white", activebackground="#e65c00", activeforeground="white", command=self.login)
        loginBtn.place(x=180, y=320)

        # sign in button
        tk.Label(f1, text="Don't have an Account?\nCreate one!", font="lucida 16 bold",bg="#ffdab9", fg="#006666").place(x=110, y=400)

        signinBtn=tk.Button(f1, text="Sign up", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="white", activebackground="#e65c00", activeforeground="white", command=self.signup)
        signinBtn.place(x=170, y=480)

        # Press 'Enter' key to login from keyboard
        loginBtn.bind("<Return>", self.login)

        # Press 'Enter' key to signin from keyboard
        signinBtn.bind("<Return>", self.signup)
        

    # Login button
    def login(self, event=None):

        # access of user id and password
        ur = self.user.get()
        pwd = self.password.get()

        sql="select * from login"
        cur1.execute(sql)
        rec = cur1.fetchall()
        for i in range(len(rec)):
            u=rec[i][1]
            p=rec[i][3]
            if ur == "" or pwd == "":
                tmsg.showerror("ERROR","Please Enter Correct Input.")
                break
            elif ur == u:
                if pwd == p:
                    # menu window...
                    print("Login Successfully...")
                    break
                else:
                    tmsg.showerror("ERROR","Invalid Password! Try Again...")
                    break
        else:
            tmsg.showerror("ERROR","Invalid Username! Try Again...")

    def signup(self, event=None):

        self.root.destroy()  # closing Login Window

        # creating Signup Window
        self.sign=tk.Tk()

        self.sign.geometry("600x600")
        self.sign.maxsize(600, 600)
        self.sign.minsize(600, 600)
        self.sign.title("Sign Up")
        self.sign.config(bg="#ffdab9")

        # heading
        tk.Label(text="Create Your Account",  font="lucida 20 bold", bg="#ffdab9", fg="#001f3f").place(relx=0.5, y=50, anchor="center")

        # user details entry
        labels = ["Username", "Full Name", "Password", "Confirm Password", "Email", "Mobile", "Age", "Pin Code"]
        self.entry = {}
        yposL = 100
        yposE = 105

        for label in labels:
            tk.Label(self.sign, text=label+" :", font="lucida 16 bold", padx=10, pady=5, bg="#ffdab9", fg="#333333").place(x=50, y=yposL)
            if "Password" in label:     # to hide password
                ent = tk.Entry(self.sign, font="lucida 16 bold", show="*")
            else:
                ent = tk.Entry(self.sign, font="lucida 16 bold")
            ent.place(x=300, y=yposE)
            self.entry[label] = ent
            yposL += 50
            yposE += 50

        signBtn=tk.Button(self.sign, text="Sign up", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="white", activebackground="#e65c00", activeforeground="white", command=self.save)
        signBtn.place(relx=0.5, y=550, anchor="center")

        # Press 'Enter' key to signin from keyboard
        signBtn.bind("<Return>", self.save)


    # save user info in database
    def save(self, event=None):         
        
        # obtaining all the user data to store in database
        uname = self.entry["Username"].get()
        fname = self.entry["Full Name"].get()
        pwd = self.entry["Password"].get()
        cpwd = self.entry["Confirm Password"].get()
        email = self.entry["Email"].get()
        mobile = self.entry["Mobile"].get()
        age = self.entry["Age"].get()
        pin = self.entry["Pin Code"].get()

        if not uname or not fname or not pwd or not cpwd or not email or not mobile or not age or not pin:
            tmsg.showerror("ERROR","Please fill all the required fields.")
            return
        if pwd != cpwd:
            tmsg.showerror("ERROR","Password do not match.\n\nTry Again")
            return
        try:
            sql="""insert into login(username, fullname, pass, email, mobile, age, city_pin) values(%s, %s, %s, %s, %s, %s, %s)"""
            values = (uname, fname, pwd, email, mobile, age, pin)
            cur1.execute(sql, values)
            con1.commit()
            tmsg.showinfo("Success","Account Created Successfully")
            self.sign.destroy()
        except Exception as e:
            tmsg.showerror("DATABASE ERROR",str(e))

        root = tk.Tk()
        loginWindow(root)
        root.mainloop()

        
        








        





# main

root = tk.Tk()
app = loginWindow(root)
# app.signup()
root.mainloop()