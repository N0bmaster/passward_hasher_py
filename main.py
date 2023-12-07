import tkinter as tk
from tkinter import *
import hashlib
import 

def hasher():
    password = enter_passwrd.get()
    encoded_password = password.encode('utf-8')
    sha256_hash = hashlib.sha256(encoded_password).hexdigest()

    # Update label text with the new hash value
    label2.config(text=f"Hashed Password: {sha256_hash}")

def reset_password_field(event=None):
    enter_passwrd.delete(0, tk.END)  # Clear the entry field

root = tk.Tk()
root.title("Password Hasher")
root.geometry("1080x380")  # Larger window size

# Apply the 'clam' theme for a more modern look
style = ttk.Style()
style.theme_use('clam')

# Configure style to change colors, font, and increase size
style.configure('TFrame', background='#f0f0f0', borderwidth=5, relief=tk.RIDGE)
style.configure('TLabel', background='#f0f0f0', font=('Arial', 16), foreground='#333')
style.configure('TButton', background='#4caf50', foreground='white', font=('Arial', 14))

# Create and place widgets
frame = ttk.Frame(root, style='TFrame')
frame.pack(padx=20, pady=20)

label = ttk.Label(frame, text="Enter Password:", style='TLabel')
enter_passwrd = ttk.Entry(frame, show='*', font=('Arial', 14))
button = ttk.Button(frame, text="Hash", command=hasher, style='TButton')

label.grid(row=0, column=0, pady=10)
enter_passwrd.grid(row=1, column=0, pady=10)
button.grid(row=2, column=0, pady=20)

# Create label to display hash
label2 = ttk.Label(root, text="", wraplength=780, font=('Arial', 14), relief=tk.RIDGE)
label2.pack()

# Bind Enter key to the hasher function and reset password field
root.bind('<Return>', lambda event=None: [hasher(), reset_password_field()])

root.mainloop()
