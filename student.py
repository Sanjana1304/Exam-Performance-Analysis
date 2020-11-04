#connecting with MySQL_database to store details.
import mysql.connector as sql
mycon=sql.connect(host="localhost",user="root",passwd="sanju123",database="Exam_Analysis")
cursor=mycon.cursor()

#for GUI
from tkinter import *
from tkinter import messagebox

#showing graphs for analysing their performance
import matplotlib.pyplot as plt

def homepageS(a,b):
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

    #name and class label
    name_label=Label(windowT,text="Name:",bg="pink",fg="black",font=("Constantia",17,"bold"))
    name_label.place(x=210,y=150)

    name_label=Label(windowT,text="Class:",bg="pink",fg="black",font=("Constantia",17,"bold"))
    name_label.place(x=520,y=150)

    #adding name and class in their resp. positions.
    query = "select name,class_sec from studentt where user_id=%s"
    val = (a,)
    cursor.execute(query,val)
    li=[]
    for i in cursor:
        for j in i:
            li.append(j)

    name_label=Label(windowT,text=li[0],bg="pink",fg="black",font=("Constantia",17))
    name_label.place(x=350,y=150)

    class_label=Label(windowT,text=li[1],bg="pink",fg="black",font=("Constantia",17))
    class_label.place(x=620,y=150)

    #report label
    rep_label=Label(windowT,text="Your Report:",bg="pink",fg="black",font=("Constantia",20,"bold"))
    rep_label.place(x=100,y=200)

    #column headings
    math_label=Label(windowT,text="Maths",bg="pink",fg="black",font=("Constantia",17))
    math_label.place(x=400,y=200)

    sci_label=Label(windowT,text="Science",bg="pink",fg="black",font=("Constantia",17))
    sci_label.place(x=520,y=200)

    soc_label=Label(windowT,text="Social",bg="pink",fg="black",font=("Constantia",17))
    soc_label.place(x=640,y=200)

    eng_label=Label(windowT,text="English",bg="pink",fg="black",font=("Constantia",17))
    eng_label.place(x=760,y=200)

    #row headings
    quar_label=Label(windowT,text="Quarterly",bg="pink",fg="black",font=("Constantia",17,"bold"))
    quar_label.place(x=100,y=280)

    half_label=Label(windowT,text="Half-yearly",bg="pink",fg="black",font=("Constantia",17,"bold"))
    half_label.place(x=100,y=360)

    annu_label=Label(windowT,text="Annual",bg="pink",fg="black",font=("Constantia",17,"bold"))
    annu_label.place(x=100,y=440)

    #avg label
    avg_label=Label(windowT,text="Average : ",bg="pink",fg="blue",font=("Constantia",19,"bold"))
    avg_label.place(x=100,y=520)

    query = "select math_q,sci_q,eng_q,soc_q,math_h,sci_h,eng_h,soc_h,math_a,sci_a,eng_a,soc_a from studentt where user_id=%s"
    val = (a,)
    mark_list=[]
    cursor.execute(query,val)
    for i in cursor:
        for j in i:
            mark_list.append(j)

    def checkReport():
        exams = ['Quarterly avg', 'Half yearly avg', 'Annual avg']
        #finding average
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

    #checkReport button
    button_checkR=Button(windowT,text="Check Report",fg='black',bg='light yellow',relief=RIDGE,font=("Constantia",17,"bold"),width=13,command=checkReport)
    button_checkR.place(x=520,y=520)

    #adding quarterly marks in their respective places.
    q1_label=Label(windowT,text=mark_list[0],bg="pink",fg="black",font=("Constantia",17,"bold"))
    q1_label.place(x=400,y=280)

    q2_label=Label(windowT,text=mark_list[1],bg="pink",fg="black",font=("Constantia",17,"bold"))
    q2_label.place(x=520,y=280)

    q3_label=Label(windowT,text=mark_list[3],bg="pink",fg="black",font=("Constantia",17,"bold"))
    q3_label.place(x=640,y=280)

    q4_label=Label(windowT,text=mark_list[2],bg="pink",fg="black",font=("Constantia",17,"bold"))
    q4_label.place(x=760,y=280)

    #adding halfyrly marks in their respective places.
    h1_label=Label(windowT,text=mark_list[4],bg="pink",fg="black",font=("Constantia",17,"bold"))
    h1_label.place(x=400,y=360)

    h2_label=Label(windowT,text=mark_list[5],bg="pink",fg="black",font=("Constantia",17,"bold"))
    h2_label.place(x=520,y=360)

    h3_label=Label(windowT,text=mark_list[7],bg="pink",fg="black",font=("Constantia",17,"bold"))
    h3_label.place(x=640,y=360)

    h4_label=Label(windowT,text=mark_list[6],bg="pink",fg="black",font=("Constantia",17,"bold"))
    h4_label.place(x=760,y=360)

    #adding annual marks in their respective places.
    a1_label=Label(windowT,text=mark_list[8],bg="pink",fg="black",font=("Constantia",17,"bold"))
    a1_label.place(x=400,y=440)

    a2_label=Label(windowT,text=mark_list[9],bg="pink",fg="black",font=("Constantia",17,"bold"))
    a2_label.place(x=520,y=440)

    a3_label=Label(windowT,text=mark_list[11],bg="pink",fg="black",font=("Constantia",17,"bold"))
    a3_label.place(x=640,y=440)

    a4_label=Label(windowT,text=mark_list[10],bg="pink",fg="black",font=("Constantia",17,"bold"))
    a4_label.place(x=760,y=440)

    #average mark label
    avg = sum(mark_list)/len(mark_list)
    avg = str(avg)
    avg = avg[:5]+"%"

    avg_label=Label(windowT,text=avg,bg="pink",fg="black",font=("Constantia",17,"bold"))
    avg_label.place(x=200,y=520)
