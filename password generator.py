import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, has_uppercase, has_lowercase, has_numbers, has_special_chars):
    password = ''
    characters = ''

    if has_uppercase:
        characters += string.ascii_uppercase
    if has_lowercase:
        characters += string.ascii_lowercase
    if has_numbers:
        characters += string.digits
    if has_special_chars:
        characters += string.punctuation

    for _ in range(length):
        password += random.choice(characters)

    return password

def generate_and_display_password():
    length = int(length_entry.get())
    has_uppercase = uppercase_var.get()
    has_lowercase = lowercase_var.get()
    has_numbers = numbers_var.get()
    has_special_chars = special_chars_var.get()

    password = generate_password(length, has_uppercase, has_lowercase, has_numbers, has_special_chars)
    password_label.config(text="Generated password: " + password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

length_label = tk.Label(root, text="Enter the length of the password:",font="comicsans 12 bold")
length_label.pack(padx=20,side="left")

length_entry = tk.Entry(root)
length_entry.pack(padx=20,side="left")

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(root, text="Include uppercase letters", variable=uppercase_var,font="comicsans 12 bold")
uppercase_checkbox.pack(padx=20,side="left",anchor='nw')

lowercase_var = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(root, text="Include lowercase letters", variable=lowercase_var,font="comicsans 12 bold")
lowercase_checkbox.pack(padx=20,side="left")

numbers_var = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(root, text="Include numbers", variable=numbers_var)
numbers_checkbox.pack(padx=20)

special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(root, text="Include special characters", variable=special_chars_var)
special_chars_checkbox.pack(padx=20)

generate_button = tk.Button(root, text="Generate password", command=generate_and_display_password)
generate_button.pack(padx=20)

password_label = tk.Label(root, text=" Generated password: ",font="comicsans 12 bold")
password_label.pack(padx=20)
root.mainloop()