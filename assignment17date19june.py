#solution 1 and 2
'''
from tkinter import Tk, Label, Button
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        self.label = Label(master, text="HELLO WORLD!")
        self.label.pack()
        self.greet_button = Button(master, text="CLICK IT", command=self.greet)
        self.greet_button.pack()
        self.close_button = Button(master, text="CLOSE", command=master.quit)
        self.close_button.pack()
    def greet(self):
        print("Greetings!")
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
'''
#solution 3

from tkinter import Tk, Label, Button
from tkinter import *
root=Tk()
frame=Frame(root)
frame.pack()
bottomframe=Frame(root)
bottomframe.pack(side = BOTTOM)
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("GUI-2")
        self.label = Label(master, text="this is a label")
        self.label.pack()
        self.greet_button = Button(master, text="CLICK IT", command=self.greet)
        self.greet_button.pack()
        self.close_button = Button(master, text="CLOSE", command=master.quit)
        self.close_button.pack()
    def greet(self):
        self.greet_button.config(text="updated text")
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

'''
#solution 4

from tkinter import *
master =Tk()
a=int(input(Label(master,text='Enter the number').grid(row=0)))
e1 = Entry(master)
e1.grid(row=0,column=1)
print(a)
mainloop()
'''
