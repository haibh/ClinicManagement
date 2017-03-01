import sys
if sys.version_info[0] == 2:
    import Tkinter as tk
else:
    import tkinter as tk


class PatientPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="quản lý bệnh nhân", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Bệnh nhân",
                           command=lambda: controller.show_frame("PharmaPage"))
        button.pack()