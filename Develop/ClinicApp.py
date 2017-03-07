import sys
if sys.version_info[0] == 2:
    import Tkinter as tk
else:
    import tkinter as tk

TITLE_FONT = ("Helvetica", 18, "bold")
LABEL_FONT = 'Arial'
LABEL_FONT_SIZE = 15


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

        # self.show_frame("LoginPage")
        self.show_frame("PharmaPage")

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

        self.warn_label = tk.Label(self, text="Vui lòng đăng nhập.", font=("blod", 10), bg=clr)
        self.warn_label.place(x=80, y=200)

        self.login_button = tk.Button(self, text="Login", width="40", font=10, command=self.login)
        self.login_button.place(x=80, y=250)

        # # Enter to login
        # self.password_entry.bind('<Enter>', self.login)  # Still have error

    def login(self):
        if (self.user_entry.get(), self.password_entry.get()) in self.users:
            self.controller.show_frame("PatientPage")
            print("Login OK")
        else:
            self.warn_label.config(text="Sai Tên đăng nhập hoặc Mật khẩu", fg="red")
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
        # label.pack(side="top", fill="x", pady=10)
        label.grid(row=0, column=1)

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("LoginPage"))
        button.grid(row=1, column=1)



        MedicineID_label = tk.Label(self, text="Mã thuốc:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        MedicineID_label.grid(row=2, column=0)
        MedicineID_text = tk.StringVar()
        MedicineID_entry = tk.Entry(self, textvariable=MedicineID_text)
        MedicineID_entry.grid(row=2, column=1, columnspan=5)

        MedicineName_label = tk.Label(self, text="Tên thuốc:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        MedicineName_label.grid(row=3, column=0)
        MedicineName_text = tk.StringVar()
        MedicineName_entry = tk.Entry(self, textvariable=MedicineName_text)
        MedicineName_entry.grid(row=3, column=1, columnspan=5)

        MedicineActiveElement_label = tk.Label(self, text="Hoạt chất:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        MedicineActiveElement_label.grid(row=4, column=0)
        MedicineActiveElement_text = tk.StringVar()
        MedicineActiveElement_entry = tk.Entry(self, textvariable=MedicineActiveElement_text)
        MedicineActiveElement_entry.grid(row=4, column=1, columnspan=5)

        MedicineUnit_label = tk.Label(self, text="Đơn vị:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        MedicineUnit_label.grid(row=5, column=0)
        MedicineUnit_text = tk.StringVar()
        MedicineUnit_entry = tk.Entry(self, textvariable=MedicineUnit_text)
        MedicineUnit_entry.grid(row=5, column=1, columnspan=5)

        MedicineInventory_label = tk.Label(self, text="Tồn kho:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        MedicineInventory_label.grid(row=6, column=0)
        MedicineInventory_text = tk.StringVar()
        MedicineInventory_entry = tk.Entry(self, textvariable=MedicineInventory_text)
        MedicineInventory_entry.grid(row=6, column=1, columnspan=5)


        MedicineList = tk.Listbox(self, height=6, width=50)
        MedicineList.grid(row=2, column=3, rowspan=10)

        MedicineScrollBox = tk.Scrollbar(self)
        MedicineScrollBox.grid(row=2, column=3, rowspan=10)

        # MedicineList.configure(yscrollcommand=MedicineList.set)
        # MedicineScrollBox.configure(command=MedicineList.yview)

        # MedicineList.bind('<<ListboxSelect>>', self.get_selected_row)

    def get_selected_row(self):
        pass

if __name__ == "__main__":
    app = ClinicApp()
    app.mainloop()
