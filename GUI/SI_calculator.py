# Create Simple Interest Calculator Using GUI.
from tkinter import Tk, Entry, Button, Label

def simple_interest():
    principal = float(entry1.get())
    time = float(entry2.get())
    rate = float(entry3.get())
    total=(principal*time*rate)/100
    result_label.config(text=f"Result: {total}")

root = Tk()
root.title("Simple Interest Calculate")
root.geometry("500x500")

#For principal
label = Label(root, text="Enter principal:")
label.pack()
entry1 = Entry(root, width=70)
entry1.pack()

#For time
label2 = Label(root, text="Enter time:")
label2.pack()
entry2 = Entry(root, width=70)
entry2.pack()

#For Rate
label3 = Label(root, text="Enter Rate:")
label3.pack()
entry3 = Entry(root, width=70)
entry3.pack()

# Button
btn = Button(root, text="Calculate",command=simple_interest)
btn.pack(pady=5)

# Result Label
result_label = Label(root, text="")
result_label.pack()

root.mainloop()