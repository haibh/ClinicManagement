from Tkinter import *

bgclr = "#282828"
fgclr = "#cecece"
clr = '#004a95'

users = [("kiman", "phongmachbacsi")]  # <<<here ''dilip'' is user and ''python'' is password


def login():
    if (user_Entry.get(), password_Entry.get()) in users:
        w.destroy()
    else:
        warn.config(text="Invalid username or Password", fg="red")


w = Tk()
w.title("login")
w.geometry("500x300")
w.config(bg=bgclr)
w.resizable()

user = Label(w,
             text="User",
             font=("blod", 15),
             bg=bgclr,
             fg=fgclr)
user.place(x=20, y=40)

user_Entry = Entry(w, bg=bgclr,
                   fg="white",
                   relief=GROOVE,
                   highlightcolor="white",
                   highlightthickness=2,
                   highlightbackground=clr,
                   width=40,
                   font=10,
                   bd=5)
user_Entry.place(x=20, y=80)

password = Label(w,
                 text="Password",
                 font=("blod", 15),
                 bg=bgclr,
                 fg=fgclr)
password.place(x=20, y=120)

password_Entry = Entry(w, bg=bgclr,
                       fg="white",
                       relief=GROOVE,
                       highlightcolor="white",
                       highlightthickness=2,
                       highlightbackground=clr,
                       width=40,
                       font=10,
                       show="*",
                       bd=5)
password_Entry.place(x=20, y=160)

warn = Label(w,
             font=("blod", 10),
             bg=bgclr)

warn.place(x=80, y=200)

button = Button(w,
                text="Login",
                bg=clr,
                fg="white",
                relief=GROOVE,
                highlightcolor=clr,
                highlightthickness=4,
                width=40,
                font=10,
                command=login)
button.place(x=20, y=240)

w.mainloop()



