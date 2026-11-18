import tkinter as tk

window = tk.Tk()
window.title("Product Calculator")
window.geometry("300x250")

label1 = tk.Label(window, text="Enter first number:")
label1.pack(pady=5)
entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Enter second number:")
label2.pack(pady=5)
entry2 = tk.Entry(window)
entry2.pack()

result_label = tk.Label(window, text="Product: ")


def multiply():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result_label.config(text="Product: " + str(a * b))
    except ValueError:
        result_label.config(text="Please enter numbers only")


button = tk.Button(window, text="Multiply", command=multiply)
button.pack(pady=10)
result_label.pack()

window.mainloop()