#for GUI
from tkinter import *
from tkinter import messagebox

#connecting with MySQL_database to store details.
import mysql.connector as sql
mycon=sql.connect(host="localhost",user="root",passwd="sanju123",database="Exam_Analysis")
cursor=mycon.cursor()

#importing entermarks.py file to add all the marks to the database.
from entermarks import *

#showing graphs for analysing their performance
import matplotlib.pyplot as plt

#student reg form(handled by teachers)
def Sregistration_form():

    #window config.
    windowR=Tk()
    windowR.geometry("550x500")
    windowR.config(bg="light yellow")
    windowR.title("Registration form")

    #head label
    label_0=Label(windowR,text="REGISTRATION FORM",fg="black",bg="light yellow",relief="solid",font=("Copperplate Gothic",17,"bold"))
    label_0.place(x=120,y=35)
   
    #adm label
    label_1=Label(windowR,text="Adm No:",fg="black",bg="light yellow",font=("Constantia",15))
    label_1.place(x=40,y=120)
    entry_1=Entry(windowR,font=("Constantia",18))
    entry_1.place(x=140,y=120)

    #name label
    label_2=Label(windowR,text="Name:",fg="black",bg="light yellow",font=("Constantia",15))
    label_2.place(x=40,y=170)
    entry_2=Entry(windowR,font=("Constantia",18))
    entry_2.place(x=140,y=170)

    #class ans sec label
    label_3=Label(windowR,text="Class&Sec:",fg="black",bg="light yellow",font=("Constantia",15))
    label_3.place(x=40,y=220)
    entry_3=Entry(windowR,font=("Constantia",18))
    entry_3.place(x=140,y=220)

    #ph no label
    label_4=Label(windowR,text="Ph no:",fg="black",bg="light yellow",font=("Constantia",15))
    label_4.place(x=40,y=270)
    entry_4=Entry(windowR,font=("Constantia",18))
    entry_4.place(x=140,y=270)

    #e mail label
    label_5=Label(windowR,text="E mail:",fg="black",bg="light yellow",font=("Constantia",15))
    label_5.place(x=40,y=320)
    entry_5=Entry(windowR,font=("Constantia",18))
    entry_5.place(x=140,y=320)

    #submit command
    def reg_submit():
        adm=entry_1.get()
        name = entry_2.get()
        cs=entry_3.get()
        phn = entry_4.get()
        email = entry_5.get()
        pwd="123"
        user_id = name[0:3]+adm+"@student.com"

        query = "insert into studentt(name,adm_no,class_sec,ph_no,e_mail,user_id,pwd) values (%s,%s,%s,%s,%s,%s,%s)"
        val = (name,adm,cs,phn,email,user_id,pwd)
        cursor.execute(query,val)
        mycon.commit()
        
        label_6=Label(windowR,text="Success!",fg="black",bg="light yellow",font=("Constantia",15))
        label_6.place(x=220,y=400)

        label_7=Label(windowR,text="Use "+user_id+" and "+pwd+" to log in ",fg="black",bg="light yellow",font=("Constantia",15))
        label_7.place(x=100,y=450)

    #registration submit button
    sub_find=Button(windowR,text="SUBMIT",fg='white',bg='black',relief=RIDGE,font=("Constantia",13),width=10,command=reg_submit)
    sub_find.place(x=120,y=400)

#find studs command
def findAll_studs(a):
    query = "select name,adm_no from studentt where class_sec=%s"
    cursor.execute(query,(a,))
    detLi=[]
    for i in cursor:
        li=list(i)
        DET="Name : "+str(li[0])+"  Adm. no. "+str(li[1])
        detLi.append(DET)

    #new window to diplay the student list.
    windowList = Tk()
    windowList.geometry("400x300")
    windowList.title("Exam Analysis")
    windowList.configure(bg="pink")
    
    eve_list=Listbox(windowList,height=8,width=20, font=("Verdana",17))
    for i in range(len(detLi)):
        eve_list.insert(i,detLi[i])
        eve_list.place(x=20,y=10)

