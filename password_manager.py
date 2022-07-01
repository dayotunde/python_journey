from tkinter import *
from tkinter import messagebox
import random
from password_details import *
import pyperclip
import json

def findpassword():
    searchelement = website_input.get()
    try:
        search_file = open("data.json","r")
    except FileNotFoundError:
        messagebox.showinfo(message="No passwords Saved Dufus")
        website_input.delete(0, END)
    else:
        rawjson = json.load(search_file)
        retrieve = (rawjson[searchelement])
        for item in retrieve.items():
            keysa,valuesa = item
        messagebox.showinfo(message=f"The username is {keysa} \n the password = {valuesa}")
        pyperclip.copy(valuesa)

def add_password():
    if len(password_input.get()) == 0 or len(email_input.get()) == 0:
        messagebox.showinfo(title="Doh", message="Username and|or Password cant be empty")
        # messagebox.showerror("Username and Password cant be empty")
    else:
        is_ok = messagebox.askokcancel("New Entry confirmation", f"The details provided are \n{website_input.get()}, \nusername :{email_input.get()} password: {password_input.get()}")

        if is_ok:

            # file_1.writelines("Website \t|Website or Username\t| Password\n")
            try:
                file_1 = open("data.json", "r")
                datas = json.load(file_1)
            except FileNotFoundError:
                file_1 = open("data.json", "w")
                new_entry = {website_input.get(): {email_input.get(): password_input.get()}}
                json.dump(new_entry, file_1, indent=3)
                # print(password_input.get())
                # print(website_input.get())
                # print(email_input.get())
                # password_input.delete(0, END)
                # website_input.delete(0, END)
                # file_1.close()
            else:
                new_entry = {website_input.get():{email_input.get():password_input.get()}}
                data2 = datas.update(new_entry)
                print(datas)
                file_1.close()
                file_1 = open("data.json", "w")
                json.dump(datas,file_1,indent=3)
            finally:
                print(website_input.get())
                print(password_input.get())
                print(email_input.get())
                password_input.delete(0, END)
                website_input.delete(0, END)
                file_1.close()


def gen_password():
    new_letters_list = []
    new_number_list = []
    new_symbols_list = []
    final_password = []
    for new_letter in range(6):
        new_letters = random.choice(letters)
        new_letters_list.append(new_letters)
    for new_number in range(6):
        new_numbers = random.choice(numbers)
        new_number_list.append(new_numbers)
    for new_symbol in range(6):
        new_symbols = random.choice(symbols)
        new_symbols_list.append(new_symbols)
    for a,b,c in zip(new_letters_list,new_letters_list,new_symbols_list):
        final_password.append(a)
        final_password.append(b)
        final_password.append(c)
    random.shuffle(final_password)
    # print(final_password)
    # final_password.extend([new_symbols_list,new_number_list,new_letters_list])
    final_password = ("".join(final_password))
    pyperclip.copy(final_password)
    password_input.insert(0,final_password)




new_window = Tk()
new_window.minsize(width=200, height=200)
new_window.title("Password Manager")
new_window.config(padx=20,pady=20,bg="#edf2f4")

imagery = PhotoImage(file="logo.png")

new_canvas = Canvas(width=200,height=200)
new_canvas.create_image(100, 100, image=imagery)
new_canvas.config(bg="#edf2f4",highlightthickness=0)
new_canvas.grid(row=0,column=1)

website_label = Label(text="Website:",bg="#edf2f4")
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username:",bg="#edf2f4")
email_label.grid(row=2,column=0)

password_label = Label(text="Password:",bg="#edf2f4")
password_label.grid(row=3,column=0)

website_input = Entry(bg="white",width=21)
website_input.focus()
website_input.grid(row=1,column=1)


email_input = Entry(bg="white",width=35)
email_input.insert(0,"ay.diu@ora.com")
email_input.grid(row=2,column=1,columnspan=2)


password_input = Entry(bg="white",width=21)
password_input.grid(row=3,column=1)


password_gen = Button(text="Generate Password")
password_gen.grid(row=3, column=2)
password_gen.config(command=gen_password)

add_btn = Button(width=36,text="Add")
add_btn.grid(row=4, column=1,columnspan=2)
add_btn.config(command=add_password)


password_search = Button(text="Find Password", command=findpassword)
password_search.grid(row=1, column=2)
password_search.config(command=findpassword)



new_window.mainloop()