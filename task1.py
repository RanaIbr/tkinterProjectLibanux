from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from unittest import result
#hello world
r = Tk()
r.title('Arithmetic Operations')
r.geometry('400x500')
num_var = StringVar()
operation_var = StringVar(r, "Addition")


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        return "Error!."
    else:
        return num1 / num2


def printing(value):
    match value:
        case 0:
            print(value)
            operation_label.config(text="+")
        case 1:
            print(value)
            operation_label.config(text="-")
        case 2:
            print(value)
            operation_label.config(text="*")
        case 3:
            print(value)
            operation_label.config(text="/")


def submit():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    selected_operation = operation_var.get()

    '''while True:
            operation = input("Enter the operation (Addition, Subtraction, Multiplication, Division): ")
            if operation not in ['Addition', 'Subtraction', 'Multiplication', 'Division']:
                print("Invalid operation. Please try again.")
                continue'''
    match selected_operation:

        case 'Addition':
            result = addition(num1, num2)
            operation_label.config(text="+")
        case 'Subtraction':
            result = subtraction(num1, num2)
            operation_label.config(text="-")
        case 'Multiplication':
            result = multiplication(num1, num2)
            operation_label.config(text="*")
        case 'Division':
            result = division(num1, num2)
            operation_label.config(text="/")
    result_label.config(text="Result: " + str(result))
    messagebox.showinfo("Result", str(result))



def show_result_page():
    result_window = Toplevel(r)
    result_window.title("Result")
    result_label = ttk.Label(result_window, text="Result: " + str(result))
    result_label.pack()


def press(event):
    print(event)


label_num1 = ttk.Label(r, text='Enter first number:')
label_num1.pack()
entry_num1 = ttk.Entry(r, width=20)
entry_num1.pack()
operation_label = ttk.Label(r, text="", font=("Bold", 15))
operation_label.pack()
operation_label.config(text="+")
label_num2 = ttk.Label(r, text='Enter second number:')
label_num2.pack()
entry_num2 = ttk.Entry(r, width=20)
entry_num2.pack()
button = ttk.Button(r, text='Submit', width=25, command=submit)
button.pack()

result_label = ttk.Label(r, text="")
result_label.pack()
radio_frame = ttk.Frame(r)
radio_frame.pack(anchor=W)
radio_button1 = ttk.Radiobutton(r, text="Addition", variable=operation_var, value="Addition", command=lambda: printing(0))
radio_button1.pack(anchor=W)


radio_button2 = ttk.Radiobutton(r, text="Subtraction", variable=operation_var, value="Subtraction", command=lambda: printing(1))
radio_button2.pack(anchor=W)

radio_button3 = ttk.Radiobutton(r, text="Multiplication", variable=operation_var, value="Multiplication",
                                command=lambda: printing(2))
radio_button3.pack(anchor=W)

radio_button4 = ttk.Radiobutton(r, text="Division", variable=operation_var, value="Division", command=lambda: printing(3))
radio_button4.pack(anchor=W)

r.mainloop()
