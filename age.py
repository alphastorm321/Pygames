import tkinter as tk
from datetime import date

def calculate_age():
    try:
        d = int(day_entry.get())
        m = int(month_entry.get())
        y = int(year_entry.get())
        today = date.today()
        age = today.year - y
        if (today.month, today.day) < (m, d):
            age -= 1
        result_label.config(text="Your age is " + str(age) + " years")
    except ValueError:
        result_label.config(text="Enter numbers only")

root = tk.Tk()
root.title("Age Calculator")

tk.Label(root, text="Day").grid(row=0, column=0)
day_entry = tk.Entry(root)
day_entry.grid(row=0, column=1)

tk.Label(root, text="Month").grid(row=1, column=0)
month_entry = tk.Entry(root)
month_entry.grid(row=1, column=1)

tk.Label(root, text="Year").grid(row=2, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=2, column=1)

tk.Button(root, text="Calculate", command=calculate_age).grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()