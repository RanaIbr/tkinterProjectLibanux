import math
from tkinter import *
from tkinter import ttk
r = Tk()
r.title('Factorial')
r.geometry('500x500')
num_var=StringVar()
result_var=StringVar()

def factorial():
    try:
        n = int(num_var.get())
        if n <= 0:
            result_var.set("FACTORIAL FAILED BECAUSE IT IS NOT A POSITIVE NUMBER")
            num_var.set('')
            return

        result = 1
        while n > 1:
            result *= n
            n -= 1

        result_var.set("Factorial is " + str(result))
        num_var.set('')

    except ValueError:
        result_var.set("Please enter a valid integer")

labelT=ttk.Label(r,text='Enter number')
labelT.pack()
inputT=ttk.Entry(r,width=25,textvariable=num_var)
inputT.pack()

button = ttk.Button(r, text='Factorial', width=25, command=factorial)
button.pack()
lableresultT=ttk.Label(r,text='Result',textvariable=result_var)
lableresultT.pack()
exit = ttk.Button(r, text='Exit', width=25, command=exit)
exit.pack()
r.mainloop()