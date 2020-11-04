#connecting with MySQL_database to store details.
import mysql.connector as sql
mycon=sql.connect(host="localhost",user="root",passwd="sanju123",database="Exam_Analysis")
cursor=mycon.cursor()

#for GUI
from tkinter import *
from tkinter import messagebox

#importing teacher.py and student.py files and using it inside the login_check if the login details are correct
from teacher import *
from student import *

#functiont o check whether the login details are correct/not and proceed to the next window.
def login_check(usid,pwd):
    if usid!="":
        #checking login details for teacher from teacher table
        if usid[-11:]=="teacher.com":
            query = """select user_id,pwd from teacher where USER_ID=%s"""
            cursor.execute(query,(usid,))
            res=cursor.fetchall()
            
            if res==[(usid,pwd)]:
                    homepageT()
            else:
                messagebox.showinfo("Invalid username or password.")
        
        #checking login details for student from student table.
        elif usid[-11:]=="student.com":
            query = """select user_id,pwd from studentt where USER_ID=%s"""
            cursor.execute(query,(usid,))
            res=cursor.fetchall()
            
            if res==[(usid,pwd)]:
                    homepageS(usid,pwd)
            else:
                messagebox.showinfo("Invalid username or password.")
        else:
            print(len(usid))
    else:
        messagebox.showinfo("Pls fill all the details.")

#registration form for teacher to register them in the system.
def Tregistration_form():
    #window configurations
    windowR=Tk()
    windowR.geometry("600x600")
    windowR.config(bg="light yellow")
    windowR.title("Registration form")

    #head label
    label_0=Label(windowR,text="REGISTRATION FORM",fg="black",bg="light yellow",relief="solid",font=("Copperplate Gothic",17,"bold"))
    label_0.place(x=150,y=35)
   
    #name label and entry
    label_1=Label(windowR,text="Name:",fg="black",bg="light yellow",font=("Constantia",15))
    label_1.place(x=40,y=120)
    entry_1=Entry(windowR,font=("Constantia",18))
    entry_1.place(x=140,y=120)

    #position label and entry(drop down)
    label_2=Label(windowR,text="Position:",fg="black",bg="light yellow",font=("Constantia",15))
    label_2.place(x=40,y=170)

    listP=['Senior Teacher','Junior Teacher']
    pos=StringVar()
    droplistP=OptionMenu(windowR,pos, *listP)
    pos.set('     ')
    droplistP.config(width=20,font=("Constantia",16),fg="red")
    droplistP.place(x=140,y=170)
    
    #email label and entry
    label_3=Label(windowR,text="E-mail:",fg="black",bg="light yellow",font=("Constantia",15))
    label_3.place(x=40,y=220)
    entry_3=Entry(windowR,font=("Constantia",18))
    entry_3.place(x=140,y=220)

    #ph no label and entry
    label_4=Label(windowR,text="Ph no.:",fg="black",bg="light yellow",font=("Constantia",15))
    label_4.place(x=40,y=270)
    entry_4=Entry(windowR,font=("Constantia",18))
    entry_4.place(x=140,y=270)

    #subject label and entry(drop down)
    label_5=Label(windowR,text="Subject:",fg="black",bg="light yellow",font=("Constantia",15))
    label_5.place(x=40,y=320)

    listS=['Maths','Science','English','Social Science']
    sub=StringVar()
    droplistSub=OptionMenu(windowR,sub, *listS)
    sub.set('     ')
    droplistSub.config(width=20,font=("Constantia",16),fg="red")
    droplistSub.place(x=140,y=320)

    #pwd label and entry
    label_6=Label(windowR,text="Pwd:",fg="black",bg="light yellow",font=("Constantia",15))
    label_6.place(x=40,y=370)
    entry_6=Entry(windowR,font=("Constantia",18))
    entry_6.place(x=140,y=370)
    
    #function for submit button which registers the teacher in the system using MySQL
    def reg_success():
        #to get all the entry values.
        name=entry_1.get()
        position = pos.get()
        email=entry_3.get()
        phn = entry_4.get()
        subj = sub.get()
        pawd = entry_6.get()
        cursor.execute("select max(s_no) from teacher")
        for i in cursor:
            s_no = i[0]+1
        user_id = name[0:3]+str(s_no)+"@teacher.com"

        #command for adding the data in mysql.
        query = "insert into teacher(name,position,e_mail,ph_no,subj,pwd,user_id) values (%s,%s,%s,%s,%s,%s,%s)"
        val = (name,position,email,phn,subj,pawd,user_id)
        cursor.execute(query,val)
        mycon.commit()
        
        #confirmation label
        label_7=Label(windowR,text="Registration Successfull.",fg="black",bg="light yellow",font=("Constantia",15))
        label_7.place(x=150,y=470)

        label_8=Label(windowR,text="Use "+user_id+" as user id to log in ",fg="black",bg="light yellow",font=("Constantia",15))
        label_8.place(x=150,y=470)


    #submit button for registration
    sub_button=Button(windowR,text="Submit",fg='white',bg='black',relief=RIDGE,font=("Constantia",12,"bold"),width=14,command=reg_success)
    sub_button.place(x=150,y=440)