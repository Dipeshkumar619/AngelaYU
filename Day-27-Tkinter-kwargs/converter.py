from tkinter import *
window=Tk()
# window.geometry("300x200")
window.title("Miles to KM Converter")
window.config(padx=20,pady=20)

def miles_convert():
    miles=float(miles_input.get())
    km=miles*1.60934
    kilometer_result_label.config(text=f"{km}")

miles_input=Entry()
miles_input.grid(column=1,row=0)

miles_label=Label(text="Miles")
miles_label.grid(column=1,row=0)

is_equal=Label(text="is Equals to")
is_equal.grid(column=2,row=0)

kilometer_result_label=Label(text="0")
kilometer_result_label.grid(column=0,row=1)

kilometer_label=Label(text="Km")
kilometer_label.grid(column=1,row=1)

calculate_button=Button(text="Calculate",command=miles_convert)
calculate_button.grid(column=1,row=2)
window.mainloop()
