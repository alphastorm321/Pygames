# Import neccesary libraries
from tkinter import *
from tkinter import messagebox

#Setup Tkinter Window
root=Tk()
root.geometry("200x200")

# Function for displaying Warning message
# This will be called once the button is clicked
# messagebox.showwarning("Window name", "Text to be displayed")
def msg():
    messagebox.showwarning("Alert! ", "Stop! Virus detected")

# Adding Button Widget to Window
button=Button(root,text="Scan for virus", command=msg)
button.place(x=40,y=80)

# Entering main event loop
root.mainloop()