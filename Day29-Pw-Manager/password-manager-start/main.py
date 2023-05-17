from tkinter import  *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    password=password_input_entry.get()
    email=email_username_entry.get()
    if len(website) ==0 or len(password) ==0 or len(email) == 0:
        messagebox.showerror(title="Error",message="These fields can't be empty, Please enter the field")
    else:
        isOk=messagebox.askokcancel(title=website,message=f"These are details entered {website},{password},{email}")
        if isOk:
            with open("datafile.txt",'+a') as data:
                data.writelines(f"{website}|{password}|{email}\n")
            website_entry.delete(0,END)
            password_input_entry.delete(0,END)
            email_username_entry.delete(0,END)
            email_username_entry.insert(END,"angela@gmail.com")

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.geometry("600x400")
window.config()
image_logo=PhotoImage(file="logo.png")
canvas=Canvas(width=200,height=200)
canvas.create_image(100,100,image=image_logo)

website_input=Label(text="Website:")
website_input.grid(row=1,column=0)
website_entry=Entry(width=35)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_username=Label(text="Email/Username:")
email_username.grid(row=2,column=0)
email_username_entry=Entry(width=35)
email_username_entry.grid(row=2,column=1)
email_username_entry.insert(END,"angela@gmail.com")

password_input=Label(text="Password",width="21")
password_input.grid(row=3,column=0)
password_input_entry=Entry(width=35)
password_input_entry.grid(row=3,column=1)

# add=Button(text="Add",width="36")
# add.grid(row=4,column=1)

# Button
generate_password_button=Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)
# generate_password_button_entry=Entry(width=35)
# generate_password_button_entry.grid(row=3,column=3)

add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1)
canvas.grid(row=0,column=0)


window.mainloop()