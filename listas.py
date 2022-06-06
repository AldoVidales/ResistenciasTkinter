from calendar import month
import imp
from msilib.schema import ComboBox
import string
from time import time
from tkinter import *
from tkinter import ttk
from turtle import color

def scrollbar(root):

    def cambiar():
        
        csum=StringVar()
        color1=str(list1.get())
        if list1.get()!= 0:
            Label(root,text="",bg=color1,height=2,width=3).place(x=100,y=120)
            c1=list1['values'].index(list1.get())
    

        color2=str(list2.get())
        if list2!= 0:
            Label(root,text="",bg=color2,height=2,width=3).place(x=100+50,y=120)
            c2=list2['values'].index(list2.get())

        color4=str(list4.get())
        if list4!= 0:
            Label(root,text="",bg=color4,height=2,width=3).place(x=100+100,y=120)
            c3=list4['values'].index(list4.get())
            values=[1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]

        csum=str(c1)+str(c2)
        csum=int(csum)
        csum=str(csum*values[c3])
        csum=int(csum)
        def resultado(csum):
            Label(root,text="Resultado: "+str(csum),bg="white",height=2,width=20).place(x=10,y=300)


        resultado(csum)
        
        
            
            

           

          

            
        



        
      
    
        
      
            
            

    
    
    list1 = ttk.Combobox(root, values=["1","2","3","4","5","6","7","8","9","10","11","12"],width=10)
    

    # get first 3 letters of every month name
    list1['values'] = ('Black', 'Brown','Red','Orange','Yellow' ,'Green','Blue','Violet','Gray','White')
    list2=ttk.Combobox(root, values=["Black","Brown","Red","Orange","Yellow","Green","Blue","Violet","Gray","White"],width=10)

    list4=ttk.Combobox(root, values=["Black","Brown","Red","Orange","Yellow","Green","Blue","Violet","Gray","White"],width=10)
    # prevent typing a value
    list1['state'] = 'readonly'
    list2['state'] = 'readonly'
    list4['state'] = 'readonly'
    list1.current(0)
    list2.current(0)
    list4.current(0)
    

    # place the widget
    list1.place(x=10, y=200)
    list2.place(x=100, y=200)
    list4.place(x=200, y=200)
    Button(root, text="Cambiar", command=cambiar).place(x=10, y=250)
    
    

   
    


