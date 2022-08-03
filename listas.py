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
        xplace=95
        csum=StringVar()
        color1=str(list1.get())
        if list1.get()!= 0:
            Label(root,text="",bg=color1,height=2,width=3).place(x=xplace,y=120)
            c1=list1['values'].index(list1.get())
    

        color2=str(list2.get())
        if list2!= 0:
            Label(root,text="",bg=color2,height=2,width=3).place(x=xplace*2,y=120)
            c2=list2['values'].index(list2.get())

        color3=str(list3.get())

        if list3!= 0:
            Label(root,text="",bg=color3,height=2,width=3).place(x=xplace*3,y=120)
            c3=list3['values'].index(list3.get())




        

        color4=str(list4.get())
        if list4!= 0:
            Label(root,text="",bg=color4,height=2,width=3).place(x=xplace*4,y=120)
            c4=list4['values'].index(list4.get())
            values=[1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,0.1,0.01]

        color5=str(list5.get())
        if list5!= 0:
            Label(root,text="",bg=color5,height=2,width=3).place(x=xplace*5,y=120)
            c5=list5['values'].index(list5.get())
            values2=["1%","2%","4%","0.5%","0.25%","0.1%","0.05%","5%","10%"]

        csum=str(c1)+str(c2)
        csum=csum+str(c3)
        csum=float(csum)
        csum=str(csum*values[c4])
        csum=float(csum)
        if 1000<csum<999999:
            csum=str(csum/1000)
            csum=str(csum)+"K"

        elif csum>=1000000:
            csum=str(csum/1000000)
            csum=str(csum)+"M"

        else:
            csum=str(csum)

        csum=str(csum)+" Ω"+"\n"+str(values2[c5])
        
        def resultado(csum):
            Label(root,text="Value: "+str(csum)  ,bg="white",height=2,width=20,anchor="center",font=("Arial",18)).place(x=90,y=300)
            


            


        resultado(csum)
        
        
            
            

           

          

            
        



        
      
    
        
      
            
            

    
    
    list1 = ttk.Combobox(root, values=["1","2","3","4","5","6","7","8","9","10","11","12"],width=10)
    

    # get first 3 letters of every month name
    list1['values'] = ('Black', 'Brown','Red','Orange','Yellow' ,'Green','Blue','Violet','Gray','White')
    list2=ttk.Combobox(root, values=["Black","Brown","Red","Orange","Yellow","Green","Blue","Violet","Gray","White"],width=10)
    list3=ttk.Combobox(root, values=["Black","Brown","Red","Orange","Yellow","Green","Blue","Violet","Gray","White"],width=10)

    list4=ttk.Combobox(root, values=["Black","Brown","Red","Orange","Yellow","Green","Blue","Violet","Gray","White","Gold","Silver"],width=10)

    list5=ttk.Combobox(root, values=["Brown","Red","Yellow","Green","Blue","Violet","Gray","Gold","Silver"],width=10)
    # prevent typing a value
    list1['state'] = 'readonly'
    list2['state'] = 'readonly'
    list3['state'] = 'readonly'
    list4['state'] = 'readonly'
    list5['state'] = 'readonly'
    list1.current(0)
    list2.current(0)
    list3.current(0)
    list4.current(0)
    list5.current(0)
    

    # place the widget
    newsize=90
    list1.place(x=newsize, y=200)
    list2.place(x=newsize*2, y=200)
    list3.place(x=newsize*3, y=200)
    list4.place(x=newsize*4, y=200)
    list5.place(x=newsize*5, y=200)
    Button(root, text="Calculate", command=cambiar,height=3,width=50,font=("Arial",11),borderwidth=4,bg='white').place(x=90, y=228)
    
    

   
    


