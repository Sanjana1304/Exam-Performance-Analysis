#connecting with MySQL_database to store details.
import mysql.connector as sql
mycon=sql.connect(host="localhost",user="root",passwd="sanju123",database="Exam_Analysis")
cursor=mycon.cursor()

#for GUI
from tkinter import *
from tkinter import messagebox

def Quarterly():

    #window config.
    windowQ=Tk()
    windowQ.geometry("550x500")
    windowQ.config(bg="light yellow")
    windowQ.title("Quarterly Exam")

    #head label
    label_0=Label(windowQ,text="QUARTERLY MARKS",fg="black",bg="light yellow",relief="solid",font=("Copperplate Gothic",17,"bold"))
    label_0.place(x=120,y=35)

    #adm label
    label_1=Label(windowQ,text="Adm No:",fg="black",bg="light yellow",font=("Constantia",15))
    label_1.place(x=40,y=120)
    entry_1=Entry(windowQ,font=("Constantia",18))
    entry_1.place(x=140,y=120)

    #Math label
    label_2=Label(windowQ,text="Math:",fg="black",bg="light yellow",font=("Constantia",15))
    label_2.place(x=40,y=170)
    entry_2=Entry(windowQ,font=("Constantia",18))
    entry_2.place(x=140,y=170)

    #Sci ans sec label
    label_3=Label(windowQ,text="Science:",fg="black",bg="light yellow",font=("Constantia",15))
    label_3.place(x=40,y=220)
    entry_3=Entry(windowQ,font=("Constantia",18))
    entry_3.place(x=140,y=220)

    #Social label
    label_4=Label(windowQ,text="Social:",fg="black",bg="light yellow",font=("Constantia",15))
    label_4.place(x=40,y=270)
    entry_4=Entry(windowQ,font=("Constantia",18))
    entry_4.place(x=140,y=270)

    #English label
    label_5=Label(windowQ,text="English:",fg="black",bg="light yellow",font=("Constantia",15))
    label_5.place(x=40,y=320)
    entry_5=Entry(windowQ,font=("Constantia",18))
    entry_5.place(x=140,y=320)

    def enter_Q():
        adm = entry_1.get()
        math = entry_2.get()
        sci = entry_3.get()
        soc = entry_4.get()
        eng = entry_5.get()
        #print(adm,math,sci,soc,eng)
        query = "update studentt set math_q=%s,sci_q=%s,eng_q=%s,soc_q=%s where adm_no=%s"
        val = (math,sci,eng,soc,adm)
        cursor.execute(query,val)
        mycon.commit()

        label_D=Label(windowQ,text="Mark added !",fg="black",bg="light yellow",font=("Constantia",15))
        label_D.place(x=120,y=450)


    #enter marks button
    button_E=Button(windowQ,text="Enter marks",fg='black',bg='light yellow',relief=RIDGE,font=("Constantia",14),width=15,command=enter_Q)
    button_E.place(x=120,y=400)

