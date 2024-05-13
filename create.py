from tkinter import *
import tkinter as tk
import json
from tkinter import messagebox
custom_font = ("courier new 20", 15)

class CreateAccount:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('Create Account')
        self.background_image = tk.PhotoImage(file="C:\\Users\\User\\OneDrive\\Desktop\\login.png")

        self.canvas = Canvas(self.root, width=2000, height=2000)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.background_image, anchor='nw')

        label_titles = [("Create Your Account", 50), ("First Name", 130), ("Last Name", 180),
                        ("Username", 230), ("Email", 280), ("Password", 330)]

        for text, y_coord in label_titles:
            label = tk.Label(self.root, text=text, font=("courier new", 12, "bold"), fg="black")
            label.place(x=200, y=y_coord, anchor='center')

        self.entry_firstname = tk.Entry(self.root, font=("courier new", 12))
        self.entry_firstname.place(x=380, y=130, anchor='center')

        self.entry_lastname = tk.Entry(self.root, font=("courier new", 12))
        self.entry_lastname.place(x=380, y=180, anchor='center')

        self.entry_username = tk.Entry(self.root, font=("courier new", 12))
        self.entry_username.place(x=380, y=230, anchor='center')

        self.entry_email = tk.Entry(self.root, font=("courier new", 12))
        self.entry_email.place(x=380, y=280, anchor='center')

        self.entry_password = tk.Entry(self.root, font=("courier new", 12), show='*')
        self.entry_password.place(x=380, y=330, anchor='center')

        self.button_submit = tk.Button(self.root, text="Create account", font=("courier new", 12), command=self.create_account)
        self.button_submit.place(x=380, y=380, anchor='center')

    def create_account(self):
        firstname = self.entry_firstname.get()
        lastname = self.entry_lastname.get()
        username = self.entry_username.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        if firstname and lastname and username and email and password:
            account_data = {
                "First Name": firstname,
                "Last Name": lastname,
                "Username": username,
                "Email": email,
                "Password": password
            }

            if self.save_account(account_data):
                messagebox.showinfo("Success", "Account created and saved successfully!")
                self.clear_entries()
            else:
                messagebox.showerror("Error", "Failed to save account.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def save_account(self, account_data, filename='account.json'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append(account_data)

        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
            return True

    def clear_entries(self):
        self.entry_firstname.delete(0, 'end')
        self.entry_lastname.delete(0, 'end')
        self.entry_username.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.entry_password.delete(0, 'end')





























'''from tkinter import *
import tkinter as tk
import json
from tkinter import messagebox
from json.decoder import JSONDecodeError

custom_font = ("courier new 20", 15)

class CreateAccount:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('Create Account')
        self.background_image = tk.PhotoImage(file="C:\\Users\\User\\OneDrive\\Desktop\\login.png")

        self.canvas = Canvas(self.root, width=2000, height=2000)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.background_image, anchor='nw')

        label_titles = [("Create Your Account", 50), ("First Name", 130), ("Last Name", 180),
                        ("Username", 230), ("Email", 280), ("Password", 330)]

        for text, y_coord in label_titles:
            label = tk.Label(self.root, text=text, font=("courier new", 12, "bold"), fg="black")
            label.place(x=200, y=y_coord, anchor='center')

        self.entry_firstname = tk.Entry(self.root, font=("courier new", 12))
        self.entry_firstname.place(x=380, y=130, anchor='center')

        self.entry_lastname = tk.Entry(self.root, font=("courier new", 12))
        self.entry_lastname.place(x=380, y=180, anchor='center')

        self.entry_username = tk.Entry(self.root, font=("courier new", 12))
        self.entry_username.place(x=380, y=230, anchor='center')

        self.entry_email = tk.Entry(self.root, font=("courier new", 12))
        self.entry_email.place(x=380, y=280, anchor='center')

        self.entry_password = tk.Entry(self.root, font=("courier new", 12), show='*')
        self.entry_password.place(x=380, y=330, anchor='center')

        self.button_submit = tk.Button(self.root, text="Create account", font=("courier new", 12), command=self.create_account)
        self.button_submit.place(x=380, y=380, anchor='center')


    def create_account(self, firstname, lastname, username, email, password):
        if firstname and lastname and username and email and password:
            account_data = {
                "Users": [
                    {
                        "First Name": firstname,
                        "Last Name": lastname,
                        "Username": username,
                        "Email": email,
                        "Password": password
                    }
                ]
            }

            print(json.dumps(account_data, indent=4))
            if self.save_account(account_data):
                messagebox.showinfo("Success", "Account created and saved successfully!")
                self.clear_entries()
            else:
                messagebox.showerror("Error", "Failed to save account.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def reading(self):
            with open("account.json") as data_file:
                old_data = json.load(data_file)
                print(old_data)

    def writing():
            with open("account.json", "w") as write_file:
                json.dump(account_data, write_file)

    def appending():
            with open("account.json", "a") as write_file:
                json.dump(account_data, write_file)
                write_file.close()
                print(account_data)

                with open("data_file.json", "a") as write_file:
                    json.dump(account_data, write_file)

    def save_account(self, account_data, filename='account.json'):

            try:
                with open(filename, mode='r') as file:
                    data = json.load(file)

                    data.update(account_data)

                # with open(filename, mode='w') as file:
                #     data.dump(data, file, indent=4)
                    print(data)
                return True
            except JSONDecodeError as e:
                print(e.msg)
                pass

    def clear_entries(self):
        self.entry_firstname.delete(0, 'end')
        self.entry_lastname.delete(0, 'end')
        self.entry_username.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.entry_password.delete(0, 'end')'''

