import math
from tkinter import *
from tkinter import ttk
r = Tk()
r.title('Celsius to Fahrenheit')
r.geometry('500x500')
num_var=StringVar()
result_var=StringVar()

def convert(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

def submit():
    celsius = float(num_var.get())
    fahrenheit = convert(celsius)
    result_var.set(fahrenheit)



labelT=ttk.Label(r,text='Enter the Temperature in Celsius')
labelT.pack()
entry_num = ttk.Entry(r, width=20,textvariable=num_var)
entry_num.pack()

button = ttk.Button(r, text='Submit', width=25, command=submit)
button.pack()

labelT=ttk.Label(r,text='The Fahrenheit temperature is')
labelT.pack()
result_entry = ttk.Entry(r, width=20, textvariable=result_var, state='readonly')
result_entry.pack()

exit = ttk.Button(r, text='Exit', width=25, command=exit)
exit.pack()
r.mainloop()