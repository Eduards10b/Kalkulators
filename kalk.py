from ast import operator
from cmath import e
from tkinter import*
from math import *
mLogs=Tk()
mLogs.title("Kalkulators")
#mLogs.geometry("300x300")
mLogs.config(bg="red")



def btnCommand(command):
    global num1
    global mathOp
    mathOp=command
    num1=int(e.get())
    e.delete(0,END)
    return 0


def btnClick(number):
    current=e.get()#nolasa esošo skaitli
    e.delete(0,END)#nodzēš
    newNumber=str(current)+str(number)
    e.insert(0,newNumber)#ievieto displeja
    return 0

def vienads():
    global num2
    num2=(int(e.get()))
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp=="/":
        result=num1/num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="%":
        result=num1*0.01*num2
    else:
        result=0
    e.delete(0,END)            
    e.insert(0,str(result))
    return 0

def notirit():
    e.delete(0,END)
    num=1
    mathOp=''
    return 0

def sr():
    global operator
    global num1 
    num1=(int(e.get()))
    num1=sqrt(num1)
    e.delete(0,END)
    e.insert(0,num1)
    return 0


def kv():
    global operator
    global num1
    num1=(float(e.get()))
    num1=num1**2
    e.delete(0,END)
    e.insert(0,num1)
    return 0


def logar():
    global operator
    global num1
    num1=(float(e.get()))
    num1=log(num1,81)
    e.delete(0,END)
    e.insert(0,num1)
    return 0






e=Entry(mLogs,width=15, bd=20,font=("Arial black",20))
e.grid(row=0,column=0,columnspan=4)

btn0=Button(mLogs, text="0",padx="40",pady="20",bg="black", fg="red",bd=10,command=lambda:btnClick(0))

btn1=Button(mLogs, text="1",padx="40",pady="20",bg="black",fg="red",bd=10,command=lambda:btnClick(1))

btn2=Button(mLogs, text="2",padx="40",pady="20",bg="black",fg="red",bd=10,command=lambda:btnClick(2))

btn3=Button(mLogs, text="3",padx="40",pady="20",bg="black",fg="red",bd=10,command=lambda:btnClick(3))

btn4=Button(mLogs, text="4",padx="40",pady="20",bg="black" ,fg="red",bd=10,command=lambda:btnClick(4))

btn5=Button(mLogs, text="5",padx="40",pady="20",bg="black",fg="red",bd=10,command=lambda:btnClick(5))

btn6=Button(mLogs, text="6",padx="40",pady="20",bg="black",fg="red",bd=10,command=lambda:btnClick(6))

btn7=Button(mLogs, text="7",padx="40",pady="20",bg="black",fg="red",bd=10,command=lambda:btnClick(7))

btn8=Button(mLogs, text="8",padx="40",pady="20",bg="black",fg="red",bd=10,command=lambda:btnClick(8))

btn9=Button(mLogs, text="9",padx="40",pady="20",bg="black",fg="red",bd=10,command=lambda:btnClick(9))




btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)
btn0.grid(row=4,column=0)

btn10=Button(mLogs, text="/",padx="40",pady="20",bg="black" ,fg="white",bd=10,command=lambda:btnCommand("/"))
btn11=Button(mLogs, text="x",padx="40",pady="20",bg="black",fg="white",bd=10,command=lambda:btnCommand("*"))
btn12=Button(mLogs, text="+",padx="40",pady="20",bg="black",fg="white",bd=10,command=lambda:btnCommand("+"))
btn13=Button(mLogs, text="-",padx="40",pady="20",bg="black",fg="white",bd=10,command=lambda:btnCommand("-"))
btn14=Button(mLogs, text="=",padx="40",pady="20",bg="black",fg="white",bd=10,command=vienads)
btn15=Button(mLogs, text="C",padx="40",pady="20",bg="black",fg="white",bd=10,command=notirit)
btn16=Button(mLogs, text="√",padx="40",pady="20",bg="black",fg="white",bd=10,command=sr)
btn17=Button(mLogs, text="x²",padx="40",pady="20",bg="black",fg="white",bd=10,command=kv)
btn18=Button(mLogs, text="log",padx="40",pady="20",bg="black",fg="white",bd=10,command=logar)
btn19=Button(mLogs, text="%",padx="40",pady="20",bg="black",fg="white",bd=10,command=lambda:btnCommand("%"))



btn10.grid(row=1,column=3)
btn11.grid(row=2,column=3)
btn12.grid(row=3,column=3)
btn13.grid(row=4,column=3)
btn14.grid(row=4,column=1)
btn15.grid(row=4,column=2)
btn16.grid(row=5,column=0)
btn17.grid(row=5,column=1)
btn18.grid(row=5,column=2)
btn19.grid(row=5,column=3)



mLogs.mainloop()
