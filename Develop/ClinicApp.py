import sys
if sys.version_info[0] == 2:
    import Tkinter as tk
else:
    import tkinter as tk

TITLE_FONT = ("Helvetica", 18, "bold")


class ClinicApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.screen_width = tk.Tk.winfo_screenwidth(self)
        self.screen_height = tk.Tk.winfo_screenheight(self)
        print(self.screen_width, self.screen_height)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(1, weight=1)

        self.frame = {}
        for F in (LoginPage, PatientPage, PharmaPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frame[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        frame = self.frame[page_name]
        frame.tkraise()


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1800, height=1000)
        self.controller = controller

        bgclr = "#282828"
        fgclr = "#cecece"
        clr = '#004a95'

        tk.Frame.config(self, bg=bgclr)
        # tk.Tk.resizable(True, False)

        self.users = [("kiman", "bacsi"), ("1", "1")]

        self.user_label = tk.Label(self, text="Username", font=("blod", 15), bg=bgclr, fg=fgclr)
        self.user_label.place(x=20, y=40)

        self.user_entry = tk.Entry(self, bg=bgclr, fg="white", width=40, font=10, bd=5)
        self.user_entry.place(x=20, y=80)
        self.user_entry.focus()

        self.password_label = tk.Label(self, text="Password", font=("blod", 15), bg=bgclr, fg=fgclr)
        self.password_label.place(x=20, y=120)

        self.password_entry = tk.Entry(self, bg=bgclr, fg="white", width=40, font=10, show="*", bd=5)
        self.password_entry.place(x=20, y=160)

        self.warn_label = tk.Label(self, font=("blod", 10), bg=bgclr)
        self.warn_label.place(x=80, y=200)

        self.login_button = tk.Button(self, text="Login", width="40", font=10, command=self.login)
        self.login_button.place(x=80, y=200)

        # # Enter to login
        self.password_entry.bind('<Enter>', self.login)  # Still have error

    def login(self):
        if (self.user_entry.get(), self.password_entry.get()) in self.users:
            self.controller.show_frame("PatientPage")
            print("Login OK")
        else:
            self.warn_label.config(text="Invalid username or Password", fg="red")
            print(self.user_entry.get(), self.password_entry.get())
            print("Login Failed")


class PatientPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="quản lý bệnh nhân", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Bệnh nhân",
                           command=lambda: controller.show_frame("PharmaPage"))
        button.pack()


class PharmaPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="quản lý thuốc", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("LoginPage"))
        button.pack()



if __name__ == "__main__":
    app = ClinicApp()
    app.mainloop()
