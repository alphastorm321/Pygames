from tkinter import *

def convert():
    inches = float(entry.get())
    result.config(text=str(inches * 2.54) + " cm")

window = Tk()
window.title("Length Converter")

Label(window, text="Enter inches:").pack()
entry = Entry(window)
entry.pack()
Button(window, text="Convert", command=convert).pack()
result = Label(window, text="")
result.pack()

window.mainloop()