from tkinter import *
def credits():
   filewin = Toplevel()
   filewin.geometry('200x200')
   filewin.resizable(False, False)
   credits = Label(filewin, text="Credits:"+'\n'+"Programmer:Alrift "+'\n'+"Name:Aldo Vidales "+'\n'+"Email:aldo.vidales@yahoo.com "+'\n'+"Date:3/6/2022 "+'\n'+"Version:1.0 "+'\n'+"License:MIT "+'\n')
   credits.pack()

def help():
   filewin2 = Toplevel()
   filewin2.geometry('200x200')
   filewin2.resizable(False, False)
    
    
   help=Label(filewin2,text="For help search in google")
   help.pack()