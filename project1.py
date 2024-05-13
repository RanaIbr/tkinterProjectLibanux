from tkinter import *
import tkinter as tk
from tkinter import messagebox
r = tk.Tk()
r.geometry('300x300')
r.title('Registration Form')
r.configure(bg="pink")
custom_font = ("courier new 20", 15)

def login():
        username = input1.get()
        password = input2.get()

        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

def create_account():

        account_window = tk.Toplevel(r)
        account_window.geometry('400x400')
        account_window.title('Create Account')

        custom_font = ("courier new", 16)


        label_title = tk.Label(account_window, text="Create Your Account", font=("courier new", 20, "bold"), fg="black")
        label_title.pack(pady=20)

        label_username = tk.Label(account_window, text="Username:", font=custom_font, fg="black")
        label_username.pack(pady=10)

        entry_username = tk.Entry(account_window, font=custom_font)
        entry_username.pack(pady=5)

        label_email = tk.Label(account_window, text="Email:", font=custom_font, fg="black")
        label_email.pack(pady=10)

        entry_email = tk.Entry(account_window, font=custom_font)
        entry_email.pack(pady=5)

        label_password = tk.Label(account_window, text="Password:", font=custom_font, fg="black")
        label_password.pack(pady=10)

        entry_password = tk.Entry(account_window, font=custom_font, show='*')
        entry_password.pack(pady=5)

        def submit_account():
                username = entry_username.get()
                email = entry_email.get()
                password = entry_password.get()
                print(f"Creating account with username: {username}, email: {email}, password: {password}")
                account_window.destroy()

        submit_button = tk.Button(account_window, text="Create Account", font=custom_font, bg="pink", fg="white",
                                  command=submit_account)
        submit_button.pack(pady=20)


label1 = tk.Label(r, text="User name", fg="white", bg="pink", font=custom_font)
label1.grid(row=0, column=0, padx=10, pady=10, sticky='w')

input1 = tk.Entry(r, bg="white", fg="black", font=custom_font)
input1.grid(row=1, column=0, padx=10, pady=1, sticky='w')

label2 = tk.Label(r, text="Password", fg="white", bg="pink", font=custom_font)
label2.grid(row=2, column=0, padx=10, pady=10, sticky='w')

input2 = tk.Entry(r, bg="white", fg="black", font=custom_font)
input2.grid(row=3, column=0, padx=10, pady=1, sticky='w')

login_button = tk.Button(r, text="login", fg="pink", bg="white", font=custom_font)
login_button.grid(row=4, column=0, padx=70, pady=10, sticky='w')

create_account_button = tk.Button(r, text="Create an account?", bg="white", fg="pink", command=create_account, font=custom_font)
create_account_button.grid(row=5, column=0, padx=10, pady=10, sticky='w')
r.mainloop()
