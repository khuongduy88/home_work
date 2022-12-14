from tkinter import *
from tkinter import messagebox

class User:
    
    def __init__(self,user_name,user_password,email,full_name,user_birth_day):
        
        self.user_name = user_name
        self.user_password = user_password
        self.email = email
        self.full_name = full_name
        self.user_birth_day = user_birth_day

class User_data:
    
    def __init__(self):

        self.user_data_list = []

    def found_user_id(self,new_user_name):

        index = -1
        for i in range(len(self.user_data_list)):
            if new_user_name == self.user_data_list[i].user_name.lower():
                index =i
                #break
        return index

    def add_user(self,add_user_name,add_user_password,add_email,add_full_name,add_user_birth_day):
        
        # add_user_name = create_user_name_entry.get()        
        # add_user_password = create_user_password_entry.get()       
        # add_email = create_email_entry.get()        
        # add_full_name = create_full_name_entry.get()        
        # add_user_birth_day = create_user_birth_day_entry.get()        
        new_user= User(add_user_name,add_user_password,add_email,add_full_name,add_user_birth_day)        
        index = self.found_user_id(new_user)        
        if index ==-1:
            self.user_data_list.append(new_user)
        
        else:
            pass


#### TEST #####

user_data_list = User_data()
user_name = "nguyenvanduy"
user_password = "nguyen"
email = "duycdt1k51@gmail.com"
full_name = "Nguyen Van Duy"
user_birth_day = "07-10-88"
user_data_list.add_user(user_name,user_password,email,full_name,user_birth_day)

#### TEST END #####

#funciton add new user name

def add_new_account(user_data_list):

    add_user_name = create_user_name_entry.get()
    add_user_password = create_user_password_entry.get()
    add_email = create_email_entry.get()
    add_full_name = create_full_name_entry.get()
    add_user_birth_day = create_user_birth_day_entry.get()
    user_data_list.add_user(add_user_name,add_user_password,add_email,add_full_name,add_user_birth_day)

# for item in user_data_list:

# print(item.user_name)
def log_in():
    

    login_user_name = user_name_entry.get()
    
    login_user_password = password_entry.get()
    print(user_data_list.user_data_list)
    for item in user_data_list.user_data_list:
         if item.user_name == login_user_name and item.password == login_user_password:
                
                #print("OK")
                messagebox.showinfo("Login","Login OK")
                
         
         else:
                print("NG")
    
    #tkMessageBox.showinfo("Login","Login NG")
    



def create_an_account():

    create_window = Tk()
    create_window.title("Create an Account")
    create_window.geometry("400x600")
    #create_account = Label(create_window,text = "Create an Account",font=("Arial", 15))
    create_user_name = Label(create_window,text = "Username")
    create_user_name_entry = Entry(create_window,width = 30)
    create_password = Label(create_window,text = "Password")
    create_password_entry = Entry(create_window,width =30,show = "*")
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
    create_password_entry.place(x=100,y=100)
    create_email.place(x=20,y=150)
    create_email_entry.place(x=100,y=150)
    create_full_name.place(x=20,y=200)
    create_full_name_entry.place(x=100,y=200)
    create_birth_day.place(x=20,y=250)
    create_birth_day_entry.place(x=100,y=250)
    btn_create.place(x=100,y=300)
    btn_create.bind("<Button-1>",add_new_account)

##### GUI START ############

window = Tk()
window.title("Login")
window.geometry("400x350")
log_in = Label(window,text = "Sign",font=("Arial", 15))
create_acc = Button(window,text = "Create an Account",font=("Arial", 10),bd = 0,command = create_an_account)
user_name = Label(window,text = "Username")
user_name_entry = Entry(window,width = 30)
password = Label(window,text = "Password")
password_entry = Entry(window,width =30,show = "*")
btn_login = Button(window, text = "Login",font=("Arial", 13),width = 20,command = log_in)
forgot_password = Button(window,text = "Forgot password?",font=("Arial", 10),bd = 0)
#user_name.grid(row = 2, column = 0)
#user_name_entry.grid(row = 2, column = 2)
#password.grid(row = 4, column = 0)
#password_entry.grid(row = 4, column = 2)

log_in.place(x=100,y=10)
create_acc.place(x=200,y=15)
user_name.place(x=20,y=50)
user_name_entry.place(x=100,y=50)
password.place(x=20,y=100)
password_entry.place(x=100,y=100)
forgot_password.place(x=250,y=130)
btn_login.place(x=100,y=170)
#btn_login.bind("<Button-1>",log_in)

##### GUI END ############

#print(user_data_list.user_data_list)

window.mainloop()