from tkinter import *
import tkinter as tk
import json
from tkinter import messagebox


class CreateAccount:
    def __init__(self, root):
        self.root = root
        self.root.geometry('600x500')
        self.root.title('Create Account')

        # Background Image
        self.background_image = tk.PhotoImage(file="C:\\Users\\User\\OneDrive\\Desktop\\login.png")
        self.canvas = Canvas(self.root, width=600, height=500)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.background_image, anchor='nw')

        # Label Titles
        label_titles = [("Create Your Account", 50), ("First Name", 130), ("Last Name", 180),
                        ("Username", 230), ("Email", 280), ("Password", 330)]

        for text, y_coord in label_titles:
            label = tk.Label(self.root, text=text, font=("courier new", 12, "bold"), fg="black")
            label.place(x=300, y=y_coord, anchor='center')

        # Entry Fields
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

        # Submit Button
        self.button_submit = tk.Button(self.root, text="Create Account", font=("courier new", 12),
                                       command=self.create_account)
        self.button_submit.place(x=300, y=380, anchor='center')

    def create_account(self):
        # Get user input from entry fields
        firstname = self.entry_firstname.get()
        lastname = self.entry_lastname.get()
        username = self.entry_username.get()
        email = self.entry_email.get()
        password = self.entry_password.get()

        # Validate if all fields are filled
        if firstname and lastname and username and email and password:
            account_data = {
                "First Name": firstname,
                "Last Name": lastname,
                "Username": username,
                "Email": email,
                "Password": password
            }

            # Save account data to JSON file
            if self.save_account(account_data):
                messagebox.showinfo("Success", "Account created and saved successfully!")
                # Optionally, clear entry fields after successful submission
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
        # Clear all entry fields
        self.entry_firstname.delete(0, 'end')
        self.entry_lastname.delete(0, 'end')
        self.entry_username.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.entry_password.delete(0, 'end')


if __name__ == "__main__":
    r = tk.Tk()
    create_account = CreateAccount(r)
    r.mainloop()
