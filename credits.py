from tkinter import *
def credits():
   filewin = Toplevel()
   filewin.geometry('200x200')
   filewin.iconbitmap('icon.ico')
   
   filewin.resizable(False, False)
   credits = Label(filewin, text="Credits:"+'\n'+"Programmer:Aldo Vidales "+'\n'+"Name:Calculadora de resistencias "+'\n'+"Email:aldo.vidales@yahoo.com "+'\n'+"Date:3/6/2022 "+'\n'+"Version:1.0 "+'\n'+"License:MIT "+'\n')
   credits.pack()

def help():
   filewin2 = Toplevel()
   filewin2.iconbitmap('icon.ico')
   filewin2.geometry('200x200')
   filewin2.resizable(False, False)
    
    
   help=Label(filewin2,text="For help search in google")
   help.pack()