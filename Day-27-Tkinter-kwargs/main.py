import tkinter

window=tkinter.Tk()

window.title("Convert kg into pound")
# window.minsize(width=500,height=300)
window.geometry("400x400")
# Label
my_label = tkinter.Label(text="New Text", font=("Arial", 24, "bold"))
my_label.pack(expand="True")
# Button
def button_clicked():
    print("I got clicked!")
    my_label.config(text=input.get())

button=tkinter.Button(text="Click Me",command=button_clicked)

button.pack(expand="True")
# Entry
input=tkinter.Entry(width=20)
print(input.get())

input.pack(expand="True")
window.mainloop()