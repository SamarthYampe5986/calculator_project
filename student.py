import tkinter as tk
from tkinter import messagebox
import sqlite3

# database connect
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
name TEXT,
roll TEXT,
marks TEXT
)
""")

def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    marks = marks_entry.get()

    if name == "" or roll == "" or marks == "":
        messagebox.showwarning("Error","Fill all fields")
        return

    cursor.execute("INSERT INTO students VALUES(?,?,?)",(name,roll,marks))
    conn.commit()

    listbox.insert(tk.END,f"{name} | {roll} | {marks}")

    name_entry.delete(0,tk.END)
    roll_entry.delete(0,tk.END)
    marks_entry.delete(0,tk.END)

def view_students():
    listbox.delete(0,tk.END)

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    for row in rows:
        listbox.insert(tk.END,row)

window = tk.Tk()
window.title("Student Management System")
window.geometry("400x400")

tk.Label(window,text="Name").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window,text="Roll No").pack()
roll_entry = tk.Entry(window)
roll_entry.pack()

tk.Label(window,text="Marks").pack()
marks_entry = tk.Entry(window)
marks_entry.pack()

tk.Button(window,text="Add Student",command=add_student).pack(pady=5)
tk.Button(window,text="View Students",command=view_students).pack(pady=5)

listbox = tk.Listbox(window,width=50)
listbox.pack(pady=10)

window.mainloop()