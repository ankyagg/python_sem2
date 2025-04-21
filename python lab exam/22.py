'''Develop a Python GUI application that calculates the areas of different geometric figures such as
circles, rectangles, and triangles. Allows users to input the necessary dimensions for various geometric
figures and calculate their respective areas. The application should include input fields for the
dimensions, buttons to perform the calculations, and labels to display the results.'''

import tkinter as tk
import math

def calculate_areaC():
    radius = float(circle_entry.get())
    circle_output.delete('1.0',tk.END)
    area = 3.14*radius*radius
    circle_output.insert(tk.END,f"{area}")

window = tk.Tk()
window.title("Area Calculator")
window.geometry("400x400")

#circle
circle_label = tk.Label(window, text="Circle",font=("Arial",15)).pack(anchor='center')
line1 = tk.Frame(window)
line1.pack(pady=10)
line2 = tk.Frame(window)
line2.pack()

tk.Label(line1, text="Radius:").pack(side='left')
circle_entry = tk.Entry(line1,width=15)
circle_entry.pack(side='left')

tk.Label(line2, text="Area:").pack(side='left', padx=5)
circle_output = tk.Text(line2,width=15,height=1)
circle_output.pack(side='left',pady=5)
calculate_btn = tk.Button(text="Calculate",command=calculate_areaC,width=8)
calculate_btn.pack(pady=10)

#rectangle

tk.Label(window,text="Rectangle",font=("Arial",15)).pack(anchor='center',pady=10)

window.mainloop()
