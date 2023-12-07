import tkinter as tk
import hashlib

def hasher():
    password = enter_passwrd.get()
    encoded_password = password.encode('utf-8')
    sha256_hash = hashlib.sha256(encoded_password).hexdigest()

    label2.config(text=sha256_hash)

root = tk.Tk()
root.title("hasher_function")
root.geometry("640x480")
root.minsize(200, 200)
root.resizable(True, True)

label = tk.Label(root, text="Enter password: ")
enter_passwrd = tk.Entry(root)
button = tk.Button(root, text="Hash", command=hasher)

label.pack()
enter_passwrd.pack()
button.pack()


label2 = tk.Label(root, text="")
label2.pack()

root.mainloop()
