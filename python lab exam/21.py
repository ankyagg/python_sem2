import tkinter as tk

def money_converter():
    rupee = float(rupee_entry.get())
    output_text.delete(1.0,tk.END)
    dollar = float(0.011711*rupee)
    output_text.insert(tk.END,f"{dollar}")

def degree_converter():
    degree = float(degree_entry.get())
    output_degree.delete(1.0,tk.END)
    farenhiet = float((degree * 9/5) + 32)
    output_degree.insert(tk.END,f"{farenhiet}")

def length_converter():
    inches = float(inches_entry.get())
    output_feet.delete('1.0',tk.END)
    feet = inches / 12 
    output_feet.insert(tk.END,f"{feet}")
    
window = tk.Tk()
window.title("Unit Converter")
window.geometry("600x600")

#Money conversions
tk.Label(text="MONEY CONVERTER",font=20).pack(pady=10)
tk.Label(text="₹",width=10,font=12).pack()
rupee_entry = tk.Entry(window, width=18)
rupee_entry.pack()

tk.Label(text="$",width=15,font=12).pack()
output_text = tk.Text(window,width=13,height=1)
output_text.pack()
convert_btn = tk.Button(text="Convert",width=7,height=1,command=money_converter).pack(pady=10)


#degree conversion
tk.Label(text="TEMPERATURE CONVERTER",font=20).pack(pady=20)
tk.Label(text="Celsius",width = 10).pack()
degree_entry = tk.Entry(window,width=8)
degree_entry.pack(pady=10,)

tk.Label(text="Farenhiet",width = 10).pack()
output_degree=tk.Text(window,width=8,height=1)
output_degree.pack()
convert_btn = tk.Button(text="Convert",width=7,height=1,command=degree_converter).pack(pady=10)


#Lenght converter
tk.Label(text="LENGTH CONVERTER",font=20).pack(pady=10)
tk.Label(text="Inches",width=10,font=12).pack()
inches_entry = tk.Entry(window, width=18)
inches_entry.pack()

tk.Label(text="Feet",width=10,font=12).pack()
output_feet = tk.Text(window,width=18,height=1)
output_feet.pack()
convert_btn = tk.Button(text="Convert",width=7,height=1,command=length_converter).pack(pady=10)

window.mainloop()

