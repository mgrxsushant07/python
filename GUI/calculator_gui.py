from tkinter import Tk, Entry, Button, Label

def add_number():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result_label.config(text=f"Result: {num1+num2}")

root = Tk()
root.title("Dipen Calculator")
root.geometry("500x500")
label = Label(root, text="First number:")
label.pack()
entry1 = Entry(root, width=70 )
entry1.pack()

label2 = Label(root, text="Second number:")
label2.pack()
entry2 = Entry(root,width=70)
entry2.pack()

# Button
btn = Button(root, text="Add",command=add_number)
btn.pack(pady=5)

# Result Label
result_label = Label(root, text="")
result_label.pack()

root.mainloop()