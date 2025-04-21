import tkinter as tk
from tkinter import messagebox

def display_data():
    name = name_entry.get()
    age = age_entry.get()
    branch = branch_entry.get()
    games = games_entry.get()
    
    output_text.delete('1.0', tk.END)
    
    output_text.insert(tk.END, f"Name: {name}\n")
    output_text.insert(tk.END, f"Age: {age}\n")
    output_text.insert(tk.END, f"Branch: {branch}\n")
    output_text.insert(tk.END, f"Favourite Games: {games}")

# Create main window
root = tk.Tk()
root.title("Student Form")
root.geometry("400x400")

# Labels and Entry fields
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root, width=30)
age_entry.pack()

tk.Label(root, text="Branch").pack()
branch_entry = tk.Entry(root, width=30)
branch_entry.pack()

tk.Label(root, text="Favourite Games").pack()
games_entry = tk.Entry(root, width=30)
games_entry.pack()

# Submit button
submit_btn = tk.Button(root, text="Submit", command=display_data)
submit_btn.pack(pady=10)

# Output Text Box
output_text = tk.Text(root, height=8, width=45)
output_text.pack(pady=10)

# Start the GUI event loop
root.mainloop()
