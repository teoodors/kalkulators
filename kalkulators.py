from tkinter import *

mansLogs = Tk()
mansLogs.title('Kalkulators')

e = Entry(mansLogs, width=15, bd=40, font=('Arial Black', 25),bg='#FFC0CB', justify='right')
e.grid(row=0, column=0, columnspan=4)

def btnClick(number):
    current = e.get()
    e.delete(0, END)
    newNumber = str(current) + str(number)
    e.insert(0, newNumber)

def btnCommand(command):
    global num1
    global mathOp
    num1 = int(e.get())
    mathOp = command
    e.delete(0, END)

def Vienads():
    num2 = int(e.get())
    result = 0
    if mathOp == "+":
        result = num1 + num2
    elif mathOp == "-":
        result = num1 - num2
    elif mathOp == "*":
        result = num1 * num2
    elif mathOp == "/":
        result = num1 / num2
    e.delete(0, END)
    e.insert(0, str(result))

def notirit():
    e.delete(0, END)
    global num1, mathOp
    num1 = 0
    mathOp = ""

btn0 = Button(mansLogs, text='0', padx='40', pady='20', command=lambda:btnClick(0),bg='#FF00FF',font=('New Times Roman',20),bd = 10)
btn1 = Button(mansLogs, text='1', padx='40', pady='20', command=lambda:btnClick(1),bg='#FF00FF',font=('New Times Roman',20),bd = 10)
btn2 = Button(mansLogs, text='2', padx='40', pady='20', command=lambda:btnClick(2),bg='#FF00FF',font=('New Times Roman',20),bd = 10)
btn3 = Button(mansLogs, text='3', padx='40', pady='20', command=lambda:btnClick(3),bg='#FF00FF',font=('New Times Roman',20),bd = 10)
btn4 = Button(mansLogs, text='4', padx='40', pady='20', command=lambda:btnClick(4),bg='#FF00FF',font=('New Times Roman',20),bd = 10)
btn5 = Button(mansLogs, text='5', padx='40', pady='20', command=lambda:btnClick(5),bg='#FF00FF',font=('New Times Roman',20),bd = 10)
btn6 = Button(mansLogs, text='6', padx='40', pady='20', command=lambda:btnClick(6),bg='#FF00FF',font=('New Times Roman',20),bd = 10)
btn7 = Button(mansLogs, text='7', padx='40', pady='20', command=lambda:btnClick(7),bg='#FF00FF',font=('New Times Roman',20),bd = 10)
btn8 = Button(mansLogs, text='8', padx='40', pady='20', command=lambda:btnClick(8),bg='#FF00FF',font=('New Times Roman',20),bd = 10)
btn9 = Button(mansLogs, text='9', padx='40', pady='20', command=lambda:btnClick(9),bg='#FF00FF',font=('New Times Roman',20),bd = 10)

btnSask = Button(mansLogs, text='+', padx='40', pady='20', command=lambda:btnCommand('+'),bg='#A020F0',font=('New Times Roman',20),bd = 10)
btnMin = Button(mansLogs, text='-', padx='40', pady='20', command=lambda:btnCommand('-'),bg='#A020F0',font=('New Times Roman',20),bd = 10)
btnReiz = Button(mansLogs, text='*', padx='40', pady='20', command=lambda:btnCommand('*'),bg='#A020F0',font=('New Times Roman',20),bd = 10)
btnDal = Button(mansLogs, text='/', padx='40', pady='20', command=lambda:btnCommand('/'),bg='#A020F0',font=('New Times Roman',20),bd = 10)
btnC = Button(mansLogs, text='C', padx='40', pady='20', command=notirit,bg='#A020F0',font=('New Times Roman',20),bd = 10)
btnVien = Button(mansLogs, text='=', padx='40', pady='20', command=Vienads,bg='#A020F0',font=('New Times Roman',20),bd = 10)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btnSask.grid(row=1, column=3)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btnMin.grid(row=2, column=3)

btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btnReiz.grid(row=3, column=3)

btn0.grid(row=4, column=0)
btnC.grid(row=4, column=1)
btnVien.grid(row=4, column=2)
btnDal.grid(row=4, column=3)

mansLogs.mainloop()
