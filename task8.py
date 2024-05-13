import tkinter as tk
from tkinter import messagebox
from datetime import datetime
r = tk.Tk()
r.title("Date Converter")
r.geometry('500x500')

def is_valid_date(input_date):
    if len(input_date) != 10:
        return False
    parts = input_date.split('-')
    if len(parts) != 3:
        return False
    try:
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        datetime(year, month, day)
        return True
    except ValueError:
        return False

def convertdate(input_date):
    if is_valid_date(input_date):
        date_obj = datetime.strptime(input_date, "%Y-%m-%d")
        output_date = date_obj.strftime("%d-%m-%Y")
        return output_date
    else:
        return None

def handle_conversion():
    input_date = entry.get()
    output_date = convertdate(input_date)
    if output_date:
        result_label.config(text=f"Converted Date: {output_date}")
    else:
        messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")


label = tk.Label(r, text="Enter Date (YYYY-MM-DD):")
label.pack(pady=10)

entry = tk.Entry(r, width=20)
entry.pack(pady=5)

convert_button = tk.Button(r, text="Convert", command=handle_conversion)
convert_button.pack(pady=10)

result_label = tk.Label(r, text="")
result_label.pack(pady=10)

r.mainloop()

