#connecting with MySQL_database to store details.
import mysql.connector as sql
mycon=sql.connect(host="localhost",user="root",passwd="sanju123",database="Exam_Analysis")
cursor=mycon.cursor()

#for GUI
from tkinter import *
from tkinter import messagebox

#importing login_reg.py file for its functions.
from login_reg import *

#window configuration
windowL=Tk()
windowL.geometry("500x500")
windowL.title("Sign-in")
windowL.config(bg="pale turquoise")

#head label
login_label=Label(windowL,text="LOGIN",bg="pale turquoise",fg='black',font=("Constantia",25,"bold"))
login_label.place(x=170,y=50)

#user id label and entry
usid_label=Label(windowL,text="USER ID : ",bg="pale turquoise",fg='black',font=("Constantia",12,"bold"))
usid_label.place(x=70,y=150)
usid_entry=Entry(windowL,width=20,font=(12))
usid_entry.place(x=190,y=150)

#pwd label and entry
pwd_label=Label(windowL,text="PASSWORD : ",bg="pale turquoise",fg='black',font=("Constantia",12,"bold"))
pwd_label.place(x=70,y=230)
pwd_entry=Entry(windowL,width=20, font=(12))
pwd_entry.place(x=190,y=230)

def store_login():
    usid = usid_entry.get()
    pwd = pwd_entry.get()
    login_check(usid,pwd)

#login button
login_button=Button(windowL,text="Login",fg='black',bg='pink',relief=RIDGE,font=("Constantia",12,"bold"),width=14,command=store_login)
login_button.place(x=170,y=300)

small_label=Label(windowL,text="Dont have an account? ",fg='blue',relief=RIDGE,font=("arial",7,"bold"))
small_label.place(x=320,y=430)

#registration button
reg_button=Button(windowL,text="Register",fg='black',bg='pink',relief=RIDGE,font=("Constantia",12,"bold"),width=14,command=Tregistration_form)
reg_button.place(x=320,y=450)

mainloop()
