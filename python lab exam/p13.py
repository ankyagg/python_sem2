import tkinter as tk
from tkinter import messagebox

def display_text():
    name = name_entry.get()
    age = age_entry.get()
    dept = Dept_entry.get()
    game = game_entry.get()

    output_box.delete('1.0', tk.END)

    output_box.insert(tk.END, f"Name: {name}\n")
    output_box.insert(tk.END, f"Age: {age}\n")
    output_box.insert(tk.END, f"Branch: {dept}\n")
    output_box.insert(tk.END, f"Favourite Games: {game}")
    
window = tk.Tk()
window.title("Student Form")
window.geometry("400x400")

name_label = tk.Label(window, text="Name")
name_label.pack()
name_entry = tk.Entry(window, width=30)
name_entry.pack()

age_label = tk.Label(window,text="Age")
age_label.pack()
age_entry = tk.Entry(window, width=30)
age_entry.pack()

Dept_label = tk.Label(window,text="Department")
Dept_label.pack()
Dept_entry = tk.Entry(window, width=30)
Dept_entry.pack()

game_label = tk.Label(window,text="Game")
game_label.pack()
game_entry = tk.Entry(window, width=30)
game_entry.pack()

submit_btn = tk.Button(window, text="Submit",command=display_text)
submit_btn.pack(pady=10)

output_box= tk.Text(window,height=9,width=45)
output_box.pack(pady=10)

window.mainloop()
