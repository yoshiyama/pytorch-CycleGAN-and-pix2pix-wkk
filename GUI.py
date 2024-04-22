import tkinter as tk
from tkinter import Entry, Label, Button
import subprocess

def execute_script():
    # Get the values from the text boxes
    dataroot = dataroot_entry.get()
    name = name_entry.get()
    # ... (repeat for other parameters)

    # Build the command string
    command = f'python train_mask.py --dataroot {dataroot} --name {name} '  # ... (add other parameters)
    # Execute the command
    subprocess.run(command, shell=True)

# Create the main window
window = tk.Tk()
window.title("Train Mask GUI")

# Create labels and text boxes for each parameter
dataroot_label = Label(window, text="Dataroot:")
dataroot_label.grid(row=0, column=0)
dataroot_entry = Entry(window)
dataroot_entry.grid(row=0, column=1)

name_label = Label(window, text="Name:")
name_label.grid(row=1, column=0)
name_entry = Entry(window)
name_entry.grid(row=1, column=1)

# ... (repeat for other parameters)

# Create the execute button
execute_button = Button(window, text="Execute Script", command=execute_script)
execute_button.grid(row=2, columnspan=2)  # Adjust row value based on the number of parameters

# Run the GUI event loop
window.mainloop()
