from tkinter import Tk, Entry, Button ,Label 

def addition_subtraction():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    addition=num1+num2
    subtraction=num1-num2
    result_label.config(text=f"Addition = {addition}  Substract = {subtraction}")


root=Tk()
root.title("addition_subtraction")
root.geometry("500x500")

label1=Label(root,text="First number")
label1.pack()
entry1=Entry(root,width=70)
entry1.pack()

label2=Label(root,text="Second number")
label2.pack()
entry2=Entry(root,width=70)
entry2.pack()

#for button
btn=Button(root,text="Calculate",command=addition_subtraction)
btn.pack(pady=5)

#result label
result_label=Label(root,text="")
result_label.pack()


#To end the process
root.mainloop()