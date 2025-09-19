# modules for Python GUI
import tkinter as tk
from PIL import Image, ImageTk
import  tkinter.messagebox as tmsg
from tkcalendar import DateEntry
from datetime import datetime
import re # to check email formate

# MySQL Connection
import mysql.connector as con



# Database connection and data transfer and retrival
# con1 = con.connect(host="localhost", user="root", password="shubham@1234", database="train")
# cur1 = con1.cursor()



# class for Login/Signup window
class loginWindow:

    def getDB(self):
        con1 = con.connect(host="localhost", user="root", password="shubham@1234", database="train")
        return con1, con1.cursor()

    # login/signup window
    def __init__(self, root):
        
        self.root = root

        # title of App
        self.root.title("Log In")

        # geometry of window
        self.root.maxsize(1000, 600)
        self.root.minsize(1000, 600)
        self.root.geometry("1000x600")

        # icon for every window
        icon = tk.PhotoImage(file="train_icon.png")
        self.root.iconphoto(True, icon)

        # background image of login window
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
        loginBtn.bind("<Return>", self.login)

        # sign in button
        tk.Label(f1, text="Don't have an Account?\nCreate one!", font="lucida 16 bold",bg="#ffdab9", fg="#006666").place(x=110, y=400)

        # sign up button
        signinBtn=tk.Button(f1, text="Sign up", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="white", activebackground="#e65c00", activeforeground="white", cursor="hand2", command=self.signup)
        signinBtn.place(x=170, y=480)
        signinBtn.bind("<Return>", self.signup)

        
    # Login button event
    def login(self, event=None):

        # access of user id and password
        ur = self.user.get()
        pwd = self.password.get()

        # obtaining username and password from database for user verification
        con1, cur1 = self.getDB()
        sql = "SELECT username, pwd FROM login WHERE username = %s"
        cur1.execute(sql, (ur,))
        rec = cur1.fetchone()
        # print(ur, pwd, rec)
        # cur1.close()
        con1.close()

        if not ur or not pwd:
            tmsg.showwarning("Incomplete", "Please Enter both Username and Password")
        elif rec is None:
            tmsg.showerror("ERROR", "Invalid Username. TRY AGAIN...")
        elif pwd == rec[1]:
            self.root.destroy() 
            new_root = tk.Tk()
            mainWindow(new_root, ur)
            new_root.mainloop()
        else:
            tmsg.showerror("ERROR", "Invalid Password. TRY AGAIN...")

        
    # Signin button event
    def signup(self, event=None):

        self.root.destroy()  # closing Login Window

        # creating Signup Window
        self.sign=tk.Tk()

        self.sign.geometry("1250x600")
        self.sign.maxsize(1250, 600)
        self.sign.minsize(1250, 600)
        self.sign.title("Sign Up")
        self.sign.config(bg="#ffdab9")

        # background frame 
        fr = tk.Frame(self.sign, relief="ridge", width=1100, height=500, bg="#ffdab9")
        fr.place(x=50, y=60)

        # heading
        tk.Label(self.sign,text="Create Your Account",  font="lucida 20 underline", bg="#ffdab9", fg="#001f3f").place(relx=0.5, rely=0.05, anchor="center")

        # user details entry
        labels1 = ["Full Name", "Username", "Gender", "Date Of Birth", "Address", "PIN CODE"]
        self.entry1 = {}

        i = 1
        for label in labels1:
            tk.Label(fr, text=label+" :", font="lucida 16 bold", padx=10, pady=5, bg="#ffdab9", fg="#333333").grid(row=i, column=0, padx=10, pady=20)
            
            if label == "Gender":
                self.genderVar = tk.StringVar(value="M")

                male = tk.Radiobutton(fr, text="MALE", variable=self.genderVar, value="M", font="lucida 16 bold", bg="#ffdab9", fg="#333333",  activebackground="#ffdab9")
                male.place(x=200, y=180)

                female = tk.Radiobutton(fr, text="FEMALE", variable=self.genderVar, value="F", font="lucida 16 bold", bg="#ffdab9", fg="#333333", activebackground="#ffdab9")
                female.place(x=320, y=180)

                self.entry1[label] = self.genderVar

            elif label == "Date Of Birth":
                self.d = DateEntry(fr, width=10, font="lucida 18 bold", date_pattern="yyyy-mm-dd")
                self.d.place(x=220, y=255)

            else:
                ent = tk.Entry(fr, font="lucida 16 bold")
                ent.grid(row=i, column=1, padx=10, pady=20)
                self.entry1[label] = ent

            i += 1

        labels2 = ["City", "State", "Mobile", "Email", "Password", "Confirm Password"]
        self.entry2 = {}

        i = 1
        for label in labels2:
            tk.Label(fr, text=label+" :", font="lucida 16 bold", padx=10, pady=5, bg="#ffdab9", fg="#333333").grid(row=i, column=2, padx=10, pady=20)
            if label == "Password" or label == "Confirm Password":
                ent = tk.Entry(fr, font="lucida 16 bold", show="*")
            else:
                ent = tk.Entry(fr, font="lucida 16 bold")
            ent.grid(row=i, column=3, padx=10, pady=20)
            self.entry2[label] = ent
            i += 1  

        # sign in button (save user data into database)
        signBtn=tk.Button(self.sign, text="Sign up", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="white", activebackground="#e65c00", activeforeground="white", cursor="hand2", command=self.save)
        signBtn.place(relx=0.5, rely=0.93, anchor="center")
        signBtn.bind("<Return>", self.save)

        # back(to login page) button
        backBtn=tk.Button(self.sign, text="Back", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="white", activebackground="#e65c00", activeforeground="white", cursor="  hand2", command=self.back)
        backBtn.place(x=10, y=10)
        backBtn.bind("<Return>", self.back)


    # back to login page
    def back(self, event=None):

        # closing sign up window
        self.sign.destroy()     

        # opening log in window
        bk = tk.Tk()            
        loginWindow(bk)
        bk.mainloop()


    # save user info in database
    def save(self, event=None):         
        
        # obtaining all the user data to store in database
        fname   = self.entry1["Full Name"].get()        
        uname   = self.entry1["Username"].get()
        gender  = self.entry1["Gender"].get()
        dob     = self.d.get()
        address = self.entry1["Address"].get()
        pincode = self.entry1["PIN CODE"].get()
        city    = self.entry2["City"].get()
        state   = self.entry2["State"].get()
        mob     = self.entry2["Mobile"].get()
        mail    = self.entry2["Email"].get()
        pwd     = self.entry2["Password"].get()
        cpwd    = self.entry2["Confirm Password"].get()
        
        # check empty fields
        if not fname or not uname or not gender or not dob or not address or not pincode or not city or not state or not mob or not mail or not pwd or not cpwd:
            tmsg.showwarning("Incomplete","Please fill all the required fields.")
            return
        
        # check full name
        # fp = r'^[a-z A-Z]'   # full name pattern
        if not re.search(r'[A-Za-z ]{1,50}', fname):
            tmsg.showerror("Invalid E-mail", "User Name should have only Characters (Uppercase and Lower case)")
            return
        
        # check user name
        if not (uname.isalnum()) or len(str(uname)) > 50:
            tmsg.showerror("Invalid Formate", "User Name should have only Characters (Uppercase and Lower case) and Numbers (0-9)")
            return
        
        # check gender
        if len(str(gender)) != 1 or gender not in ['M', 'F', 'm', 'f']:
            tmsg.showerror("Invalid Formate", "Gender Should be M (MALE) or F (FEMALE)")
            return
        
        # check dob 
        try:
            datetime.strptime(dob, "%Y-%m-%d")
        except ValueError as v:
            tmsg.showerror("Invalid Formate", "Invalid Date")
            return
        
        # check address
        if len(str(address)) > 50:
            tmsg.showerror("Invalid Formate", "Address should have only Characters (Uppercase and Lower case), Numbers (0-9)")
            return
        
        # check pin code
        if not str(pincode).isnumeric() or len(str(pincode)) != 6:
            tmsg.showerror("Invalid Formate", "PIN CODE should have numbers (0-9) and of 6-digits.")
            return
        
        # check city
        if not str(city).isalpha() or len(str(city)) > 50:
            tmsg.showerror("Invalid Formate", "City should contain only Characters(Uppercase and Lower case)")
            return
        
        # check state
        if not str(state).isalpha() or len(str(state)) > 50:
            tmsg.showerror("Invalid Formate", "State should contain only Characters(Uppercase and Lower case)")
            return
        
        # check mobile
        if not str(mob).isnumeric() or len(str(mob)) != 10:
            tmsg.showerror("Invalid Formate", "Mobile Number should have numbers (0-9) and of 10-digits.")
            return
        
        # check email
        ep = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'  # email pattern
        if not re.search(ep, mail):
            tmsg.showerror("Invalid E-mail", "E-mail address should be like 'example.one@mail.com'")
            return
        
        if len(pwd) < 8:
            tmsg.showerror("Password Length", "Password should be at least 8 characters long.")
            return
    
        if pwd != cpwd:
            tmsg.showerror("ERROR","Password do not match.\n\nTry Again")
            return
        
        try:
            cur1, con1 = self.getDB()
            sql="""insert into login(fullname, username, gender, dob, address, pin, city, state, mobile, email, pwd)
                   values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (fname, uname, gender, dob, address, pincode, city, state, mob, mail, pwd)
            cur1.execute(sql, values)
            con1.commit()
            con1.close()
            tmsg.showinfo("Success","Account Created Successfully")
            self.sign.destroy()
        except Exception as e:
            tmsg.showerror("DATABASE ERROR",str(e))

        root = tk.Tk()
        loginWindow(root)
        root.mainloop()


# class for My Profile
class profile:

    def __init__(self, parent, username):
        
        self.parent = parent
        self.acc = tk.Toplevel(parent)

        # get username for SQL query
        self.username = username

        # geometry
        self.acc.geometry("965x650")
        self.acc.maxsize(965, 650)
        self.acc.minsize(965, 650)    
        self.acc.config(background="#fff5e6")
        self.acc.title("PROFILE")

        tk.Label(self.acc, text="MY PROFILE", font="lucida 20 underline", background="#fff5e6").place(relx=0.5, rely=0.05, anchor="center")

        # frame for data display
        self.f1 = tk.Frame(self.acc, relief="ridge", bd=1, background="#ffdab9", height=350, width=940) 
        self.f1.place(x=10, y=100)

        # SQL query to get user data
        con1, cur1 = loginWindow.getDB(self)
        sql = "select * from login where username = %s"
        cur1.execute(sql, (username,))
        rec = cur1.fetchone()   # fetching all data
        con1.close()
        
        if rec is None:   # no user found
            tmsg.showerror("Error", f"User '{username}' not found in database!")
            self.acc.destroy()
            return

        self.id = rec[0]     # fetching user id for saveChange() command

        # user data from MySQL database
        self.data1 = rec[1:6]
        self.data2 = rec[6:11]

        # displaying user data on left
        labels1 = ["Full Name", "Username", "Gender", "Date Of Birth", "Address"]  

        pyL1 = 50
        for label in labels1:
            tk.Label(self.f1, text=label+" :", font="lucida 16 bold", padx=10, pady=5, bg="#ffdab9", fg="#333333").place(x=20, y=pyL1)
            pyL1 += 50

        pyD1 = 50
        for a in self.data1:
            tk.Label(self.f1, text=a, font="lucida 16 bold", padx=10, pady=5, bg="#ffdab9", fg="#333333").place(x=180, y=pyD1)
            pyD1 += 50

        # displaying user data on right
        labels2 = ["PIN CODE", "City", "State", "Mobile", "Email"]  

        pyL2 = 50
        for label in labels2:
            tk.Label(self.f1, text=label+" :", font="lucida 16 bold", padx=10, pady=5, bg="#ffdab9", fg="#333333").place(x=460, y=pyL2)
            pyL2 += 50

        pyD2 = 50
        for b in self.data2:
            tk.Label(self.f1, text=b, font="lucida 16 bold", padx=10, pady=5, bg="#ffdab9", fg="#333333").place(x=600, y=pyD2)
            pyD2 += 50

        # frame for action buttons
        self.f2 = tk.Frame(self.acc, relief="ridge", bd=1, background="#ffdab9", height=100, width=940)
        self.f2.place(x=10, y=520)

        # update button
        updateBtn = tk.Button(self.f2, text="Update Profile", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="#002147", activebackground="#e65c00", activeforeground="white", cursor="hand2", command=self.update)
        updateBtn.place(x=30, y=25)
        updateBtn.bind("<Return>", self.update)

        # change password
        changeBtn = tk.Button(self.f2, text="Change Password", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="#002147", activebackground="#e65c00", activeforeground="white", cursor="hand2", command=self.changePass)
        changeBtn.place(x=385, y=25)
        changeBtn.bind("<Return>", self.changePass)

        # back button
        backBtn = tk.Button(self.f2, text="Back", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="#002147", activebackground="#e65c00", activeforeground="white", cursor="hand2", command=self.back)
        backBtn.place(x=790, y=25)
        backBtn.bind("<Return>", self.back)


    # update profile
    def update(self, event=None):

        # clear previous frame if exists
        for widget in self.acc.winfo_children():
            widget.destroy()

        tk.Label(self.acc, text="Update Profile", font="lucida 20 underline", background="#fff5e6").place(relx=0.5, rely=0.05, anchor="center")

        # frame for data display
        self.f1 = tk.Frame(self.acc, relief="ridge", bd=1, background="#ffdab9", height=350, width=940) 
        self.f1.place(x=10, y=100)
        
        # displaying user data
        labels1 = ["Full Name", "Username", "Gender", "Date Of Birth", "Address"]  
        self.d1 = {} 

        pyL1, pyD1 = 50, 55
        
        for i, label in enumerate(labels1):
            tk.Label(self.f1, text=label+" :", font="lucida 16 bold", padx=10, pady=5, bg="#ffdab9", fg="#333333").place(x=30, y=pyL1)

            if label == "Gender":
                self.genVar = tk.StringVar(value=self.data1[i])

                m = tk.Radiobutton(self.f1, text="MALE", variable=self.genVar, value="M", font="lucida 16 bold", bg="#ffdab9", fg="#333333",  activebackground="#ffdab9")
                m.place(x=200, y=pyD1)

                fm = tk.Radiobutton(self.f1, text="FEMALE", variable=self.genVar, value="F", font="lucida 16 bold", bg="#ffdab9", fg="#333333",  activebackground="#ffdab9")
                fm.place(x=320, y=pyD1)

                self.d1[label] = self.genVar
            
            elif label == "Date Of Birth":
                self.dt = DateEntry(self.f1, width=10, font="lucida 18 bold", date_pattern="yyyy-mm-dd")
                self.dt.set_date(self.data1[i])
                self.dt.place(x=200, y=pyD1)
                self.d1[label] = self.dt

            else:
                ent = tk.Entry(self.f1, font="lucida 16 bold")
                ent.place(x=200, y=pyD1)
                ent.insert(0, self.data1[i])
                self.d1[label] = ent        
    
            pyL1 += 50
            pyD1 += 50

        # displaying user data
        labels2 = ["PIN CODE", "City", "State", "Mobile", "Email"]  
        self.d2 = {}

        pyL2, pyD2 = 50, 55
        for i, label in enumerate(labels2):
            tk.Label(self.f1, text=label+" :", font="lucida 16 bold", padx=10, pady=5, bg="#ffdab9", fg="#333333").place(x=500, y=pyL2)
            ent = tk.Entry(self.f1, font="lucida 16 bold")
            ent.place(x=650, y=pyD2)
            ent.insert(0, self.data2[i])
            self.d2[label] = ent
            pyL2 += 50
            pyD2 += 50

        # frame for action buttons
        self.f2 = tk.Frame(self.acc, relief="ridge", bd=1, background="#ffdab9", height=100, width=940)
        self.f2.place(x=10, y=520)

        # update button
        upBtn = tk.Button(self.f2, text="Save Changes", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="#002147", activebackground="#e65c00", activeforeground="white", cursor="hand2", command=self.saveChange)
        upBtn.pack(side="left", padx=170, pady=20)
        upBtn.bind("<Return>", self.saveChange)

        # back button
        bkBtn = tk.Button(self.f2, text="BACK", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="#002147", activebackground="#e65c00", activeforeground="white", cursor="hand2", command=self.back)
        bkBtn.pack(side="right", padx=170, pady=20)    
        bkBtn.bind("<Return>", self.back)    


    # save user's updated data in database
    def saveChange(self, event=None):

        # obtaining user data from textbox
        fname   = self.d1["Full Name"].get()
        uname   = self.d1["Username"].get()
        gender  = self.d1["Gender"].get()
        dob     = self.dt.get()
        add     = self.d1["Address"].get()

        pin     = self.d2["PIN CODE"].get()
        city    = self.d2["City"].get()
        state   = self.d2["State"].get()
        mob     = self.d2["Mobile"].get()
        email   = self.d2["Email"].get()

        # print(fname, uname, gender, dob, add, pin, city, state, mob, email)
        
        # updating user data to database
        try:
            con1, cur1 = loginWindow.getDB(self)
            sql = "update login set fullname = %s, username = %s, gender = %s, dob = %s, address = %s, pin = %s, city = %s, state = %s, mobile = %s, email = %s where id = %s"
            values = (fname, uname, gender, dob, add, pin, city, state, mob, email, self.id)
            cur1.execute(sql, values)
            con1.commit()   
            con1.close()

            tmsg.showinfo("Update", "Your Profile updated successfully.")

            self.acc.destroy()      # closing my profile window
            self.parent.destroy()   # closing main menu

            # opening fresh login/signup window
            root = tk.Tk()
            loginWindow(root)
            root.mainloop()

        except Exception as e:
            tmsg.showerror("Database Error", str(e))


    # back to main menu
    def back(self, event=None):

        self.acc.destroy()  #destroy the profile window


    # password change
    def changePass(self, event=None):

        # clear previous frame if exists
        for widget in self.acc.winfo_children():
            widget.destroy()

        tk.Label(self.acc, text="Change Password", font="lucida 20 underline", background="#fff5e6").place(relx=0.5, rely=0.1, anchor="center")

        # new frame
        self.fm = tk.Frame(self.acc, relief="ridge", bd=1, background="#ffdab9", height=350, width=870)
        self.fm.place(relx=0.05, rely=0.2)

        # password
        self.pwd = tk.Label(self.fm, text="New Password : ", font="lucida 16 bold", padx=10, pady=5, bg="#ffdab9", fg="#333333", anchor="center")
        self.pwd.place(x=100, y=100)

        self.pwdEty = tk.Entry(self.fm, font="lucida 20 bold", show="*")
        self.pwdEty.place(x=400, y=100)

        # confirm password
        self.cpwd = tk.Label(self.fm, text="Confirm Password : ", font="lucida 16 bold", padx=10, pady=5, bg="#ffdab9", fg="#333333", anchor="center")
        self.cpwd.place(x=100, y=200)

        self.cpwdEty = tk.Entry(self.fm, font="lucida 20 bold", show="*")
        self.cpwdEty.place(x=400, y=200)

        # save button
        saveBtn = tk.Button(self.acc, text="Save Changes", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="#002147", activebackground="#e65c00", activeforeground="white", cursor="hand2", command=self.savePass)
        saveBtn.place(x=200, y=550)
        saveBtn.bind("<Return>", self.savePass)

        # back button
        bkBtn = tk.Button(self.acc, text="BACK", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="#002147", activebackground="#e65c00", activeforeground="white", cursor="hand2", command=self.back)
        bkBtn.place(x=600, y=550)   
        bkBtn.bind("<Return>", self.back)    
        

    # save user's updated password in database
    def savePass(self, event=None):

        pwd = self.pwdEty.get()
        cpwd = self.cpwdEty.get()

        if len(pwd) < 8:
            tmsg.showerror("Password Length", "Password should be at least 8 characters long.")
            return
    
        if pwd != cpwd:
            tmsg.showerror("ERROR","Password do not match.\n\nTry Again")
            return
        
        try:
            con1, cur1 = loginWindow.getDB(self)
            sql="""update login set pwd = %s where username = %s"""
            values = (pwd, self.username)
            cur1.execute(sql, values)
            con1.commit()
            con1.close()
            tmsg.showinfo("Success","Password Changed Successfully")
        except Exception as e:
            tmsg.showerror("DATABASE ERROR",str(e))

        self.acc.destroy()
        self.parent.destroy()

        login = tk.Tk()
        loginWindow(login)
        login.mainloop()


# class for main window
class mainWindow:

    # Menu Display
    def __init__(self, root, username):
        
        self.root = root
        self.username = username
        # self.username = "Shubham1"

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
        myBtn.bind("<Return>", self.account)

        # log out
        logoutBtn = tk.Button(self.root, text="LOG OUT", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="#002147", activebackground="#e65c00", activeforeground="white", 
        cursor="hand2", command=self.logout)
        logoutBtn.place(x=1040, y=15)
        logoutBtn.bind("<Return>", self.logout)

        # button for book ticket
        bookBtn = tk.Button(f1, text="BOOK TICKETS", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="#002147", activebackground="#e65c00", activeforeground="white", 
        cursor="hand2", command=self.bt)
        bookBtn.grid(row=1, column=1, padx=10, pady=10)
        bookBtn.bind("<Return>", self.bt)

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
    def account(self, event=None):
        profile(self.root, self.username)


    # log out button
    def logout(self, event=None):

        # destroy main menu
        self.root.destroy()

        # opening login window
        log = tk.Tk()
        loginWindow(log)
        log.mainloop()


    # Book Ticket Button
    def bt(self, event=None):

        # heading
        tk.Label(self.f2, text="Choose Train", font="lucida 20 underline", background="#ffdab9").place(x=470, y=10)

        # frame for train search
        self.frm = tk.Frame(self.f2, bd=1, relief="ridge", width=1155, height=100, background="#ff6600")
        self.frm.place(x=10, y=60)

        # source station
        self.sor = tk.Entry(self.frm, font="lucida 18 bold")
        self.sor.insert(0, "From")
        self.sor.place(x=30, y=35)

        # swap button for stations
        self.swp = tk.Button(self.frm, text="⇆", font="lucida 16 bold", padx=10, pady=5, bg="#ff6600", fg="#002147", activebackground="#e65c00", activeforeground="white", 
        cursor="hand2", command=self.swap)
        self.swp.place(x=320, y=25)

        # destinatoin station
        self.des = tk.Entry(self.frm, font="lucida 18 bold")
        self.des.insert(0, "To")
        self.des.place(x=400, y=35)

        # select date
        tk.Label(self.frm, text="Date : ", font="lucida 18 bold", background="#ff6600").place(x=700, y=35)
        self.cal = DateEntry(self.frm, width=6, font="lucida 18 bold")
        self.cal.place(x=800, y=35)

        # search button
        self.srhBtn = tk.Button(self.frm, text="Search", font="lucida 16 bold", padx=20, pady=5, bg="#ff6600", fg="#002147", activebackground="#e65c00", activeforeground="white", 
        cursor="hand2", command=self.search)
        self.srhBtn.place(x=1000, y=25)

        # frame to show available trains
        fmt = tk.Frame(self.f2, relief="ridge", background="#fff5e6", width=1155, height=340)
        fmt.place(x=10, y=180)

    # search button function
    def search(self, event=None):
        
        print(self.sor.get(), self.des.get())

    # swap button function
    def swap(self, event=None):

        # store the values
        self.sr = self.sor.get()
        self.dt = self.des.get()

        # delete the previous values
        self.sor.delete(0, tk.END)
        self.des.delete(0, tk.END)

        # swap values
        self.sor.insert(0, self.dt)
        self.des.insert(0, self.sr)
       






# testing

root = tk.Tk()
app = loginWindow(root)
# app.signup()
# app = mainWindow(root, "Shubham")                                    
root.mainloop()