import tkinter as tk
from tkinter import messagebox

def calculate_toll():
    try:
        # Get data from the entry boxes
        name = entry_name.get().strip().lower()
        a = float(entry_distance.get())
        b = float(entry_time.get())

        members = ["adam", "ula", "derek", "scott", "austin", "malia", "mellisa", "walter", "hanna"]
        
        dis = 5 * a
        total_t = 100 * b
        tax = dis + total_t
        
        is_member = name in members
        
        # Logic for calculation
        if is_member and dis > total_t:
            final = tax - total_t
            result_text = f"Member Found!\nYour toll is: {final}"
        elif is_member and total_t > dis:
            final = tax - dis
            result_text = f"Member Found!\nYour toll is: {final}"
        elif is_member:
            result_text = f"Member Found!\nYour toll is: {tax}"
        else:
            result_text = f"Not a Member.\nYour toll is: {tax}"

        # Update the label with the result
        label_result.config(text=result_text, fg="blue")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for distance and time.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Toll Calculator")
root.geometry("350x400")

# Name Input
tk.Label(root, text="Enter Name:", font=("Arial", 10, "bold")).pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack()

# Distance Input
tk.Label(root, text="Distance Traveled (in km):", font=("Arial", 10, "bold")).pack(pady=5)
entry_distance = tk.Entry(root)
entry_distance.pack()

# Time Input
tk.Label(root, text="Time of Possession (in mins):", font=("Arial", 10, "bold")).pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack()

# Calculate Button
btn_calc = tk.Button(root, text="Calculate Toll", command=calculate_toll, bg="green", fg="white")
btn_calc.pack(pady=20)

# Result Label
label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=10)

root.mainloop()
