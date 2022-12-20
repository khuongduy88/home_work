from tkinter import *
from tkinter import messagebox
import json
import tkinter as tk

data_list = open('data.txt')
user_data_list = json.load(data_list)
data_list.close()
#####################################################################################

def found_user_id(new_user_name):
    index = -1
    for i in range(len(user_data_list)):
        if new_user_name.lower() == user_data_list[i]['user_name'].lower():
            index =i
            return index
            break
    return index

#####################################################################################

def new_user(add_user_name,add_user_password,add_email,add_full_name,add_user_birth_day):

    user_new ={
    'user_name':add_user_name,
    'user_password':add_user_password,
    'email':add_email,
    'full_name':add_full_name,
    'user_birth_day':add_user_birth_day
    }

    return user_new

#####################################################################################

def add_user(user_data_list):

    add_user_name = create_user_name_entry.get()
    add_user_password = create_user_password_entry.get()
    add_email = create_email_entry.get()
    add_full_name = create_full_name_entry.get()
    add_birth_day = create_birth_day_entry.get()
    
    index = found_user_id(add_user_name)
    if index ==-1:
        new_user_a = new_user(add_user_name,add_user_password,add_email,add_full_name,add_birth_day)
        user_data_list.append(new_user_a)
        
        with open('data.txt','w') as outfile:
            json.dump(user_data_list,outfile)
        messagebox.showinfo("Create an Account", "Your Account is created")
    else:
        messagebox.showerror("Create an Account", "ID is exist!")

#####################################################################################

def login():
       
    login_user_name = user_name_entry.get()
    login_user_password = password_entry.get()
    index = found_user_id(login_user_name)
    
    if index ==-1:
        messagebox.showerror("Login", "ID is not exist!")
    elif user_data_list[index]['user_password'] == login_user_password:
        messagebox.showinfo("Login", "Login Successful")
        user_info_show = tk.Toplevel()
        user_info_show.title("Your information")
        user_info_show.geometry("300x100")
        T = Text(user_info_show,height =100, width = 300)
        info ="""
user name :{}
pass word :{}
email :{}
full name :{}
birth day :{}
""".format(user_data_list[index]['user_name'],user_data_list[index]['user_password'],user_data_list[index]['email'],user_data_list[index]['full_name'],user_data_list[index]['user_birth_day'])
        T.pack()
        T.insert(tk.END,info)
            
    else:
        messagebox.showerror("Login", "Login Error!")
        
    ############################# TEST #############################################
    
#user = new_user('nguyenvanduy','nguyen','duycdt1k51@gmail.com','Nguyen Van Duy','07-10-88')
#user_data_list.append(user)

#print(user_data_list)

#####################################################################################

def create_an_account():
    global create_user_name_entry
    global create_user_password_entry
    global create_email_entry
    global create_full_name_entry
    global create_birth_day_entry
    
    create_window = Toplevel()
    create_window.title("Create an Account")
    create_window.geometry("400x400")
    create_user_name = Label(create_window,text = "Username")
    create_user_name_entry = Entry(create_window,width = 30)
    create_password = Label(create_window,text = "Password")
    create_user_password_entry = Entry(create_window,width =30,show = "*")
    create_email = Label(create_window,text = "Email")
    create_email_entry = Entry(create_window,width =30)
    create_full_name = Label(create_window,text = "Full Name")
    create_full_name_entry = Entry(create_window,width = 30)
    create_birth_day = Label(create_window,text = "Birth Day")
    create_birth_day_entry = Entry(create_window,width = 30)
    btn_create = Button(create_window, text = "Create an Account",font=("Arial", 13),width = 20)
    
    create_user_name.place(x=20,y=50)
    create_user_name_entry.place(x=100,y=50)
    create_password.place(x=20,y=100)
    create_user_password_entry.place(x=100,y=100)
    create_email.place(x=20,y=150)
    create_email_entry.place(x=100,y=150)
    create_full_name.place(x=20,y=200)
    create_full_name_entry.place(x=100,y=200)
    create_birth_day.place(x=20,y=250)
    create_birth_day_entry.place(x=100,y=250)
    btn_create.place(x=100,y=300)
    
    btn_create.bind("<Button-1>",lambda b:add_user(user_data_list))

##### GUI START ############

window = Tk()
window.title("Login")
window.geometry("450x350")
log_in = Label(window,text = "Sign",font=("Arial", 20))
create_acc = Button(window,text = "Create an Account",font=("Arial", 10),bd = 0,command = create_an_account)
user_name = Label(window,text = "Username")
user_name_entry = Entry(window,width = 30)
password = Label(window,text = "Password")
password_entry = Entry(window,width =30,show = "*")
btn_login = Button(window, text = "Login",font=("Arial", 20),width = 20,command = login)
forgot_password = Button(window,text = "Forgot password?",font=("Arial", 10),bd = 0)

log_in.place(x=100,y=10)
create_acc.place(x=250,y=18)
user_name.place(x=20,y=50)
user_name_entry.place(x=100,y=50)
password.place(x=20,y=100)
password_entry.place(x=100,y=100)
forgot_password.place(x=250,y=130)
btn_login.place(x=100,y=170)
#btn_login.bind("<Button-1>",log_in)



#with open('data.txt','w') as outfile:
#    json.dump(user_data_list,outfile)
##### GUI END ############

window.mainloop()