def Halfyrly():
    windowQ=Tk()
    windowQ.geometry("550x500")
    windowQ.config(bg="light yellow")
    windowQ.title("Half yrly Exam")

    label_0=Label(windowQ,text="HALF YEARLY MARKS",fg="black",bg="light yellow",relief="solid",font=("Copperplate Gothic",17,"bold"))
    label_0.place(x=120,y=35)

    #adm label
    label_1=Label(windowQ,text="Adm No:",fg="black",bg="light yellow",font=("Constantia",15))
    label_1.place(x=40,y=120)
    entry_1=Entry(windowQ,font=("Constantia",18))
    entry_1.place(x=140,y=120)

    #Math label
    label_2=Label(windowQ,text="Math:",fg="black",bg="light yellow",font=("Constantia",15))
    label_2.place(x=40,y=170)
    entry_2=Entry(windowQ,font=("Constantia",18))
    entry_2.place(x=140,y=170)

    #Sci ans sec label
    label_3=Label(windowQ,text="Science:",fg="black",bg="light yellow",font=("Constantia",15))
    label_3.place(x=40,y=220)
    entry_3=Entry(windowQ,font=("Constantia",18))
    entry_3.place(x=140,y=220)

    #Social label
    label_4=Label(windowQ,text="Social:",fg="black",bg="light yellow",font=("Constantia",15))
    label_4.place(x=40,y=270)
    entry_4=Entry(windowQ,font=("Constantia",18))
    entry_4.place(x=140,y=270)

    #English label
    label_5=Label(windowQ,text="English:",fg="black",bg="light yellow",font=("Constantia",15))
    label_5.place(x=40,y=320)
    entry_5=Entry(windowQ,font=("Constantia",18))
    entry_5.place(x=140,y=320)

    def enter_H():
        adm = entry_1.get()
        math = entry_2.get()
        sci = entry_3.get()
        soc = entry_4.get()
        eng = entry_5.get()
        #print(adm,math,sci,soc,eng)
        query = "update studentt set math_h=%s,sci_h=%s,eng_h=%s,soc_h=%s where adm_no=%s"
        val = (math,sci,eng,soc,adm)
        cursor.execute(query,val)
        mycon.commit()

        label_D=Label(windowQ,text="Mark added !",fg="black",bg="light yellow",font=("Constantia",15))
        label_D.place(x=120,y=450)

    #enter marks button
    button_E=Button(windowQ,text="Enter marks",fg='black',bg='light yellow',relief=RIDGE,font=("Constantia",14),width=15,command=enter_H)
    button_E.place(x=120,y=400)

def annual():
    windowQ=Tk()
    windowQ.geometry("550x500")
    windowQ.config(bg="light yellow")
    windowQ.title("Annual Exam")

    label_0=Label(windowQ,text="ANNUAL MARKS",fg="black",bg="light yellow",relief="solid",font=("Copperplate Gothic",17,"bold"))
    label_0.place(x=120,y=35)

    #adm label
    label_1=Label(windowQ,text="Adm No:",fg="black",bg="light yellow",font=("Constantia",15))
    label_1.place(x=40,y=120)
    entry_1=Entry(windowQ,font=("Constantia",18))
    entry_1.place(x=140,y=120)

    #Math label
    label_2=Label(windowQ,text="Math:",fg="black",bg="light yellow",font=("Constantia",15))
    label_2.place(x=40,y=170)
    entry_2=Entry(windowQ,font=("Constantia",18))
    entry_2.place(x=140,y=170)

    #Sci ans sec label
    label_3=Label(windowQ,text="Science:",fg="black",bg="light yellow",font=("Constantia",15))
    label_3.place(x=40,y=220)
    entry_3=Entry(windowQ,font=("Constantia",18))
    entry_3.place(x=140,y=220)

    #Social label
    label_4=Label(windowQ,text="Social:",fg="black",bg="light yellow",font=("Constantia",15))
    label_4.place(x=40,y=270)
    entry_4=Entry(windowQ,font=("Constantia",18))
    entry_4.place(x=140,y=270)

    #English label
    label_5=Label(windowQ,text="English:",fg="black",bg="light yellow",font=("Constantia",15))
    label_5.place(x=40,y=320)
    entry_5=Entry(windowQ,font=("Constantia",18))
    entry_5.place(x=140,y=320)


    def enter_A():
        adm = entry_1.get()
        math = entry_2.get()
        sci = entry_3.get()
        soc = entry_4.get()
        eng = entry_5.get()
        #print(adm,math,sci,soc,eng)
        query = "update studentt set math_a=%s,sci_a=%s,eng_a=%s,soc_a=%s where adm_no=%s"
        val = (math,sci,eng,soc,adm)
        cursor.execute(query,val)
        mycon.commit()

        label_D=Label(windowQ,text="Mark added !",fg="black",bg="light yellow",font=("Constantia",15))
        label_D.place(x=120,y=450)

    #enter marks button
    button_E=Button(windowQ,text="Enter marks",fg='black',bg='light yellow',relief=RIDGE,font=("Constantia",14),width=15,command=enter_A)
    button_E.place(x=120,y=400)