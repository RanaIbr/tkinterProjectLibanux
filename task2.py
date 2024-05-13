import math
from tkinter import *
from tkinter import ttk
r = Tk()
r.title('Counting Seconds')
r.geometry('500x500')
num_var=StringVar()
result_var=StringVar()
def is_prime(N):
            if N <= 1:
                return False
            for i in range(2, int(math.sqrt(N))+1):
                if N % i == 0:
                    return False
            return True


def submit():
    name = num_var.get()
    if is_prime(int(name)):
        result_var.set(name+' is a prime number')
        num_var.set('')
    else:
        result_var.set(name+' is not a prime number')
        num_var.set('')

labelT=ttk.Label(r,text='Enter number')
labelT.pack()
inputT=ttk.Entry(r,width=25,textvariable=num_var)
inputT.pack()

button = ttk.Button(r, text='Submit', width=25, command=submit)
button.pack()
lableresultT=ttk.Label(r,text='Result',textvariable=result_var)
lableresultT.pack()
exit = ttk.Button(r, text='Exit', width=25, command=exit)
exit.pack()
r.mainloop()


