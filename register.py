import tkinter as tk
from tkinter import messagebox
from create import CreateAccount
import json

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.geometry('500x400')
        self.root.title('Login Form')

        frame_login = tk.Frame(self.root, bg="pink", padx=20, pady=20)
        frame_login.place(relx=0.5, rely=0.5, anchor='center')

        title_label = tk.Label(frame_login, text="Login Area", font=("Impact", 25, "bold"), bg="white", fg="black")
        title_label.pack()

        self.username_label = tk.Label(frame_login, text="Username:", font=("courier new", 12), bg="white", fg="black")
        self.username_label.pack(anchor='w', padx=0, pady=5)

        self.username_entry = tk.Entry(frame_login, font=("courier new", 12))
        self.username_entry.pack(pady=5, fill=tk.X)

        self.password_label = tk.Label(frame_login, text="Password:", font=("courier new", 12), bg="white", fg="black")
        self.password_label.pack(anchor='w')

        self.password_entry = tk.Entry(frame_login, font=("courier new", 12), show='*')
        self.password_entry.pack(pady=5, fill=tk.X)

        login_button = tk.Button(frame_login, text="Login", font=("courier new", 12), bg="white", fg="black", command=self.login)
        login_button.pack(pady=20, fill=tk.X)

        create_account_button = tk.Button(frame_login, text="Create an account?", bg="white", fg="pink", command=self.open_create_account)
        create_account_button.pack(pady=10, fill=tk.X)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password.")
            return

        try:
            with open('account.json', 'r') as file:
                data = json.load(file)

            for user in data:
                if user.get('Username') == username and user.get('Password') == password:
                    messagebox.showinfo("Success", "Login successful!")
                    return

            messagebox.showerror("Error", "Invalid username or password.")

        except FileNotFoundError:
            messagebox.showerror("Error", "Account data not found.")

    def open_create_account(self):
        create_account_window = tk.Toplevel(self.root)
        create_account_window.title("Create Account")
        create_account_form = CreateAccount(create_account_window)


if __name__ == "__main__":
    root = tk.Tk()
    login_form = LoginForm(root)
    root.mainloop()
