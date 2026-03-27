# simple_waste_gui_min.py
import tkinter as tk
from tkinter import ttk

def classify_stub(text):
    if "banana" in text.lower() or "peel" in text.lower():
        return "wet", "Green bin", "#2ecc71"
    if "phone" in text.lower() or "charger" in text.lower():
        return "e-waste", "Gray bin", "#95a5a6"
    return "dry", "Blue bin", "#3498db"

root = tk.Tk()
root.title("Waste Bin Demo (MIN)")
root.geometry("600x320")
root.config(bg="#f0f0f0")

entry_var = tk.StringVar()
entry = ttk.Entry(root, textvariable=entry_var, font=("Arial", 14))
entry.pack(fill="x", padx=20, pady=(20,8))

def on_check():
    item = entry_var.get().strip()
    cat, bin_label, color = classify_stub(item)
    label_result.config(text=f"{item} → {cat} ({bin_label})")
    color_bar.config(bg=color)

btn = ttk.Button(root, text="Check", command=on_check)
btn.pack(pady=(0,10))

label_result = ttk.Label(root, text="Result will appear here", font=("Arial", 14))
label_result.pack(pady=(8,8))

color_bar = tk.Frame(root, height=44, bg="#ffffff", bd=1, relief="sunken")
color_bar.pack(fill="x", padx=20, pady=(6,20))

root.mainloop()
