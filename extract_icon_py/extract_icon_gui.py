import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import tempfile
from PIL import Image

def extract_icon_using_wrestool(exe_path, output_png):
    # Create a temporary directory to hold extracted icon files.
    with tempfile.TemporaryDirectory() as tmpdir:
        # Run wrestool to extract icon resources (type 14).
        command = ["wrestool", "-x", "-t", "14", exe_path, "-o", tmpdir]
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Extraction Error", f"Error extracting icon with wrestool:\n{e}")
            return False

        # Find ICO files in the temporary directory.
        ico_files = [os.path.join(tmpdir, f) for f in os.listdir(tmpdir) if f.endswith('.ico')]
        if not ico_files:
            messagebox.showerror("Extraction Error", "No ICO files were extracted. The executable may not contain icon resources.")
            return False

        # Use the first extracted ICO file.
        ico_path = ico_files[0]
        try:
            with Image.open(ico_path) as img:
                # Save the image as PNG.
                img.save(output_png)
            return True
        except Exception as e:
            messagebox.showerror("Processing Error", f"Error processing the ICO file:\n{e}")
            return False

def select_input():
    filename = filedialog.askopenfilename(title="Select EXE File", filetypes=[("Executable files", "*.exe")])
    if filename:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, filename)

def select_output():
    filename = filedialog.asksaveasfilename(title="Select Output File", defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if filename:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, filename)

def run_extraction():
    exe_path = input_entry.get()
    output_path = output_entry.get()
    if not exe_path:
        messagebox.showerror("Input Error", "Please select an input EXE file.")
        return
    if not output_path:
        messagebox.showerror("Input Error", "Please select an output file path.")
        return
    if extract_icon_using_wrestool(exe_path, output_path):
        messagebox.showinfo("Success", f"Icon saved as:\n{output_path}")

# Build the GUI
root = tk.Tk()
root.title("EXE Icon Extractor")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Input file section
tk.Label(frame, text="Input EXE File:").grid(row=0, column=0, sticky="e")
input_entry = tk.Entry(frame, width=50)
input_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame, text="Browse...", command=select_input).grid(row=0, column=2, padx=5)

# Output file section
tk.Label(frame, text="Output PNG File:").grid(row=1, column=0, sticky="e")
output_entry = tk.Entry(frame, width=50)
output_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame, text="Browse...", command=select_output).grid(row=1, column=2, padx=5)

# Extract button
tk.Button(frame, text="Extract Icon", command=run_extraction).grid(row=2, column=1, pady=10)

root.mainloop()
