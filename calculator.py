import tkinter as tk

def get_values():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        return num1, num2
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")
        return None, None

def add_numbers():
    num1, num2 = get_values()
    if num1 is not None:
        result_label.config(text=f"Result: {num1 + num2}")

def subtract_numbers():
    num1, num2 = get_values()
    if num1 is not None:
        result_label.config(text=f"Result: {num1 - num2}")

def multiply_numbers():
    num1, num2 = get_values()
    if num1 is not None:
        result_label.config(text=f"Result: {num1 * num2}")

def divide_numbers():
    num1, num2 = get_values()
    if num1 is not None:
        if num2 != 0:
            result_label.config(text=f"Result: {num1 / num2}")
        else:
            result_label.config(text="Error: Division by zero.")

def clear_field():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Result will be displayed here:")

root = tk.Tk()
root.title("Simple Calculator")

entry1 = tk.Entry(root, width=10)
entry1.grid(row=0, column=0, padx=5, pady=5)

entry2 = tk.Entry(root, width=10)
entry2.grid(row=0, column=1, padx=5, pady=5)

add_button = tk.Button(root, text="Add", command=add_numbers)
add_button.grid(row=1, column=0, padx=5, pady=5)

subtract_button = tk.Button(root, text="Subtract", command=subtract_numbers)
subtract_button.grid(row=1, column=1, padx=5, pady=5)

multiply_button = tk.Button(root, text="Multiply", command=multiply_numbers)
multiply_button.grid(row=1, column=2, padx=5, pady=5)

divide_button = tk.Button(root, text="Divide", command=divide_numbers)
divide_button.grid(row=1, column=3, padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_field)
clear_button.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

result_label = tk.Label(root, text="Result will be displayed here:")
result_label.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
