from tkinter import ttk
import tkinter as tk

def calculate():
    # Get the numbers and operator from the entry widgets
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    operator = operator_var.get()

    # Perform the calculation
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        result = "Invalid operator"

    # Display the result
    result_label.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Calculator")

# Apply a ttk theme


# Create the entry widgets for the numbers
num1_entry = ttk.Entry(root)
num1_entry.grid(row=0, column=1)
num2_entry = ttk.Entry(root)
num2_entry.grid(row=1, column=1)

# Create the operator radio buttons
operator_var = tk.StringVar(value="+")
addition_button = ttk.Radiobutton(root, text="+", variable=operator_var, value="+")
addition_button.grid(row=2, column=0)
subtraction_button = ttk.Radiobutton(root, text="-", variable=operator_var, value="-")
subtraction_button.grid(row=2, column=1)
multiplication_button = ttk.Radiobutton(root, text="*", variable=operator_var, value="*")
multiplication_button.grid(row=2, column=2)
division_button = ttk.Radiobutton(root, text="/", variable=operator_var, value="/")
division_button.grid(row=2, column=3)

# Create the calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=1)

# Create the result label
result_label = ttk.Label(root, text="Result:")
result_label.grid(row=4, column=1)

root.mainloop()
