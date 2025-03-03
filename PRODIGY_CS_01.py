import tkinter as tk
from tkinter import messagebox

# Function for Caesar Cipher encryption and decryption
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift_amount) % 26 + base)
            result += new_char
        else:
            result += char
    return result

# Function to handle encryption
def encrypt_text():
    text = entry_text.get()
    shift = entry_shift.get()
    if not shift.isdigit():
        messagebox.showerror("Input Error", "Shift value must be a number!")
        return
    shift = int(shift)
    result = caesar_cipher(text, shift, "encrypt")
    label_result.config(text=f"Encrypted: {result}", bg="#222831", fg="#EEEEEE")

# Function to handle decryption
def decrypt_text():
    text = entry_text.get()
    shift = entry_shift.get()
    if not shift.isdigit():
        messagebox.showerror("Input Error", "Shift value must be a number!")
        return
    shift = int(shift)
    result = caesar_cipher(text, shift, "decrypt")
    label_result.config(text=f"Decrypted: {result}", bg="#222831", fg="#EEEEEE")

# Create main GUI window
root = tk.Tk()
root.title("Caesar Cipher Encryptor & Decryptor")
root.geometry("550x450")  # Slightly larger
root.configure(bg="#222831")  # Darker cyber-style theme

# Styling
label_style = {"font": ("Hack", 12, "bold"), "bg": "#393E46", "fg": "#00ADB5"}
entry_style = {"bg": "#00ADB5", "fg": "#EEEEEE", "insertbackground": "white", "font": ("Arial", 12, "bold"), "relief": "flat"}
button_style = {"font": ("Arial", 12, "bold"), "width": 15, "height": 2, "relief": "flat"}

# Labels and Entries
tk.Label(root, text="Enter Message:", **label_style).pack(pady=5)
entry_text = tk.Entry(root, width=40, **entry_style)
entry_text.pack(pady=5)

tk.Label(root, text="Enter Shift Value:", **label_style).pack(pady=5)
entry_shift = tk.Entry(root, width=10, **entry_style)
entry_shift.pack(pady=5)

# Buttons for encryption and decryption
btn_encrypt = tk.Button(root, text="Encrypt", command=encrypt_text, bg="#00ADB5", fg="#222831", **button_style)
btn_encrypt.pack(pady=5)

btn_decrypt = tk.Button(root, text="Decrypt", command=decrypt_text, bg="#00ADB5", fg="#222831", **button_style)
btn_decrypt.pack(pady=5)

# Result Label
label_result = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#393E46", fg="#00ADB5", width=50, height=2)
label_result.pack(pady=10)

# Run GUI loop
root.mainloop()
