#!/usr/bin/python

#**************************
import tkinter as tk
from tkinter import messagebox
import sys


#create class ****************************************************
class simpleapp_tk(tk.Tk):
    
    #function
    def __init__(self,parent):
        tk.Tk.__init__(self,parent)
        #keep track of parent
        self.parent = parent
        self.initialize()

    #initialize gui
    def initialize(self):
        self.grid()  
        
        #INSERT DATA**********************************************
        self.entryVariable = tk.StringVar()
        self.entry = tk.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entryVariable.set(u"Enter text here.")
    
        self.entryVariable1 = tk.StringVar()
        self.entry1 = tk.Entry(self,textvariable=self.entryVariable1)
        self.entry1.grid(column=1,row=0,sticky='EW')
        self.entryVariable1.set(u"Enter text here.")
        
        self.entryVariable2 = tk.StringVar()
        self.entry2 = tk.Entry(self,textvariable=self.entryVariable2)
        self.entry2.grid(column=2,row=0,sticky='EW')
        self.entryVariable2.set(u"Enter text here.")
        
        #LISTENERS*************************************************
        self.entry.bind("<Return>", self.OnPressEnter) 
        self.entry1.bind("<Return>", self.OnPressEnter1)
        self.entry2.bind("<Return>", self.OnPressEnter2)
        
        #BUTTON*****************************************************
        button1 = tk.Button(self,text=u"CHECK THE RESULT!!", command=self.OnButtonClick)
        button1.grid(column=1,row=2)
        
        #LABEL******************************************************
        self.labelVariable = tk.StringVar()
        label = tk.Label(self,textvariable=self.labelVariable,anchor="w",fg="white",bg="red")
        label.grid(column=0,row=1,columnspan=1,sticky='EW')
        self.labelVariable.set(u"[value X]")
        
        self.labelVariable1 = tk.StringVar()
        label = tk.Label(self,textvariable=self.labelVariable1,anchor="w",fg="black",bg="yellow")
        label.grid(column=1,row=1,columnspan=1,sticky='EW')
        self.labelVariable1.set(u"[value Y]")
        
        self.labelVariable2 = tk.StringVar()
        label = tk.Label(self,textvariable=self.labelVariable2,anchor="w",fg="white",bg="green")
        label.grid(column=2,row=1,columnspan=1,sticky='EW')
        self.labelVariable2.set(u"[value TOTAL]")
               
        #WINDOW*********************************************************
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry("400x300")     
        self.entry.focus_set()
        self.entry.selection_range(0, tk.END)
    
    #Action: enter keyboard
    def OnPressEnter(self,event):
        #UPDATE LABELS
        self.labelVariable.set("[value X] = "+self.entryVariable.get())
        #FOCUS
        self.entry1.focus_set()
        self.entry1.selection_range(0, tk.END)

    #Action: enter keyboard
    def OnPressEnter1(self,event):
        self.labelVariable1.set("[value Y] = "+self.entryVariable1.get())
        #FOCUS
        self.entry2.focus_set()
        self.entry2.selection_range(0, tk.END)
        
    #Action: enter keyboard
    def OnPressEnter2(self,event):
        self.labelVariable2.set("[value TOTAL] = "+self.entryVariable2.get())  

    
    #ACTION: button click
    def OnButtonClick(self):
        #print ("You clicked the button !")
        #self.labelVariable1.set("[value Y] = "+self.entryVariable1.get())
        
        #USER
        x = self.entry.get()      
        y = self.entry1.get() 
        sumUser = self.entry2.get() 
         
        #OPERATION (+, -, *, /, %, **, //)
        sumPython = int(x) + int(y)
        
        #CONDITIONS AND PRINT
        print("")
        if ( int(sumUser)  == sumPython ) : 
            print ("VALUES : " + "x = " + '{}'.format(x) + "; " + "y = " + '{}'.format(y) + "; ")
            print ("OPERATION : " + '{} '.format(x) + "+ " + '{} '.format(y) + "= " + '{} '.format(sumPython) )
            print ("CONGRATS!!! THAT IS THE SPIRIT!!!")
            messagebox.showinfo( "Hello Python", "CONGRATS!! THAT IS CORRECT!!", icon="warning")  

        else :
            print ("sumUser = " + '{} '.format(sumUser) + "; sumPython = " + '{} '.format(sumPython) )
            print ("NOT CORRECT... TRY AGAIN...")
            
            #CLEAN ENTRY
            self.entryVariable.set(u"")
            self.entryVariable1.set(u"")
            self.entryVariable2.set(u"")
            self.labelVariable.set("[value X] = ")
            self.labelVariable1.set("[value Y] = ")
            self.labelVariable2.set("[value TOTAL] = ")  
            
            #FOCUS
            self.entry.focus_set()
            self.entry.selection_range(0, tk.END)

    
#**************************   
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('MIGUEL MATH IS MY FAVORITE SUBJECT!!')
    app.mainloop()
  