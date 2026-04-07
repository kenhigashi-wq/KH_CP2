import tkinter as tk

root = tk.Tk()

root.title("Testing")
root.configure(background="pink")

root.geometry("300x300+100+100")

start = tk.Label(root, text="New label", font=("Times New Roman", 30, "bold"))
start.config(fg="light green", background="pink")
start.pack()

#Counter
root.count = 0

def add():
    root.count += 1
    lbl['text'] = str(root.count)

def sub():
    root.count -= 1
    lbl['text'] = str(root.count)

btn = tk.Button(root, text="ADD", command=add)
btn.pack()
btn2 = tk.Button(root, text="SUB", command=sub)
btn2.pack()

lbl = tk.Label(root, text= "0")
lbl.pack()

root.minsize(250, 250)
root.maxsize(1500, 1500)


root.mainloop()