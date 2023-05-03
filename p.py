import tkinter as tk

def check_login():
    # Replace with actual login authentication logic
    if username_entry.get() == "admin" and password_entry.get() == "password":
        status_label.config(text="Login Successful", fg="green")
    else:
        status_label.config(text="Invalid Credentials", fg="red")

# Create a new Tkinter window
root = tk.Tk()
root.title("Login Page")
root.geometry("800x600")
# Create a label for the username field
username_label = tk.Label(root, text="Username:")
username_label.pack()

# Create an entry field for the username
username_entry = tk.Entry(root)
username_entry.pack()

# Create a label for the password field
password_label = tk.Label(root, text="Password:")
password_label.pack()

# Create an entry field for the password
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create a button to submit the login credentials
submit_button = tk.Button(root, text="Login", command=check_login)
submit_button.pack()

# Create a label to display the login status
status_label = tk.Label(root, text="")
status_label.pack()

# Run the main event loop
root.mainloop()
