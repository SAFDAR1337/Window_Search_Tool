import os
import subprocess
import tkinter as tk
from tkinter import messagebox

def open_location(event=None):  # Added event parameter for Enter key binding
    path = entry.get().strip()  # Get input and remove spaces
    
    if os.path.exists(path):  # Check if path exists
        if os.path.isdir(path):  # If it's a folder, open it directly
            subprocess.run(['explorer', path], shell=True)
        else:  # If it's a file, open its parent folder
            folder_path = os.path.dirname(path)
            subprocess.run(['explorer', folder_path], shell=True)
    else:
        messagebox.showerror("Error", "Invalid file or folder path!")

# GUI Setup
root = tk.Tk()
root.title("Windows Search App")
root.geometry("400x200")

tk.Label(root, text="Enter File or Folder Path:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)
entry.bind("<Return>", open_location)  # Bind Enter key to function

btn_open = tk.Button(root, text="Open Location", command=open_location)
btn_open.pack(pady=10)

root.mainloop()
