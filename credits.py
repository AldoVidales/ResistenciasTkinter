from msilib.schema import Icon
from multiprocessing.spawn import import_main_path
from tkinter import *
import os,sys


def resource_path(relative_path):
   try:
       base_path = sys._MEIPASS
   except Exception:
        base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
icon=resource_path('icon.ico')

def credits():
   filewin = Toplevel()
   filewin.geometry('200x200')
   filewin.iconbitmap(icon)







   
   filewin.resizable(False, False)
   credits = Label(filewin, text="Credits:"+'\n'+"Programmer:Aldo Vidales "+'\n'+"Name:Color resistor "+'\n'+"Email:aldo.vidales@yahoo.com "+'\n'+"Date:3/6/2022 "+'\n'+"Version:1.0 "+'\n'+"License:MIT "+'\n',anchor="center",font=("Arial",11),bg="#E5DAB2",fg="black")
   credits.pack()

def help():
   filewin2 = Toplevel()
   filewin2.iconbitmap(icon)


   filewin2.geometry('200x200')
   filewin2.resizable(False, False)


   help=Label(filewin2,text="For help search in google")
   help.pack()