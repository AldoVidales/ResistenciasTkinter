from calendar import month
import imp
from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk
from turtle import color

def scrollbar(root):

    def cambiar():
        c1=StringVar()
        color1=str(list1.get())
        if color1=="Black":
            Label(root,text="",bg="black",height=2,width=3).place(x=100,y=120)
            c1="0"
        elif color1=="Brown":
            Label(root,text="",bg="brown",height=2,width=3).place(x=100,y=120)
            c1="1"
        elif color1=="Red":
            Label(root,text="",bg="red",height=2,width=3).place(x=100,y=120)
            c1="2"

        elif color1=="Orange":
            Label(root,text="",bg="orange",height=2,width=3).place(x=100,y=120)
            c1="3"

        elif color1=="Yellow":
            Label(root,text="",bg="yellow",height=2,width=3).place(x=100,y=120)
            c1="4"


        elif color1=="Green":
            Label(root,text="",bg="green",height=2,width=3).place(x=100,y=120)
            c1="5"

        elif color1=="Blue":
            Label(root,text="",bg="blue",height=2,width=3).place(x=100,y=120)
            c1="6"
        elif color1=="Violet":
            Label(root,text="",bg="purple",height=2,width=3).place(x=100,y=120)
            c1="7"
        elif color1=="Gray":
            Label(root,text="",bg="gray",height=2,width=3).place(x=100,y=120)
            c1="8"
        elif color1=="White":
            Label(root,text="",bg="white",height=2,width=3).place(x=100,y=120)
            c1="9"

        color2=str(list2.get())
        if color2=="Black":
            Label(root,text="",bg="black",height=2,width=3).place(x=100+50,y=120)
            c2="0"
        elif color2=="Brown":
            Label(root,text="",bg="brown",height=2,width=3).place(x=100+50,y=120)
            c2="1"
        elif color2=="Red":
            Label(root,text="",bg="red",height=2,width=3).place(x=100+50,y=120)
            c2="2"

        elif color2=="Orange":
            Label(root,text="",bg="orange",height=2,width=3).place(x=100+50,y=120)
            c2="3"

        elif color2=="Yellow":
            Label(root,text="",bg="yellow",height=2,width=3).place(x=100+50,y=120)
            c2="4"


        elif color2=="Green":
            Label(root,text="",bg="green",height=2,width=3).place(x=100+50,y=120)
            c2="5"

        elif color2=="Blue":
            Label(root,text="",bg="blue",height=2,width=3).place(x=100+50,y=120)
            c2="6"
        elif color2=="Violet":
            Label(root,text="",bg="purple",height=2,width=3).place(x=100+50,y=120)
            c2="7"
        elif color2=="Gray":
            Label(root,text="",bg="gray",height=2,width=3).place(x=100+50,y=120)
            c2="8"
        elif color2=="White":
            Label(root,text="",bg="white",height=2,width=3).place(x=100+50,y=120)
            c2="9"



        Label(root, text=f'Valor de resistencia {c1} {c2} ohms').place(x=10, y=300)
        
      
            
            

    
    
    list1 = ttk.Combobox(root, values=["1","2","3","4","5","6","7","8","9","10","11","12"],width=10)
    

    # get first 3 letters of every month name
    list1['values'] = ('Black', 'Brown','Red','Orange','Yellow' ,'Green','Blue','Violet','Gray','White')
    list2=ttk.Combobox(root, values=["Black","Brown","Red","Orange","Yellow","Green","Blue","Violet","Gray","White"],width=10)
    # prevent typing a value
    list1['state'] = 'readonly'
    list2['state'] = 'readonly'
    list1.current(0)
    list2.current(0)
    

    # place the widget
    list1.place(x=10, y=200)
    list2.place(x=100, y=200)
    Button(root, text="Cambiar", command=cambiar).place(x=10, y=250)
    
    

   
    


