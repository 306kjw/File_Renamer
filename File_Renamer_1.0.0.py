import os
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_files():
    folder_path = folder_entry.get()
    ext = ext_entry.get().strip().lower()
    digits = digit_entry.get().strip()
    prefix = prefix_entry.get()
    suffix = suffix_entry.get()
    start_str = start_entry.get().strip()

    if not digits.isdigit() or int(digits) <= 0:
        messagebox.showerror("Error", "Number of digits must be a positive integer.")
        return
    digits = int(digits)

    if not start_str.isdigit():
        messagebox.showerror("Error", "Start number must be a positive integer.")
        return
    start = int(start_str)

    if not ext.startswith("."):
        ext = "." + ext

    if not os.path.isdir(folder_path):
        messagebox.showerror("Error", "Please enter a valid folder path.")
        return

    files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(ext)])
    if not files:
        messagebox.showinfo("Info", f"No files found with extension {ext}.")
        return

    for i, old_name in enumerate(files, start=start):
        new_name = f"{prefix}{i:0{digits}d}{suffix}{ext}"
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)

    messagebox.showinfo("Done", f"Successfully renamed {len(files)} files.")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_selected)

# GUI
root = tk.Tk()
root.title("File Renamer")

tk.Label(root, text="Folder path").grid(row=0, column=0, sticky="e")
folder_entry = tk.Entry(root, width=50)
folder_entry.grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_folder).grid(row=0, column=2)

tk.Label(root, text="Extension").grid(row=1, column=0, sticky="e")
ext_entry = tk.Entry(root, width=20)
ext_entry.grid(row=1, column=1, sticky="w")
ext_entry.insert(0, "png")

tk.Label(root, text="Number of digits").grid(row=2, column=0, sticky="e")
digit_entry = tk.Entry(root, width=20)
digit_entry.grid(row=2, column=1, sticky="w")
digit_entry.insert(0, "3")

tk.Label(root, text="Start number").grid(row=3, column=0, sticky="e")
start_entry = tk.Entry(root, width=20)
start_entry.grid(row=3, column=1, sticky="w")
start_entry.insert(0, "1")

tk.Label(root, text="Prefix").grid(row=4, column=0, sticky="e")
prefix_entry = tk.Entry(root, width=20)
prefix_entry.grid(row=4, column=1, sticky="w")

tk.Label(root, text="Suffix").grid(row=5, column=0, sticky="e")
suffix_entry = tk.Entry(root, width=20)
suffix_entry.grid(row=5, column=1, sticky="w")

tk.Button(root, text="Rename Files", command=rename_files).grid(row=6, column=1, pady=10)

root.mainloop()
