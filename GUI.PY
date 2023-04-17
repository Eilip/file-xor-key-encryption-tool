import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Create a tkinter GUI window
root = tk.Tk()
root.title("XOR Zip File")
root.geometry("400x200")

# Create a label for the input file
input_file_label = tk.Label(root, text="Input Zip File:")
input_file_label.grid(row=0, column=0, padx=5, pady=5)

# Create an entry field for the input file
input_file_entry = tk.Entry(root, width=50)
input_file_entry.grid(row=0, column=1, padx=5, pady=5)

# Create a button to browse for the input file
def browse_input_file():
    input_file = filedialog.askopenfilename()
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, input_file)

browse_input_file_button = tk.Button(root, text="Browse", command=browse_input_file)
browse_input_file_button.grid(row=0, column=2, padx=5, pady=5)

# Create a label for the XOR key
key_label = tk.Label(root, text="XOR Key:")
key_label.grid(row=1, column=0, padx=5, pady=5)

# Create an entry field for the XOR key
key_entry = tk.Entry(root, width=50)
key_entry.grid(row=1, column=1, padx=5, pady=5)

# Create a label for the output file
output_file_label = tk.Label(root, text="Output Zip File:")
output_file_label.grid(row=2, column=0, padx=5, pady=5)

# Create an entry field for the output file
output_file_entry = tk.Entry(root, width=50)
output_file_entry.grid(row=2, column=1, padx=5, pady=5)

# Create a button to browse for the output file directory
def browse_output_file_dir():
    output_dir = filedialog.askdirectory()
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(0, os.path.join(output_dir, "output_" + os.path.basename(input_file_entry.get())))

browse_output_file_dir_button = tk.Button(root, text="Browse", command=browse_output_file_dir)
browse_output_file_dir_button.grid(row=2, column=2, padx=5, pady=5)

# Create a function to perform the XOR operation and save the result
def xor_zip_file():
    # Get the input file location and XOR key entered by the user
    input_file = input_file_entry.get()
    key = key_entry.get()

    # Check if the input file exists
    if not os.path.isfile(input_file):
        messagebox.showerror("Error", "Input file does not exist.")
        return

    # Open the input zip file in binary mode
    with open(input_file, 'rb') as in_file:
        # Read the contents of the file
        contents = in_file.read()

    # XOR each byte with the key and store the result in a new bytearray
    result = bytearray()
    for byte in contents:
        result.append(byte ^ ord(key))

    # Get the output file location entered by the user
    output_file = output_file_entry.get()

    # Write the result to a new file
    with open(output_file, 'wb') as out_file:
        out_file.write(result)

    # Show a message box with the location of the output file
    messagebox.showinfo("XOR Zip File", f"Output file saved at {output_file}")

# Create a button
xor_button = tk.Button(root, text="XOR", command=xor_zip_file)
xor_button.grid(row=3, column=1, padx=5, pady=20)
root.mainloop()