def checkreport(a):
    query = "select math_q,sci_q,eng_q,soc_q,math_h,sci_h,eng_h,soc_h,math_a,sci_a,eng_a,soc_a from studentt where adm_no=%s"
    val = (a,)
    mark_list=[]
    cursor.execute(query,val)
    for i in cursor:
        for j in i:
            mark_list.append(j)
    exams = ['Quarterly avg', 'Half yearly avg', 'Annual avg']
    #finding average
    if mark_list!=[]:
        q = (mark_list[0]+mark_list[1]+mark_list[2]+mark_list[3])/4
        h = (mark_list[4]+mark_list[5]+mark_list[6]+mark_list[7])/4
        a = (mark_list[8]+mark_list[9]+mark_list[10]+mark_list[11])/4
        values = [q, h, a]

        plt.figure(figsize=(5, 5))
        plt.ylabel('Marks')
        plt.xlabel('Examinations')
        plt.plot(exams, values)
        plt.suptitle('Exam Performance Analysis')
        plt.show()
    else:
        messagebox.showinfo("Student does not exist.")

def homepageT():
    
    windowT=Tk()
    windowT.geometry("1000x700")
    windowT.title("Exam Analysis")
    windowT.configure(bg="pink")

    #school logo
    logo=PhotoImage(master=windowT,file="SV-logo.png")
    label_p1=Label(windowT, image=logo)
    label_p1.place(x=20,y=10)

    #school name title
    schname_label=Label(windowT,text="SARASWATHI VIDYALAYA",bg="pink",fg="black",font=("Constantia",27,"bold"))
    schname_label.place(x=250,y=20)

    #heading
    head_label=Label(windowT,text="Examination Marks & Performance Analysis",bg="pink",fg="brown",font=("Constantia",22,"bold"))
    head_label.place(x=210,y=90)

    #student_reg button
    button_studR=Button(windowT,text="Reg. Student",fg='white',bg='light blue',relief=RIDGE,font=("Constantia",17,"bold"),width=10,command=Sregistration_form)
    button_studR.place(x=40,y=200)

    #find students using class
    find_label=Label(windowT,text="Find stud's adm. no:",bg="pink",fg="black",font=("Constantia",13))
    find_label.place(x=620,y=160)
    
    listC=['9A','10A','11A','12A','9B','10B','11B','12B']
    clas=StringVar()
    droplistC=OptionMenu(windowT,clas, *listC)
    clas.set('     ')
    droplistC.config(width=10,font=("Constantia",16),fg="red")
    droplistC.place(x=640,y=190)
    
    def send_find():
        classs=clas.get()
        findAll_studs(classs)

    #find studs using class button
    button_find=Button(windowT,text="Find",fg='white',bg='black',relief=RIDGE,font=("Constantia",13),width=10,command=send_find)
    button_find.place(x=820,y=190)

    #check report label
    report_label=Label(windowT,text="Check Report:",bg="pink",fg="red",font=("Constantia",20,"bold"))
    report_label.place(x=210,y=270)

    #student's adm no. label
    studA_label=Label(windowT,text="Stud's Adm. No:",bg="pink",fg="black",font=("Constantia",18,"bold"))
    studA_label.place(x=240,y=350)
    adm_entry=Entry(windowT,width=15, font=(12))
    adm_entry.place(x=500,y=350)

    def submit():
        adm_no = adm_entry.get()
        checkreport(adm_no)

    #button to check their report using matplotlib.
    sub_find=Button(windowT,text="SUBMIT",fg='white',bg='black',relief=RIDGE,font=("Constantia",13),width=10,command=submit)
    sub_find.place(x=420,y=400)

    #add marks label
    add_label=Label(windowT,text="Add marks:",bg="pink",fg="red",font=("Constantia",20,"bold"))
    add_label.place(x=210,y=470)

    #exam type buttons(functions are their in the extramarks.py file)
    button_Q=Button(windowT,text="Quarterly",fg='blue',bg='light yellow',relief=RIDGE,font=("Constantia",14),width=10,command=Quarterly)
    button_Q.place(x=250,y=540)

    button_H=Button(windowT,text="Half yrly",fg='blue',bg='light yellow',relief=RIDGE,font=("Constantia",14),width=10,command=Halfyrly)
    button_H.place(x=500,y=540)

    button_A=Button(windowT,text="Annual",fg='blue',bg='light yellow',relief=RIDGE,font=("Constantia",14),width=10,command=annual)
    button_A.place(x=750,y=540)

