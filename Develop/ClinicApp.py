import sys
from Develop import PharmacyFunction

if sys.version_info[0] == 2:
    import Tkinter as tk
else:
    import tkinter as tk


PharmacyFunction.connect()


TITLE_FONT = ("Helvetica", 18, "bold")
LABEL_FONT = 'Arial'
LABEL_FONT_SIZE = 15


class ClinicApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.screen_width = tk.Tk.winfo_screenwidth(self)
        self.screen_height = tk.Tk.winfo_screenheight(self)
        # print(self.screen_width, self.screen_height)

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
        # tk.Frame.__init__(self, parent, width=1800, height=1000)
        tk.Frame.__init__(self, parent)
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
        label = tk.Label(self, text="QUẢN LÝ THUỐC", font=TITLE_FONT)
        # label.pack(side="top", fill="x", pady=10)
        label.grid(row=0, column=1)

        button = tk.Button(self, text="Về trang đăng nhập",
                           command=lambda: controller.show_frame("LoginPage"))
        button.grid(row=1, column=1)

        bgclr = "#282828"
        fgclr = "#cecece"
        clr = '#004a95'

        medicineCode_label = tk.Label(self, text="Mã thuốc:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        medicineCode_label.grid(row=2, column=0)
        medicineCode_text = tk.StringVar()
        medicineCode_entry = tk.Entry(self, textvariable=medicineCode_text)
        medicineCode_entry.grid(row=2, column=1, columnspan=5)

        medicineName_label = tk.Label(self, text="Tên thuốc:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        medicineName_label.grid(row=3, column=0)
        medicineName_text = tk.StringVar()
        medicineName_entry = tk.Entry(self, textvariable=medicineName_text)
        medicineName_entry.grid(row=3, column=1, columnspan=5)

        medicineActiveElement_label = tk.Label(self, text="Hoạt chất:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        medicineActiveElement_label.grid(row=4, column=0)
        medicineActiveElement_text = tk.StringVar()
        medicineActiveElement_entry = tk.Entry(self, textvariable=medicineActiveElement_text)
        medicineActiveElement_entry.grid(row=4, column=1, columnspan=5)

        medicineUnit_label = tk.Label(self, text="Đơn vị:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        medicineUnit_label.grid(row=5, column=0)
        medicineUnit_text = tk.StringVar()
        medicineUnit_entry = tk.Entry(self, textvariable=medicineUnit_text)
        medicineUnit_entry.grid(row=5, column=1, columnspan=5)

        medicineInventory_label = tk.Label(self, text="Tồn kho:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        medicineInventory_label.grid(row=6, column=0)
        medicineInventory_text = tk.StringVar()
        medicineInventory_entry = tk.Entry(self, textvariable=medicineInventory_text)
        medicineInventory_entry.grid(row=6, column=1, columnspan=5)


        # medicineList = tk.Listbox(self, height=6, width=50)
        self.medicineList = tk.Listbox(self)
        self.medicineList.grid(row=2, column=5, rowspan=5, columnspan=5)

        self.medicineScrollBox = tk.Scrollbar(self)
        self.medicineScrollBox.grid(row=2, column=13, rowspan=10)

        self.medicineList.configure(yscrollcommand=self.medicineScrollBox.set)
        self.medicineScrollBox.configure(command=self.medicineList.yview)

        viewButton = tk.Button(self, text="Xem tất cả", width=12, bg=bgclr, fg=fgclr, command=self.view_command)
        viewButton.grid(row=7, column=0)

        searchButton = tk.Button(self, text="Tìm kiếm", width=12, bg=bgclr, fg=fgclr)
        searchButton.grid(row=7, column=1)

        addButton = tk.Button(self, text="Thêm mới", width=12, bg=bgclr, fg=fgclr)
        addButton.grid(row=7, column=2)

        deleteButton = tk.Button(self, text="Xóa dữ liệu", width=12, bg=bgclr, fg=fgclr)
        deleteButton.grid(row=7, column=3)

        # medicineList.bind('<<ListboxSelect>>', self.get_selected_row)

    def view_command(self):
        self.medicineList.delete(0, END)
        for row in PharmacyFunction.view():
            self.medicineList.insert(END, row)

    def get_pharmacy_selected_row(self):
        global pharmacy_selected_tuple
        # index = self.medicineList.curselection()[0]


if __name__ == "__main__":
    app = ClinicApp()
    app.mainloop()
