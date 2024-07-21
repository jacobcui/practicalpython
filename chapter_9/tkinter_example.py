import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Simple Tkinter App")

# Create a label widget
label = tk.Label(root, text="Enter your name:")
label.pack()  # Add the label to the window

# Create an entry widget
entry = tk.Entry(root)
entry.pack()  # Add the entry field to the window


# Function to handle button click event
def on_button_click():
    name = entry.get()  # Get the text from the entry field
    label.config(text=f"Hello, {name}!")


# Create a button widget
button = tk.Button(root, text="Greet", command=on_button_click)
button.pack()  # Add the button to the window

# Start the Tkinter event loop
root.mainloop()
