import tkinter as tk
from tkinter import *
from tkinter import messagebox

def addNumbers():
    res=int(number1.get())+int(number2.get())
    myText.set(res)

def subNumbers():
    res=int(number1.get())-int(number2.get())
    myText.set(res)

def mulNumbers():
    res=int(number1.get())*int(number2.get())
    myText.set(res)

def divNumbers():
    res=int(number1.get())/int(number2.get())
    myText.set(res)

def Reset():
    num1=number1.get()
    num2=number2.get()
    sol=answer.get()
    file = open('History.txt','a')
    file.write(num1+ ','+ num2+'\n'+sol+'\n'+'\n')
    file.close()
    number1.delete(0,tk.END)
    number2.delete(0,tk.END)
    answer.delete(0,tk.END)

def End():
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        screen.destroy()

screen = tk.Tk()
myText = StringVar()
screen.title('Simple Calculator')
screen.geometry('400x350')
screen.configure(bg = '#848A8A')

tk.Label(screen,text= 'Enter Your First Number:',bg='black',fg='white',font=('Times new Roman',12)).place(x=20,y=10)
number1 = tk.Entry(screen,font = ('Times new roman',20))
number1.place(x=20,y=40)

tk.Label(screen,text= 'Enter Your Second Number:',bg='black',fg='white',font=('Times new Roman',12)).place(x=20,y=90)
number2 = tk.Entry(screen,font = ('Times new roman',20))
number2.place(x=20,y=120)

b1=tk.Button(screen,text='Add',bg='black',fg='white',font=('Times new roman',12), command=addNumbers).place(x=40,y=170)

b2=tk.Button(screen,text='Subtract',bg='black',fg='white',font=('Times new roman',12), command=subNumbers).place(x=90,y=170)

b3=tk.Button(screen,text='Multiply',bg='black',fg='white',font=('Times new roman',12), command=mulNumbers).place(x=165,y=170)

b4=tk.Button(screen,text='Divide',bg='black',fg='white',font=('Times new roman',12), command=divNumbers).place(x=235,y=170)

tk.Label(screen,text= 'Your Solution is:',bg='black',fg='white',font=('Times new Roman',12)).place(x=20,y=220)
answer = tk.Entry(screen,font = ('Times new roman',20), textvariable=myText)
answer.place(x=20,y=250)

tk.Button(screen,text='Reset',bg='black',fg='white',font=('Times new roman',12), command=Reset).place(x=100,y=290)

tk.Button(screen, text='End', bg='black',fg='white',font=('Times new roman',12), command=End).place(x=150,y=290)

screen.mainloop()
