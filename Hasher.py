from tkinter import *
import hashlib
import customtkinter

def hasher():
    password = enter_passwrd.get()
    encoded_password = password.encode('utf-8')
    sha256_hash = hashlib.sha256(encoded_password).hexdigest()

    # Update label text with the new hash value
    label2.configure(text=f"Hashed Password: {sha256_hash}")

def reset_password_field(event=None):
    enter_passwrd.delete(0,customtkinter.END)  # Clear the entry field

root = customtkinter.CTk()
root.title("Password Hasher")
root.geometry("1080x380")  # Larger window size

# Apply the 'clam' theme for a more modern look

# Create and place widgets
frame = customtkinter.CTkFrame(root)
frame.pack(padx=20, pady=20)

label = customtkinter.CTkLabel(frame, text="Enter Password:")
enter_passwrd = customtkinter.CTkEntry(frame, show='*', font=('Arial', 14))
button = customtkinter.CTkButton(frame, text="Hash", command=hasher)

label.grid(row=0, column=0, pady=10)
enter_passwrd.grid(row=1, column=0, pady=10)
button.grid(row=2, column=0, pady=20)

# Create label to display hash
label2 = customtkinter.CTkLabel(root, text="", wraplength=780)
label2.pack()

# Bind Enter key to the hasher function and reset password field
root.bind('<Return>', lambda event=None: [hasher(), reset_password_field()])

root.mainloop()
