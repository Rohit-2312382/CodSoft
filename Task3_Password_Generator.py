import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        # Get the desired length from the user
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length must be greater than 0.")

        # Get complexity options
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_specials = specials_var.get()

        # Create a pool of characters based on user selection
        char_pool = ""
        if use_letters:
            char_pool += string.ascii_letters
        if use_numbers:
            char_pool += string.digits
        if use_specials:
            char_pool += string.punctuation

        if not char_pool:
            raise ValueError("At least one character type must be selected.")

        # Generate the password
        password = "".join(random.choice(char_pool) for _ in range(length))

        # Display the password
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Title label
tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

# Length input
frame1 = tk.Frame(root)
frame1.pack(pady=5)
tk.Label(frame1, text="Password Length:").pack(side=tk.LEFT)
length_entry = tk.Entry(frame1, width=5)
length_entry.pack(side=tk.LEFT, padx=5)

# Options for complexity
frame2 = tk.Frame(root)
frame2.pack(pady=5)
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
specials_var = tk.BooleanVar(value=True)

letters_check = tk.Checkbutton(frame2, text="Letters", variable=letters_var)
letters_check.pack(side=tk.LEFT, padx=5)
numbers_check = tk.Checkbutton(frame2, text="Numbers", variable=numbers_var)
numbers_check.pack(side=tk.LEFT, padx=5)
specials_check = tk.Checkbutton(frame2, text="Special Characters", variable=specials_var)
specials_check.pack(side=tk.LEFT, padx=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Password output
frame3 = tk.Frame(root)
frame3.pack(pady=5)
password_entry = tk.Entry(frame3, width=30, font=("Arial", 12))
password_entry.pack(side=tk.LEFT)

# Run the main loop
root.mainloop()
