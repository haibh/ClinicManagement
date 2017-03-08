import sys


if sys.version_info[0] == 2:
    import Tkinter as tk
else:
    import tkinter as tk


Label(master, text="First").grid(row=0)
Label(master, text="Second").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)