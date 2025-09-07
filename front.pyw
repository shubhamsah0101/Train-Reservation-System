import tkinter as tk
from PIL import Image, ImageTk
import  tkinter.messagebox as tmsg

import mysql.connector as con

con1 = con.connect(host="localhost", user="root", password="shubham@1234", database="train")
cur1 = con1.cursor()

# class for Login/Signup window
class loginWindow:

    # login/signin window
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

        head=tk.Label(f1, text="Log in/ Sign Up", font="lucida 20 bold", bg="#ffdab9", fg="#001f3f")
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
        loginBtn = tk.Button(f1, text="Log in", font="licida 16 bold", padx=20, pady=5, bg="#ff6600", fg="white", activebackground="#e65c00", activeforeground="white", cursor="hand2", command=self.login)
        loginBtn.place(x=180, y=320)

        # sign in button
        tk.Label(f1, text="Don't have an Account?\nCreate one!", font="lucida 16 bold",bg="#ffdab9", fg="#006666").place(x=110, y=400)

        signinBtn=tk.Button(f1, text="Sign up", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="white", activebackground="#e65c00", activeforeground="white", cursor="hand2", command=self.signup)
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
            u=rec[i][2]
            p=rec[i][11]
            if ur == "" or pwd == "":
                tmsg.showwarning("Incomplete","Please Enter Correct Input.")
                break
            elif ur == u:
                if pwd == p:
                    # tmsg.showinfo("LOGIN","Log in Successfully")
                    self.root.destroy()     # clase login window
                    # opening main window
                    new_root = tk.Tk()
                    mainWindow(new_root, ur)
                    new_root.mainloop()
                    break
                else:
                    tmsg.showerror("ERROR","Invalid Password! Try Again...")
                    break
        else:
            tmsg.showerror("ERROR","Invalid Username! Try Again...")

    # Signin button
    def signup(self, event=None):

        self.root.destroy()  # closing Login Window

        # creating Signup Window
        self.sign=tk.Tk()

        self.sign.geometry("1250x600")
        self.sign.maxsize(1250, 600)
        self.sign.minsize(1250, 600)
        self.sign.title("Sign Up")
        self.sign.config(bg="#ffdab9")

        fr = tk.Frame(self.sign, relief="ridge", width=1100, height=500, bg="#ffdab9")
        fr.place(x=50, y=60)

        # heading
        tk.Label(self.sign,text="Create Your Account",  font="lucida 20 underline", bg="#ffdab9", fg="#001f3f").place(relx=0.5, rely=0.05, anchor="center")

        # user details entry
        labels1 = ["Full Name", "Username", "Gender (M/F)", "Date Of Birth (YYYY-MM-DD)", "Address", "PIN CODE"]
        self.entry1 = {}

        i = 1
        for label in labels1:
            tk.Label(fr, text=label+" :", font="lucida 16 bold", padx=10, pady=5, bg="#ffdab9", fg="#333333").grid(row=i, column=0, padx=10, pady=20)
            ent = tk.Entry(fr, font="lucida 16 bold")
            ent.grid(row=i, column=1, padx=10, pady=20)
            self.entry1[label] = ent
            i += 1

        labels2 = ["City", "State", "Mobile", "Email", "Password", "Confirm Password"]
        self.entry2 = {}

        i = 1
        for label in labels2:
            tk.Label(fr, text=label+" :", font="lucida 16 bold", padx=10, pady=5, bg="#ffdab9", fg="#333333").grid(row=i, column=2, padx=10, pady=20)
            ent = tk.Entry(fr, font="lucida 16 bold")
            ent.grid(row=i, column=3, padx=10, pady=20)
            self.entry2[label] = ent
            i += 1  

        # sign in button (save user data into database)
        signBtn=tk.Button(self.sign, text="Sign up", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="white", activebackground="#e65c00", activeforeground="white", cursor="hand2", command=self.save)
        signBtn.place(relx=0.5, rely=0.93, anchor="center")

        # Press 'Enter' key to signin from keyboard
        signBtn.bind("<Return>", self.save)

        # back button
        backBtn=tk.Button(self.sign, text="Back", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="white", activebackground="#e65c00", activeforeground="white", cursor="hand2", command=self.back)
        backBtn.place(x=10, y=10)

    # back to login page
    def back(self):
        self.sign.destroy()
        bk = tk.Tk()
        loginWindow(bk)
        bk.mainloop()

    # save user info in database
    def save(self, event=None):         
        
        # obtaining all the user data to store in database
        fname = self.entry1["Full Name"].get()        
        uname = self.entry1["Username"].get()
        gender = self.entry1["Gender (M/F)"].get()
        dob = self.entry1["Date Of Birth (YYYY-MM-DD)"].get()
        address = self.entry1["Address"].get()
        pincode = self.entry1["PIN CODE"].get()
        city = self.entry2["City"].get()
        state = self.entry2["State"].get()
        mob = self.entry2["Mobile"].get()
        mail = self.entry2["Email"].get()
        pwd = self.entry2["Password"].get()
        cpwd = self.entry2["Confirm Password"].get()
        
        if not fname or not uname or not gender or not dob or not address or not pincode or not city or not state or not mob or not mail or not pwd or not cpwd:
            tmsg.showwarning("Incomplete","Please fill all the required fields.")
            return
        if pwd != cpwd:
            tmsg.showerror("ERROR","Password do not match.\n\nTry Again")
            return
        try:
            sql="""insert into login(fullname, username, gender, dob, address, pin, city, state, mobile, email, pwd)
                   values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (fname, uname, gender, dob, address, pincode, city, state, mob, mail, pwd)
            cur1.execute(sql, values)
            con1.commit()
            tmsg.showinfo("Success","Account Created Successfully")
            self.sign.destroy()
        except Exception as e:
            tmsg.showerror("DATABASE ERROR",str(e))

        root = tk.Tk()
        loginWindow(root)
        root.mainloop()

# class for main window
class mainWindow:

    # Menu Display
    def __init__(self, root, username):
        
        self.root = root

        # title
        self.root.title("Main Menu")

        # geometry of window
        self.root.geometry("1200x750")
        self.root.maxsize(1200, 750)
        self.root.minsize(1200, 750)
        self.root.config(bg="#fff5e6")

        # icon
        icon = tk.PhotoImage(file="train_icon.png")
        self.root.iconphoto(True, icon)

        # greeting
        tk.Label(self.root, text="Welcome, {}".format(username), font="lucida 20 bold", background="#fff5e6").place(x=460, y=10)


        # FRAMES 

        # menu frame
        f1 = tk.Frame(self.root, bd=1, relief="ridge", width=1180, height=63, background="#003366")
        f1.place(x=10, y=80)

        # frame for displaying menu option
        self.f2 = tk.Frame(self.root, bd=1, relief="ridge", width=1180, height=540, background="#ffdab9")
        self.f2.place(x=10, y=170)


        # BUTTONS

        # my account
        myBtn = tk.Button(self.root, text="MY ACCOUNT", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="#002147", activebackground="#e65c00", activeforeground="white", 
        cursor="hand2", command=self.account)
        myBtn.place(x=10, y=15)

        # log out
        logoutBtn = tk.Button(self.root, text="LOG OUT", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="#002147", activebackground="#e65c00", activeforeground="white", 
        cursor="hand2", command=self.logout)
        logoutBtn.place(x=1040, y=15)

        # button for book ticket
        bookBtn = tk.Button(f1, text="BOOK TICKETS", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="#002147", activebackground="#e65c00", activeforeground="white", 
        cursor="hand2", command=self.bt)
        bookBtn.grid(row=1, column=1, padx=10, pady=10)

        # button for cancel ticket
        cancelBtn = tk.Button(f1, text="CANCEL TICKETS", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="#002147", activebackground="#e65c00", activeforeground="white", 
        cursor="hand2")
        cancelBtn.grid(row=1, column=2, padx=10, pady=10)

        # button for PNR status
        pnrBtn = tk.Button(f1, text="PNR STATUS", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="#002147", activebackground="#e65c00", activeforeground="white", 
        cursor="hand2")
        pnrBtn.grid(row=1, column=3, padx=10, pady=10)

        # button for train schedule
        scheduleBtn = tk.Button(f1, text="TRAIN SCHEDULE", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="#002147", activebackground="#e65c00", activeforeground="white", 
        cursor="hand2")
        scheduleBtn.grid(row=1, column=4, padx=10, pady=10)

        # button for track train 
        trackBtn = tk.Button(f1, text="TRACK TRAIN", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="#002147", activebackground="#e65c00", activeforeground="white", 
        cursor="hand2")
        trackBtn.grid(row=1, column=5, padx=10, pady=10)


    # COMMAND FOR EACH BUTTON

    # my account button
    def account(self):
        
        self.acc = tk.Toplevel(self.root)

        # geometry
        self.acc.geometry("1000x700")
        self.acc.maxsize(1000, 700)
        self.acc.minsize(1000, 700)
        self.acc.config(background="#fff5e6")
        self.acc.title("PROFILE")

        tk.Label(self.acc, text="MY PROFILE", font="lucida 20 underline", background="#fff5e6").place(relx=0.5, rely=0.05, anchor="center")

    # log out button
    def logout(self):

        # destroy main menu
        self.root.destroy()

        # opening login window
        log = tk.Tk()
        loginWindow(log)
        log.mainloop()

    # Booking Button
    def bt(self):

        tk.Label(self.f2, text="BOOK TICKET", font="lucida 20 underline", background="#ffdab9").place(x=470, y=10)

        pass

        



# testing

root = tk.Tk()
app = loginWindow(root)
# app.signup()
# app = mainWindow(root, "Shubham")                                     
root.mainloop()