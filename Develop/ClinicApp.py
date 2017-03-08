import sys
from Develop import PharmacyFunction
from Develop import PatientFunction

if sys.version_info[0] == 2:
    import Tkinter as tk
else:
    import tkinter as tk


PharmacyFunction.connect()
PatientFunction.connect()


TITLE_FONT = ("Helvetica", 18, "bold")
LABEL_FONT = 'Arial'
LABEL_FONT_SIZE = 15


class ClinicApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # self.screen_width = tk.Tk.winfo_screenwidth(self)
        # self.screen_height = tk.Tk.winfo_screenheight(self)
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
        self.show_frame("PatientPage")
        # self.show_frame("PharmaPage")

    def show_frame(self, page_name):
        frame = self.frame[page_name]
        frame.tkraise()


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        # tk.Frame.__init__(self, parent, width=800, height=600)
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
        # tk.Frame.__init__(self, parent, width=800, height=600)
        tk.Frame.__init__(self, parent)

        self.controller = controller
        # self.view_command()

        bgclr = "#282828"
        fgclr = "#cecece"
        clr = '#004a95'

        '''
        TitleBar
        '''
        PatientTitle_LabelFrame = tk.LabelFrame(self)
        PatientTitle_LabelFrame.grid(row=0, columnspan=20, rowspan=2, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)
        label = tk.Label(PatientTitle_LabelFrame, text="QUẢN LÝ BỆNH NHÂN", font=TITLE_FONT)
        label.grid(row=0, column=0)
        button = tk.Button(PatientTitle_LabelFrame, text="Đến quản lý thuốc",
                           command=lambda: controller.show_frame("PharmaPage"))
        button.grid(row=0, column=1)

        '''
         Patient Detailed
         '''
        PatientDetailed_LabelFrame = tk.LabelFrame(self, text="Thông tin bệnh nhân")
        PatientDetailed_LabelFrame.grid(row=2, columnspan=20, rowspan=2, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)

        self.patientName_label = tk.Label(PatientDetailed_LabelFrame, text="Họ Tên:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        self.patientName_label.grid(row=0, column=0)
        self.patientName_text = tk.StringVar()
        self.patientName_entry = tk.Entry(PatientDetailed_LabelFrame, textvariable=self.patientName_text, width=80)
        self.patientName_entry.grid(row=0, column=1, columnspan=15)

        self.patientID_label = tk.Label(PatientDetailed_LabelFrame, text="CMND:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        self.patientID_label.grid(row=1, column=0)
        self.patientID_text = tk.StringVar()
        self.patientID_entry = tk.Entry(PatientDetailed_LabelFrame, textvariable=self.patientID_text, width=80)
        self.patientID_entry.grid(row=1, column=1, columnspan=5)

        self.patientPhone_label = tk.Label(PatientDetailed_LabelFrame, text="Điện thoại:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        self.patientPhone_label.grid(row=2, column=0)
        self.patientPhone_text = tk.StringVar()
        self.patientPhone_entry = tk.Entry(PatientDetailed_LabelFrame, textvariable=self.patientPhone_text, width=80)
        self.patientPhone_entry.grid(row=2, column=1, columnspan=5)

        self.patientAge_label = tk.Label(PatientDetailed_LabelFrame, text="Tuổi:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        self.patientAge_label.grid(row=3, column=0)
        self.patientAge_text = tk.StringVar()
        self.patientAge_entry = tk.Entry(PatientDetailed_LabelFrame, textvariable=self.patientAge_text, width=80)
        self.patientAge_entry.grid(row=3, column=1, columnspan=5)

        self.patientBirthYear_label = tk.Label(PatientDetailed_LabelFrame, text="Năm sinh:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        self.patientBirthYear_label.grid(row=4, column=0)
        self.patientBirthYear_text = tk.StringVar()
        self.patientBirthYear_entry = tk.Entry(PatientDetailed_LabelFrame, textvariable=self.patientBirthYear_text, width=80)
        self.patientBirthYear_entry.grid(row=4, column=1, columnspan=5)

        '''
         Patient History
         '''
        PatientHistory_LabelFrame = tk.LabelFrame(self, text="Lịch sử điều trị")
        PatientHistory_LabelFrame.grid(row=2, column=21, columnspan=20, rowspan=2, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)

        self.patientHistory_label = tk.Label(PatientHistory_LabelFrame, text="Tiền căn:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        self.patientHistory_label.grid(row=0, column=0)
        self.patientHistory_text = tk.StringVar()
        self.patientHistory_entry = tk.Entry(PatientHistory_LabelFrame, textvariable=self.patientHistory_text, width=100)
        self.patientHistory_entry.grid(row=0, column=1, columnspan=7, ipady=25)

        self.patientFamilyHistory_label = tk.Label(PatientHistory_LabelFrame, text="Tiền căn gia đình:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        self.patientFamilyHistory_label.grid(row=1, column=0)
        self.patientFamilyHistory_text = tk.StringVar()
        self.patientFamilyHistory_entry = tk.Entry(PatientHistory_LabelFrame, textvariable=self.patientFamilyHistory_text, width=100)
        self.patientFamilyHistory_entry.grid(row=1, column=1, columnspan=7, ipady=25)

        '''
         Patient treatment
         '''
        PatientTreatment_LabelFrame = tk.LabelFrame(self, text="Điều trị")
        PatientTreatment_LabelFrame.grid(row=4, column=0, columnspan=50, rowspan=2, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)

        self.patientDescription_label = tk.Label(PatientTreatment_LabelFrame, text="Mô tả bệnh:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        self.patientDescription_label.grid(row=9, column=0)
        self.patientDescription_text = tk.StringVar()
        self.patientDescription_entry = tk.Entry(PatientTreatment_LabelFrame, textvariable=self.patientDescription_text, width=100)
        self.patientDescription_entry.grid(row=9, column=1, columnspan=7, rowspan=5, ipady=25)

        self.patientDiagnostic_label = tk.Label(PatientTreatment_LabelFrame, text="Chuẩn đoán:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        self.patientDiagnostic_label.grid(row=9, column=8)
        self.patientDiagnostic_text = tk.StringVar()
        self.patientDiagnostic_entry = tk.Entry(PatientTreatment_LabelFrame, textvariable=self.patientDiagnostic_text, width=100)
        self.patientDiagnostic_entry.grid(row=9, column=9, columnspan=7, rowspan=5, ipady=25)

        '''
         Patient List
         '''
        PatientList_LabelFrame = tk.LabelFrame(self, text="Danh sách bệnh nhân")
        PatientList_LabelFrame.grid(row=6, column=0, columnspan=50, rowspan=2, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)

        self.patientList = tk.Listbox(PatientList_LabelFrame, height=10, width=230)
        self.patientList.grid(row=0, column=0, rowspan=5, columnspan=50)

        self.patientScrollBox = tk.Scrollbar(PatientList_LabelFrame)
        self.patientScrollBox.grid(row=0, column=51, rowspan=10, sticky='NS')

        self.patientList.configure(yscrollcommand=self.patientScrollBox.set)
        self.patientScrollBox.configure(command=self.patientList.yview)
        self.patientList.bind('<<ListboxSelect>>', self.get_patient_selected_row)

        '''
         Function List
         '''
        PatientFuction_LabelFrame = tk.LabelFrame(self, text="Chức năng")
        PatientFuction_LabelFrame.grid(row=8, column=0, columnspan=50, rowspan=2, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)


        self.viewButton = tk.Button(PatientFuction_LabelFrame, text="Xem tất cả", width=12, bg=bgclr, fg=fgclr, command=self.view_command)
        self.viewButton.grid(row=0, column=0, padx=5, pady=5, ipadx=5, ipady=5)

        self.searchButton = tk.Button(PatientFuction_LabelFrame, text="Tìm kiếm", width=12, bg=bgclr, fg=fgclr, command=self.search_command)
        self.searchButton.grid(row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5)

        self.insertButton = tk.Button(PatientFuction_LabelFrame, text="Thêm mới", width=12, bg=bgclr, fg=fgclr, command=self.insert_command)
        self.insertButton.grid(row=0, column=2, padx=5, pady=5, ipadx=5, ipady=5)

        self.updateButton = tk.Button(PatientFuction_LabelFrame, text="Cập nhật", width=12, bg=bgclr, fg=fgclr,command=self.update_command)
        self.updateButton.grid(row=0, column=3, padx=5, pady=5, ipadx=5, ipady=5)

        self.deleteButton = tk.Button(PatientFuction_LabelFrame, text="Xóa dữ liệu", width=12, bg=bgclr, fg=fgclr, command=self.delete_command)
        self.deleteButton.grid(row=0, column=4, padx=5, pady=5, ipadx=5, ipady=5)


    def view_command(self):
        self.patientList.delete(0, tk.END)
        for row in PatientFunction.view():
            self.patientList.insert(tk.END, row)

    def search_command(self):
        self.patientList.delete(0,tk.END)
        for row in PatientFunction.search(self.patientID_entry.get(), self.patientName_entry.get(), self.patientPhone_entry.get(), self.patientAge_entry.get(), self.patientBirthYear_entry.get(), self.patientHistory_entry.get(), self.patientFamilyHistory_entry.get(), self.patientDescription_entry.get(),self.patientDiagnostic_entry.get()):
            self.patientList.insert(tk.END, row)

    def insert_command(self):
        PatientFunction.insert(self.patientID_entry.get(), self.patientName_entry.get(), self.patientPhone_entry.get(), self.patientAge_entry.get(), self.patientBirthYear_entry.get(), self.patientHistory_entry.get(), self.patientFamilyHistory_entry.get(), self.patientDescription_entry.get(),self.patientDiagnostic_entry.get())
        self.patientList.delete(0, tk.END)
        self.patientList.insert(tk.END, (self.patientID_entry.get(), self.patientName_entry.get(), self.patientPhone_entry.get(), self.patientAge_entry.get(), self.patientBirthYear_entry.get(), self.patientHistory_entry.get(), self.patientFamilyHistory_entry.get(), self.patientDescription_entry.get(),self.patientDiagnostic_entry.get()))

    def delete_command(self):
        PatientFunction.delete(patient_selected_tuple[0])


    def update_command(self):
        PatientFunction.update(patient_selected_tuple[0],self.patientID_entry.get(), self.patientName_entry.get(), self.patientPhone_entry.get(), self.patientAge_entry.get(), self.patientBirthYear_entry.get(), self.patientHistory_entry.get(), self.patientFamilyHistory_entry.get(), self.patientDescription_entry.get(),self.patientDiagnostic_entry.get())


    def get_patient_selected_row(self,event):
        global patient_selected_tuple
        index = self.patientList.curselection()[0]
        patient_selected_tuple = self.patientList.get(index)

        self.patientID_entry.delete(0, tk.END)
        self.patientID_entry.insert(tk.END, patient_selected_tuple[1])

        self.patientName_entry.delete(0, tk.END)
        self.patientName_entry.insert(tk.END, patient_selected_tuple[2])

        self.patientPhone_entry.delete(0, tk.END)
        self.patientPhone_entry.insert(tk.END, patient_selected_tuple[3])

        self.patientAge_entry.delete(0, tk.END)
        self.patientAge_entry.insert(tk.END, patient_selected_tuple[4])

        self.patientBirthYear_entry.delete(0, tk.END)
        self.patientBirthYear_entry.insert(tk.END, patient_selected_tuple[5])

        self.patientHistory_entry.delete(0, tk.END)
        self.patientHistory_entry.insert(tk.END, patient_selected_tuple[6])

        self.patientFamilyHistory_entry.delete(0, tk.END)
        self.patientFamilyHistory_entry.insert(tk.END, patient_selected_tuple[7])

        self.patientDescription_entry.delete(0, tk.END)
        self.patientDescription_entry.insert(tk.END, patient_selected_tuple[8])

        self.patientDiagnostic_entry.delete(0, tk.END)
        self.patientDiagnostic_entry.insert(tk.END, patient_selected_tuple[9])


class PharmaPage(tk.Frame):
    def __init__(self, parent, controller):
        # tk.Frame.__init__(self, parent, width=800, height=600)
        tk.Frame.__init__(self, parent)

        self.controller = controller
        # self.view_command()

        bgclr = "#282828"
        fgclr = "#cecece"
        clr = '#004a95'

        '''
        TitleBar
        '''
        PharmaTitle_LabelFrame = tk.LabelFrame(self)
        PharmaTitle_LabelFrame.grid(row=0, columnspan=20, rowspan=2, sticky='WE',padx=5, pady=5, ipadx=5, ipady=5)
        label = tk.Label(PharmaTitle_LabelFrame, text="QUẢN LÝ THUỐC", font=TITLE_FONT)
        # label.pack(side="top", fill="x", pady=10)
        label.grid(row=0, column=0)

        button = tk.Button(PharmaTitle_LabelFrame, text="Đến quản lý bệnh nhân",
                           command=lambda: controller.show_frame("PatientPage"))
        button.grid(row=0, column=1)


        '''
        Pharmacy Detailed
        '''
        PharmaDetailed_LabeFrame = tk.LabelFrame(self, text="Thông tin thuốc")
        PharmaDetailed_LabeFrame.grid(row=2, columnspan=20, rowspan=2, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)


        self.medicineCode_label = tk.Label(PharmaDetailed_LabeFrame, text="Mã thuốc:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        self.medicineCode_label.grid(row=0, column=0)
        self.medicineCode_text = tk.StringVar()
        self.medicineCode_entry = tk.Entry(PharmaDetailed_LabeFrame, textvariable=self.medicineCode_text, width=80)
        self.medicineCode_entry.grid(row=0, column=1, columnspan=5)

        self.medicineName_label = tk.Label(PharmaDetailed_LabeFrame, text="Tên thuốc:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        self.medicineName_label.grid(row=2, column=0)
        self.medicineName_text = tk.StringVar()
        self.medicineName_entry = tk.Entry(PharmaDetailed_LabeFrame, textvariable=self.medicineName_text, width=80)
        self.medicineName_entry.grid(row=2, column=1, columnspan=5)

        self.medicineActiveElement_label = tk.Label(PharmaDetailed_LabeFrame, text="Hoạt chất:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        self.medicineActiveElement_label.grid(row=3, column=0)
        self.medicineActiveElement_text = tk.StringVar()
        self.medicineActiveElement_entry = tk.Entry(PharmaDetailed_LabeFrame, textvariable=self.medicineActiveElement_text, width=80)
        self.medicineActiveElement_entry.grid(row=3, column=1, columnspan=5)

        self.medicineUnit_label = tk.Label(PharmaDetailed_LabeFrame, text="Đơn vị:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        self.medicineUnit_label.grid(row=4, column=0)
        self.medicineUnit_text = tk.StringVar()
        self.medicineUnit_entry = tk.Entry(PharmaDetailed_LabeFrame, textvariable=self.medicineUnit_text, width=80)
        self.medicineUnit_entry.grid(row=4, column=1, columnspan=5)

        self.medicineInventory_label = tk.Label(PharmaDetailed_LabeFrame, text="Tồn kho:", font=(LABEL_FONT, LABEL_FONT_SIZE))
        self.medicineInventory_label.grid(row=5, column=0)
        self.medicineInventory_text = tk.StringVar()
        self.medicineInventory_entry = tk.Entry(PharmaDetailed_LabeFrame, textvariable=self.medicineInventory_text, width=80)
        self.medicineInventory_entry.grid(row=5, column=1, columnspan=5)

        '''
        Display Pharmacy list
        '''
        PharmaList_LabeFrame = tk.LabelFrame(self, text="Danh sách thuốc")
        PharmaList_LabeFrame.grid(row=2, column=21, columnspan=20, rowspan=2, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)

        self.medicineList = tk.Listbox(PharmaList_LabeFrame, height=10, width=100)
        self.medicineList.grid(row=0, column=0, rowspan=5, columnspan=10)

        self.medicineScrollBox = tk.Scrollbar(PharmaList_LabeFrame)
        self.medicineScrollBox.grid(row=0, column=15, rowspan=10, sticky='NS')

        self.medicineList.configure(yscrollcommand=self.medicineScrollBox.set)
        self.medicineScrollBox.configure(command=self.medicineList.yview)
        self.medicineList.bind('<<ListboxSelect>>', self.get_pharmacy_selected_row)

        '''
        Function Section
        '''
        PharmaFuction_LabeFrame = tk.LabelFrame(self, text="Chức năng")
        PharmaFuction_LabeFrame.grid(row=5, column=0, columnspan=20, rowspan=2, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)

        self.viewButton = tk.Button(PharmaFuction_LabeFrame, text="Xem tất cả", width=12, bg=bgclr, fg=fgclr, command=self.view_command)
        self.viewButton.grid(row=0, column=0, padx=5, pady=5, ipadx=5, ipady=5)

        self.searchButton = tk.Button(PharmaFuction_LabeFrame, text="Tìm kiếm", width=12, bg=bgclr, fg=fgclr, command=self.search_command)
        self.searchButton.grid(row=0, column=1,padx=5, pady=5, ipadx=5, ipady=5)

        self.insertButton = tk.Button(PharmaFuction_LabeFrame, text="Thêm mới", width=12, bg=bgclr, fg=fgclr, command=self.insert_command)
        self.insertButton.grid(row=0, column=2,padx=5, pady=5, ipadx=5, ipady=5)

        self.updateButton = tk.Button(PharmaFuction_LabeFrame, text="Cập nhật", width=12, bg=bgclr, fg=fgclr,command=self.update_command)
        self.updateButton.grid(row=0, column=3,padx=5, pady=5, ipadx=5, ipady=5)

        self.deleteButton = tk.Button(PharmaFuction_LabeFrame, text="Xóa dữ liệu", width=12, bg=bgclr, fg=fgclr, command=self.delete_command)
        self.deleteButton.grid(row=0, column=4,padx=5, pady=5, ipadx=5, ipady=5)

        '''
        Function Section
        '''

    def view_command(self):
        self.medicineList.delete(0, tk.END)
        for row in PharmacyFunction.view():
            self.medicineList.insert(tk.END, row)

    def search_command(self):
        self.medicineList.delete(0,tk.END)
        for row in PharmacyFunction.search(self.medicineCode_entry.get(), self.medicineName_entry.get(), self.medicineActiveElement_entry.get(), self.medicineUnit_entry.get(), self.medicineInventory_entry.get()):
            self.medicineList.insert(tk.END, row)

    def insert_command(self):
        PharmacyFunction.insert(self.medicineCode_entry.get(), self.medicineName_entry.get(), self.medicineActiveElement_entry.get(), self.medicineUnit_entry.get(), self.medicineInventory_entry.get())
        self.medicineList.delete(0, tk.END)
        self.medicineList.insert(tk.END,(self.medicineCode_entry.get(), self.medicineName_entry.get(), self.medicineActiveElement_entry.get(), self.medicineUnit_entry.get(), self.medicineInventory_entry.get()))

    def delete_command(self):
        PharmacyFunction.delete(pharmacy_selected_tuple[0])

    def update_command(self):
        PharmacyFunction.update(pharmacy_selected_tuple[0], self.medicineCode_entry.get(), self.medicineName_entry.get(), self.medicineActiveElement_entry.get(), self.medicineUnit_entry.get(), self.medicineInventory_entry.get())

    def get_pharmacy_selected_row(self, event):
        global pharmacy_selected_tuple

        index = self.medicineList.curselection()[0]
        pharmacy_selected_tuple = self.medicineList.get(index)
        self.medicineCode_entry.delete(0, tk.END)
        self.medicineCode_entry.insert(tk.END, pharmacy_selected_tuple[1])

        self.medicineName_entry.delete(0, tk.END)
        self.medicineName_entry.insert(tk.END, pharmacy_selected_tuple[2])

        self.medicineActiveElement_entry.delete(0, tk.END)
        self.medicineActiveElement_entry.insert(tk.END, pharmacy_selected_tuple[3])

        self.medicineUnit_entry.delete(0, tk.END)
        self.medicineUnit_entry.insert(tk.END, pharmacy_selected_tuple[4])

        self.medicineInventory_entry.delete(0, tk.END)
        self.medicineInventory_entry.insert(tk.END, pharmacy_selected_tuple[5])


if __name__ == "__main__":
    app = ClinicApp()
    app.mainloop()
