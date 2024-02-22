import tkinter as tk

# Conversion functions
def cm_to_feet():
    try:
        cm = float(cm_entry.get())
        feet = cm * 0.0328084
        result_label.config(text=f"{cm} cm = {feet:.2f} feet")
    except ValueError:
        result_label.config(text="Invalid input")

def feet_to_inches():
    try:
        feet = float(feet_entry.get())
        inches = feet * 12
        result_label.config(text=f"{feet} feet = {inches:.2f} inches")
    except ValueError:
        result_label.config(text="Invalid input")

def sqft_to_sqm():
    try:
        sqft = float(sqft_entry.get())
        sqm = sqft * 0.092903
        result_label.config(text=f"{sqft} sqft = {sqm:.2f} sqm")
    except ValueError:
        result_label.config(text="Invalid input")

def sqft_to_hectare_acres():
    try:
        sqft = float(sqft_entry.get())
        hectare = sqft * 0.0000092903
        acre = sqft * 0.00002295684
        result_label.config(text=f"{sqft} sqft = {hectare:.6f} hectare\n{sqft} sqft = {acre:.6f} acres")
    except ValueError:
        result_label.config(text="Invalid input")

# GUI setup
root = tk.Tk()
root.title("Unit Converter")

# Centimeter to Feet
cm_label = tk.Label(root, text="Centimeter:")
cm_label.grid(row=0, column=0)
cm_entry = tk.Entry(root)
cm_entry.grid(row=0, column=1)
cm_to_feet_button = tk.Button(root, text="Convert to Feet", command=cm_to_feet)
cm_to_feet_button.grid(row=0, column=2)

# Feet to Inches
feet_label = tk.Label(root, text="Feet:")
feet_label.grid(row=1, column=0)
feet_entry = tk.Entry(root)
feet_entry.grid(row=1, column=1)
feet_to_inches_button = tk.Button(root, text="Convert to Inches", command=feet_to_inches)
feet_to_inches_button.grid(row=1, column=2)

# Sqft to Sqm
sqft_label = tk.Label(root, text="Square Feet:")
sqft_label.grid(row=2, column=0)
sqft_entry = tk.Entry(root)
sqft_entry.grid(row=2, column=1)
sqft_to_sqm_button = tk.Button(root, text="Convert to Sqm", command=sqft_to_sqm)
sqft_to_sqm_button.grid(row=2, column=2)

# Sqft to Hectare / Acres
sqft_to_hectare_acres_button = tk.Button(root, text="Convert to Hectare / Acres", command=sqft_to_hectare_acres)
sqft_to_hectare_acres_button.grid(row=3, column=1)

# Result display
result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=3)

root.mainloop()