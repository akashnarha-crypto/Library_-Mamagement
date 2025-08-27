import tkinter as tk
from tkinter import messagebox
import json
import os

FILENAME = "library_users.json"

def load_data():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)

students = load_data()

def search_student():
    code = entry_code.get()
    if code in students:
        s = students[code]
        messagebox.showinfo("Student Found",
                            f"📘 Student Details\n\n"
                            f"Code: {code}\n"
                            f"Name: {s['name']}\n"
                            f"Seat No: {s['seatno']}\n"
                            f"Fee Paid: {s['fee_paid']}")
    else:
        add = messagebox.askyesno("Not Found", "No record found. Do you want to add this student?")
        if add:
            add_student(code)

def add_student(code):
    name = entry_name.get()
    seatno = entry_seat.get()
    fee = entry_fee.get()

    if name and seatno and fee:
        students[code] = {"name": name, "seatno": seatno, "fee_paid": int(fee)}
        save_data(students)
        messagebox.showinfo("Success", "✅ Student added successfully!")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

# GUI
root = tk.Tk()
root.title("📚 Library App")

tk.Label(root, text="Library Code:").pack()
entry_code = tk.Entry(root)
entry_code.pack()

tk.Button(root, text="Search Student", command=search_student).pack(pady=5)

tk.Label(root, text="--- Add New Student ---").pack()

tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Seat No:").pack()
entry_seat = tk.Entry(root)
entry_seat.pack()

tk.Label(root, text="Fee Paid:").pack()
entry_fee = tk.Entry(root)
entry_fee.pack()

tk.Button(root, text="Add Student", command=lambda: add_student(entry_code.get())).pack(pady=10)

root.mainloop()
