from tkinter import *
from tkinter import ttk
r = Tk()
r.title('Replacement')
r.geometry('500x500')

def click():
    input_text = text_entry.get()
    output_text = '*' * (len(input_text) - 5) + input_text[-5:]
    output.delete('1.0', END)
    output.insert(END, output_text)
label = ttk.Label(r, text="Enter a string:")
label.pack()

text_entry = ttk.Entry(r, width=50)
text_entry.pack()

button = ttk.Button(r, text='Click', width=25, command=click)
button.pack()

label = ttk.Label(r, text="Replacement:")
label.pack()
output = Text(r, height=1, width=40, foreground='magenta4')
output.pack(pady=10)
r.mainloop()