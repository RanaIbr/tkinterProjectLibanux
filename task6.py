from tkinter import *
from tkinter import ttk
r = Tk()
r.title('Reversed String')
r.geometry('500x500')
s = StringVar()

def click():
   input_str = text_entry.get()
   reversed_str = ""
   index = len(input_str) - 1
   while index >= 0:
       reversed_str += input_str[index]
       index -= 1
   output.delete(1.0, END)
   output.insert(END, reversed_str)

label = ttk.Label(r, text="Enter a string:")
label.pack()

text_entry = ttk.Entry(r, width=50)
text_entry.pack()

button = ttk.Button(r, text='Reverse', width=25, command=click)
button.pack()

label = ttk.Label(r, text="Reversed string:")
label.pack()

output = Text(r, height=1, width=40)
output.pack(pady=10)

r.mainloop()