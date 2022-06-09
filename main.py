from msilib.schema import Icon
from tkinter import *
from credits import credits,help,resource_path
from app import app






root = Tk()
root.title("Calculadora de resistencias")
icon=resource_path('icon.ico')
root.iconbitmap(icon)
root.geometry('600x400+50+50')
root.resizable(False, False)
root.configure(background="#E5DAB2")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Close", command=credits)

filemenu.add_separator()

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=help)
helpmenu.add_command(label="About...", command=credits)
helpmenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Menu", menu=helpmenu)

root.config(menu=menubar)

app(root)





root.mainloop()