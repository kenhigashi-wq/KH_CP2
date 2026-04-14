#KH portfolio
#Import everthing needed
import tkinter as tk
import subprocess
import sys
import os
from tkinter import messagebox


#Make dataset and stuff for descriptiom
projects = {
    "Simple Morse Code": {
        "info": (
            "This program converts text into Morse code for encoding messages.\n\n"
            "What I learned:\n"
            "- Using dictionaries for character mapping\n"
            "- Processing strings character by character\n\n"
            "Challenge:\n"
            "- Handling unsupported or invalid characters"
            "- Also making the morse code stuff"
        ),
        "path": "individual_projects/simple_morse_code.py"
    },
    "Geometry Calculator": {
        "info": (
            "Calculates geometric values like area and perimeter.\n\n"
            "What I learned:\n"
            "- Classes\n"
            "- Mathematical formulas\n\n"
            "Challenge:\n"
            "- Searching up formulas for everysingle one of them because I don't remember tham"
        ),
        "path": "individual_projects/geometry_calc/main.py"
    },
    "Grade Book": {
        "info": (
            "Stores grades and calculates averages.\n\n"
            "What I learned:\n"
            "- Lists and averages\n"
            "- Organizing data\n\n"
            "Challenge:\n"
            "- Typing everything out correctly"
        ),
        "path": "individual_projects/grade_book/main.py"
    },
    "Financial Calculator": {
        "info": (
            "Performs basic financial calculations.\n\n"
            "What I learned:\n"
            "- Functions\n"
            "- Numerical input handling\n\n"
            "Challenge:\n"
            "- Maintaining calculation accuracy"
        ),
        "path": "individual_projects/financial_calculator.py"
    }
}

#make a function for showing info
def show_info(name):
    root.current_project = name
    info_text.delete("1.0", tk.END)
    info_text.insert(tk.END, projects[name]["info"])
    run_btn.config(state="normal")

#Making a function for running the project
def run_project():
    path = projects[root.current_project]["path"]

    if not os.path.exists(path):
        messagebox.showerror(
            "File Not Found",
            "Project file not found.\nMake sure the project is in the correct folder"
        )
        return

    subprocess.Popen([sys.executable, path])

#init root 
root = tk.Tk()
root.title("Kensei Higashi - Python Portfolio")
root.geometry("900x500")
root.current_project = None

#make ui and stuff enow
tk.Label(
    root,
    text=(
        "Python Programming Portfolio\n"
        "Click a project to view details, then run it."
    ),
    pady=10
).pack()

main = tk.Frame(root)
main.pack(fill="both", expand=True)

left = tk.Frame(main)
left.pack(side="left", padx=10)

tk.Label(left, text="Projects").pack()

for name in projects:
    tk.Button(
        left,
        text=name,
        width=28,
        command=lambda n=name: show_info(n)
    ).pack(pady=4)

right = tk.Frame(main)
right.pack(side="right", fill="both", expand=True, padx=10)

info_text = tk.Text(right, wrap="word")
info_text.pack(fill="both", expand=True)

run_btn = tk.Button(
    right,
    text="Run Project",
    state="disabled",
    command=run_project
)
run_btn.pack(pady=10)

#run
root.mainloop()