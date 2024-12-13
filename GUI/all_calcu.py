from tkinter import Tk, Entry, Button, Label

def multiply():
    num1=float(entry1.get())
    num2=float(entry2.get())
    total=num1*num2
    result_label.config(text=f"Result: {total}")

root = Tk()
root.title=("Multiply")
root.geometry("500x500")
label1 = Label(root,text="First number :")
label1.pack()
entry1 = Entry(root, width=70 )
entry1.pack()

label2=Label(root,text="Second number :")
label2.pack()
entry2 = Entry(root, width=70)
entry2.pack()

#button
btn=Button(root,text="Multiply",command=multiply)
btn.pack(pady=10)

#result label
result_label = Label(root, text="")
result_label.pack()

root.mainloop()