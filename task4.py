from tkinter import *
from tkinter import ttk
r = Tk()
r.geometry('400x200')
r.title('String Replacement')

def replace_text():
    input_text = text_entry.get()
    output_text = input_text.replace("python", "wait").replace("java", "python").replace("wait", "java")
    output.delete(1.0, END)
    output.insert(END, output_text)

label = ttk.Label(r, text="Input a text with 'Python' and 'Java':")
label.pack()

text_entry = ttk.Entry(r, width=50)
text_entry.pack()

replace_button = ttk.Button(r, text="Replace", command=replace_text)
replace_button.pack()

output = Text(r, height=5, width=40)
output.pack(pady=10)

r.mainloop()


