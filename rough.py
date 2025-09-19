import tkinter as tk
from tkcalendar import DateEntry

root = tk.Tk()

root.geometry("400x400")
root.maxsize(400, 400)
root.minsize(400, 400)

selectOption = tk.StringVar(value="M")

r1 = tk.Radiobutton(root, text="Male", textvariable=selectOption, value="M", font="lucida 16 bold")
r1.pack()

dob = DateEntry(root, width=15, background="darkblue",
                foreground="white", date_pattern="yyyy-mm-dd")
dob.pack(pady=20)

def show_date():
    print("Selected Date:", dob.get())

btn = tk.Button(root, text="Get Date", command=show_date)
btn.pack()



root.mainloop()

# for i in range(len(rec)):
        #     u=rec[i][2]
        #     p=rec[i][11]
        #     if ur == "" or pwd == "":
        #         tmsg.showwarning("Incomplete","Please Enter Correct Input.")
        #         break
        #     elif ur == u:
        #         if pwd == p:
        #             self.root.destroy()     # clase login window
        #             # opening main window
        #             new_root = tk.Tk()
        #             mainWindow(new_root, ur)
        #             new_root.mainloop()
        #             break
        #         else:
        #             tmsg.showerror("ERROR","Invalid Password! Try Again...")
        #             break
        # else:
        #     tmsg.showerror("ERROR","Invalid Username! Try Again...")

