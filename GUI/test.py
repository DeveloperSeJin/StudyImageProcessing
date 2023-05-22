import tkinter as tk

def delete_button():
    button.destroy()
    print("Button deleted")

# Create the main window
window = tk.Tk()

# Create a button
button = tk.Button(window, text="Delete Button", command=delete_button)
button.pack()

# Start the main event loop
window.mainloop()
