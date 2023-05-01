import tkinter
from tkinter import *
import time
from tkinter import ttk, messagebox
import ttkthemes
from tkcalendar import*
import pymysql
from tkinter import filedialog
from tkinter import font
import tkinter as tk

#Clock
def clock():
    date = time.strftime('%m/%d/%Y')
    ctime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text = f'    Date: {date}\nTime:{ctime}')
    datetimeLabel.after(1000,clock)

def displaydatabase():

    q='select *from students'
    conncursor.execute(q)
    fetched = conncursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched:
        studentTable.insert('', END, value=data)

def displayevents():
    query='select *from events'
    mycursor.execute(query)
    fetched=mycursor.fetchall()
    calen.delete(*calen.get_children())
    for data in fetched:
        calen.insert('', END, value=data)

def displaystudent():
    def update_input():
        q='update students set name=%s,mobile=%s,email=%s,gender=%s,dob=%s,emergency_contact=%s,emergency_number=%s'
        conncursor.execute(q,(studentnameEntry.get(),studentPhoneEntry.get(),studentEmailEntry.get(),sGenderEntry.get(),
                              studentDoBEntry.get(),EmerContactEntry.get(),EmernumEntry.get()))
        conn.commit()
        messagebox.showinfo('Success','Record Successfully Updated')
        updatestudentwindow.destroy()
        displaystudent()

    updatestudentwindow=Toplevel()
    updatestudentwindow.title('Student Record')
    updatestudentwindow.resizable(False,False)
    updatestudentwindow.grab_set()

    studentidLabel=Label(updatestudentwindow, text='Student ID', font=('times new roman', 17))
    studentidLabel.grid(row=0,column=0,sticky=W,padx=20,pady=20)
    studentidEntry=Entry(updatestudentwindow, bd=7, font=('times new roman',17))
    studentidEntry.grid(row=0,column=1,sticky=W,padx=20,pady=20)

    studentnameLabel=Label(updatestudentwindow, text='Name', font=('times new roman', 17))
    studentnameLabel.grid(row=1,column=0,sticky=W,padx=20,pady=20)
    studentnameEntry=Entry(updatestudentwindow, bd=7, font=('times new roman',17))
    studentnameEntry.grid(row=1,column=1,sticky=W,padx=20,pady=20)

    studentPhoneLabel=Label(updatestudentwindow, text='Mobile', font=('times new roman', 17))
    studentPhoneLabel.grid(row=2,column=0,sticky=W,padx=20,pady=20)
    studentPhoneEntry=Entry(updatestudentwindow, bd=7, font=('times new roman',17))
    studentPhoneEntry.grid(row=2,column=1,sticky=W,padx=20,pady=20)

    studentEmailLabel=Label(updatestudentwindow, text='Email', font=('times new roman', 17))
    studentEmailLabel.grid(row=3,column=0,sticky=W,padx=20,pady=20)
    studentEmailEntry=Entry(updatestudentwindow, bd=7, font=('times new roman',17))
    studentEmailEntry.grid(row=3,column=1,sticky=W,padx=20,pady=20)

    sGenderLabel=Label(updatestudentwindow, text='Gender', font=('times new roman', 17))
    sGenderLabel.grid(row=4,column=0,sticky=W,padx=20,pady=20)
    sGenderEntry = Entry(updatestudentwindow, bd=7,font=('times new roman',17))
    sGenderEntry.grid(row=4,column=1,sticky=W,padx=20,pady=20)

    studentDoBLabel=Label(updatestudentwindow, text='DOB', font=('times new roman', 17))
    studentDoBLabel.grid(row=5,column=0,sticky=W,padx=20,pady=20)
    studentDoBEntry=Entry(updatestudentwindow, bd=7, font=('times new roman',17))
    studentDoBEntry.grid(row=5,column=1,sticky=W,padx=20,pady=20)

    EmerContactLabel=Label(updatestudentwindow, text='Emergency Contact', font=('times new roman', 17))
    EmerContactLabel.grid(row=6,column=0,sticky=W,padx=20,pady=20)
    EmerContactEntry=Entry(updatestudentwindow, bd=7, font=('times new roman',17))
    EmerContactEntry.grid(row=6,column=1,sticky=W,padx=20,pady=20)

    EmernumLabel=Label(updatestudentwindow, text='Emergency #', font=('times new roman', 17))
    EmernumLabel.grid(row=7,column=0,sticky=W,padx=20,pady=20)
    EmernumEntry=Entry(updatestudentwindow, bd=7, font=('times new roman',17))
    EmernumEntry.grid(row=7,column=1,sticky=W,padx=20,pady=20)

    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    updatedata=content['values']
    studentidEntry.insert(0,updatedata[0])
    studentnameEntry.insert(0,updatedata[1])
    studentPhoneEntry.insert(0, updatedata[2])
    studentEmailEntry.insert(0, updatedata[3])
    sGenderEntry.insert(0, updatedata[4])
    studentDoBEntry.insert(0, updatedata[5])
    EmerContactEntry.insert(0, updatedata[6])
    EmernumEntry.insert(0, updatedata[7])

def add_student():

    def add_input():
        if studentidEntry.get()== '' or studentnameEntry.get() == '' or studentPhoneEntry.get() == '' or studentEmailEntry.get() == '' or sGenderEntry.get() == '' or studentDoBEntry.get()=='' or EmerContactEntry.get()=='' or EmernumEntry.get() == '':
            messagebox.showerror('Error', 'All Fields Required', parent= addstudentwindow)

        else:
            query='insert into students values(%s, %s, %s, %s, %s, %s, %s, %s)'
            conncursor.execute(query, (studentidEntry.get(),studentnameEntry.get(),studentPhoneEntry.get(), studentEmailEntry.get(),
                                  sGenderEntry.get(), studentDoBEntry.get(),EmerContactEntry.get(),EmernumEntry.get()))
            conn.commit()
            result = messagebox.askyesno('Confirm','Student Successfully Added. Reset fields?', parent=addstudentwindow)
            if result:
                studentidEntry.delete(0, END)
                studentnameEntry.delete(0, END)
                studentPhoneEntry.delete(0, END)
                studentEmailEntry.delete(0, END)
                sGenderEntry.delete(0, END)
                studentDoBEntry.delete(0, END)
                EmerContactEntry.delete(0, END)
                EmernumEntry.delete(0, END)
            else:
                pass
            query='select *from students'
            conncursor.execute(query)
            get_data=conncursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in get_data:
                datalist=list(data)
                studentTable.insert('', END, values=datalist)

    addstudentwindow=Toplevel()
    addstudentwindow.title('Add a Student')
    addstudentwindow.resizable(False,False)
    addstudentwindow.grab_set()

    studentidLabel=Label(addstudentwindow, text='Student ID', font=('times new roman', 17))
    studentidLabel.grid(row=0,column=0,sticky=W,padx=20,pady=20)
    studentidEntry=Entry(addstudentwindow, bd=7, font=('times new roman',17))
    studentidEntry.grid(row=0,column=1,sticky=W,padx=20,pady=20)

    studentnameLabel=Label(addstudentwindow, text='Name', font=('times new roman', 17))
    studentnameLabel.grid(row=1,column=0,sticky=W,padx=20,pady=20)
    studentnameEntry=Entry(addstudentwindow, bd=7, font=('times new roman',17))
    studentnameEntry.grid(row=1,column=1,sticky=W,padx=20,pady=20)

    studentPhoneLabel=Label(addstudentwindow, text='Mobile', font=('times new roman', 17))
    studentPhoneLabel.grid(row=2,column=0,sticky=W,padx=20,pady=20)
    studentPhoneEntry=Entry(addstudentwindow, bd=7, font=('times new roman',17))
    studentPhoneEntry.grid(row=2,column=1,sticky=W,padx=20,pady=20)

    studentEmailLabel=Label(addstudentwindow, text='Email', font=('times new roman', 17))
    studentEmailLabel.grid(row=3,column=0,sticky=W,padx=20,pady=20)
    studentEmailEntry=Entry(addstudentwindow, bd=7, font=('times new roman',17))
    studentEmailEntry.grid(row=3,column=1,sticky=W,padx=20,pady=20)

    sGenderLabel=Label(addstudentwindow, text='Gender', font=('times new roman', 17))
    sGenderLabel.grid(row=4,column=0,sticky=W,padx=20,pady=20)
    sGenderEntry = Entry(addstudentwindow, bd=7,font=('times new roman',17))
    sGenderEntry.grid(row=4,column=1,sticky=W,padx=20,pady=20)

    studentDoBLabel=Label(addstudentwindow, text='DOB', font=('times new roman', 17))
    studentDoBLabel.grid(row=5,column=0,sticky=W,padx=20,pady=20)
    studentDoBEntry=Entry(addstudentwindow, bd=7, font=('times new roman',17))
    studentDoBEntry.grid(row=5,column=1,sticky=W,padx=20,pady=20)

    EmerContactLabel=Label(addstudentwindow, text='Emergency Contact', font=('times new roman', 17))
    EmerContactLabel.grid(row=6,column=0,sticky=W,padx=20,pady=20)
    EmerContactEntry=Entry(addstudentwindow, bd=7, font=('times new roman',17))
    EmerContactEntry.grid(row=6,column=1,sticky=W,padx=20,pady=20)

    EmernumLabel=Label(addstudentwindow, text='Emergency #', font=('times new roman', 17))
    EmernumLabel.grid(row=7,column=0,sticky=W,padx=20,pady=20)
    EmernumEntry=Entry(addstudentwindow, bd=7, font=('times new roman',17))
    EmernumEntry.grid(row=7,column=1,sticky=W,padx=20,pady=20)

    add_studentButton=ttk.Button(addstudentwindow, text='Add Student', command=add_input)
    add_studentButton.grid(rowspan=8,columnspan=2, pady=15)

def add_event():
    def create_event():
        if addEventEntry.get() == '' or eDateEntry.get() == '' or eTimeEntry.get() == '' or eLocationEntry.get() == '':
            messagebox.showerror('Error', 'All fields Required', parent=addeventwindow)

        else:
            query='insert into events values(%s,%s,%s,%s)'
            mycursor.execute(query,(addEventEntry.get(),eDateEntry.get(),eTimeEntry.get(),eLocationEntry.get()))
            con.commit()
            result=messagebox.askyesno('Confirm','Event Created. Do you want to reset form?', parent=addeventwindow)
            if result:
                addEventEntry.delete(0, END)
                eDateEntry.delete(0, END)
                eTimeEntry.delete(0, END)
                eLocationEntry.delete(0, END)
            else:
                pass

            query='select *from events'
            mycursor.execute(query)
            fetch_data=mycursor.fetchall()
            calen.delete(*calen.get_children())
            for data in fetch_data:
                datalist=list(data)
                calen.insert('',END,values=datalist)

    addeventwindow=Toplevel()
    addeventwindow.grab_set()
    addeventwindow.resizable(False,False)

    addeventLabel=Label(addeventwindow, text='Event', font=('times new roman',20,'bold'))
    addeventLabel.grid(row=0,column=0,padx=30, pady=15)
    addEventEntry=Entry(addeventwindow,width=35,font=('times new roman',15,'bold'))
    addEventEntry.grid(row=0,column=1, pady=15, padx=10)

    eDateLabel=Label(addeventwindow, text='Date', font=('times new roman',20,'bold'))
    eDateLabel.grid(row=1,column=0,padx=30, pady=15)
    eDateEntry=Entry(addeventwindow, font=('times new roman',15,'bold'))
    eDateEntry.grid(row=1,column=1, pady=15, padx=1)

    eTimeLabel=Label(addeventwindow, text='Time', font=('times new roman',20,'bold'))
    eTimeLabel.grid(row=2,column=0,padx=30, pady=15)
    eTimeEntry=Entry(addeventwindow,font=('times new roman',15,'bold'))
    eTimeEntry.grid(row=2,column=1, pady=15, padx=10)

    eLocationLabel=Label(addeventwindow, text='Location', font=('times new roman',20,'bold'))
    eLocationLabel.grid(row=3,column=0,padx=30, pady=15)
    eLocationEntry=Entry(addeventwindow,width=35,font=('times new roman',15,'bold'))
    eLocationEntry.grid(row=3,column=1, pady=15, padx=10)

    addevent_button =ttk.Button(addeventwindow, text='Create Event', command=create_event)
    addevent_button.grid(row=4,columnspan=2, pady=15)

def searchstudent():
    def search_input():
        q = 'select * from students where id=%s or name=%s'
        conncursor.execute(q, (studentidEntry.get(),studentnameEntry.get()))
        studentTable.delete(*studentTable.get_children())
        get_data = conncursor.fetchall()
        for data in get_data:
            studentTable.insert('', END, value=data)


    searchstudentwindow = Toplevel()
    searchstudentwindow.title('Search for a Student')
    searchstudentwindow.resizable(False, False)
    searchstudentwindow.grab_set()

    studentidLabel = Label(searchstudentwindow, text='Student ID', font=('times new roman', 17))
    studentidLabel.grid(row=0, column=0, sticky=W, padx=20, pady=20)
    studentidEntry = Entry(searchstudentwindow, bd=7, font=('times new roman', 17))
    studentidEntry.grid(row=0, column=1, sticky=W, padx=20, pady=20)

    studentnameLabel = Label(searchstudentwindow, text='Name', font=('times new roman', 17))
    studentnameLabel.grid(row=1, column=0, sticky=W, padx=20, pady=20)
    studentnameEntry = Entry(searchstudentwindow, bd=7, font=('times new roman', 17))
    studentnameEntry.grid(row=1, column=1, sticky=W, padx=20, pady=20)

    search_studentButton = ttk.Button(searchstudentwindow, text='Search Student', command=search_input)
    search_studentButton.grid(rowspan=8, columnspan=2, pady=15)

def searchevent():
    def search_data():
        query='select *from events where event=%s or date=%s or time=%s or location=%s'
        mycursor.execute(query, (searcheventEntry.get(), eDateEntry.get(), eTimeEntry.get, eLocationEntry.get))
        calen.delete(*calen.get_children())
        fetch_data=mycursor.fetchall()
        for data in fetch_data:
            calen.insert('',END,values=data)


    searcheventwindow = Toplevel()
    searcheventwindow.title('Search for Event')
    searcheventwindow.resizable(False, False)
    searcheventwindow.grab_set()

    searcheventLabel=Label(searcheventwindow, text='Event', font=('times new roman',20,'bold'))
    searcheventLabel.grid(row=0,column=0,padx=30, pady=15)
    searcheventEntry=Entry(searcheventwindow,width=35,font=('times new roman',15,'bold'))
    searcheventEntry.grid(row=0,column=1, pady=15, padx=10)

    eDateLabel=Label(searcheventwindow, text='Date', font=('times new roman',20,'bold'))
    eDateLabel.grid(row=1,column=0,padx=30, pady=15)
    eDateEntry=Entry(searcheventwindow, font=('times new roman',15,'bold'))
    eDateEntry.grid(row=1,column=1, pady=15, padx=1)

    eTimeLabel=Label(searcheventwindow, text='Time', font=('times new roman',20,'bold'))
    eTimeLabel.grid(row=2,column=0,padx=30, pady=15)
    eTimeEntry=Entry(searcheventwindow,font=('times new roman',15,'bold'))
    eTimeEntry.grid(row=2,column=1, pady=15, padx=10)

    eLocationLabel=Label(searcheventwindow, text='Location', font=('times new roman',20,'bold'))
    eLocationLabel.grid(row=3,column=0,padx=30, pady=15)
    eLocationEntry=Entry(searcheventwindow,width=35,font=('times new roman',15,'bold'))
    eLocationEntry.grid(row=3,column=1, pady=15, padx=10)

    searchevent_button =ttk.Button(searcheventwindow, text='Search', command=search_data)
    searchevent_button.grid(row=4,columnspan=2, pady=15)


def deletestudent():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    contentid=content['values'][0]

    q='delete from students where id=%s'
    conncursor.execute(q,contentid)
    conn.commit()
    messagebox.showinfo('Deleted',f'Student ID {contentid} has been deleted successfully')
    q='select *from students'
    conncursor.execute(q)
    fetched=conncursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched:
        studentTable.insert('',END,value=data)

def deleteevent():
    indexing=calen.focus()
    print(indexing)
    content=calen.item(indexing)
    content_id=content['values'][0]
    query='delete from events where event=%s'
    mycursor.execute(query, content_id)
    con.commit()
    messagebox.showinfo('Deleted','Event has been Deleted')
    query='select *from events'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    calen.delete(*calen.get_children())
    for data in fetched_data:
        calen.insert('', END, values=data)


def updatestudent():
    def update_input():
        q='update students set name=%s,mobile=%s,email=%s,gender=%s,dob=%s,emergency_contact=%s,emergency_number=%s where id=%s'
        conncursor.execute(q,(studentnameEntry.get(),studentPhoneEntry.get(),studentEmailEntry.get(),sGenderEntry.get(),
                              studentDoBEntry.get(),EmerContactEntry.get(),EmernumEntry.get()))
        conn.commit()
        messagebox.showinfo('Success','Record Successfully Updated')
        updatestudentwindow.destroy()
        displaystudent()

    updatestudentwindow=Toplevel()
    updatestudentwindow.title('Update a Student')
    updatestudentwindow.resizable(False,False)
    updatestudentwindow.grab_set()

    studentidLabel=Label(updatestudentwindow, text='Student ID', font=('times new roman', 17))
    studentidLabel.grid(row=0,column=0,sticky=W,padx=20,pady=20)
    studentidEntry=Entry(updatestudentwindow, bd=7, font=('times new roman',17))
    studentidEntry.grid(row=0,column=1,sticky=W,padx=20,pady=20)

    studentnameLabel=Label(updatestudentwindow, text='Name', font=('times new roman', 17))
    studentnameLabel.grid(row=1,column=0,sticky=W,padx=20,pady=20)
    studentnameEntry=Entry(updatestudentwindow, bd=7, font=('times new roman',17))
    studentnameEntry.grid(row=1,column=1,sticky=W,padx=20,pady=20)

    studentPhoneLabel=Label(updatestudentwindow, text='Mobile', font=('times new roman', 17))
    studentPhoneLabel.grid(row=2,column=0,sticky=W,padx=20,pady=20)
    studentPhoneEntry=Entry(updatestudentwindow, bd=7, font=('times new roman',17))
    studentPhoneEntry.grid(row=2,column=1,sticky=W,padx=20,pady=20)

    studentEmailLabel=Label(updatestudentwindow, text='Email', font=('times new roman', 17))
    studentEmailLabel.grid(row=3,column=0,sticky=W,padx=20,pady=20)
    studentEmailEntry=Entry(updatestudentwindow, bd=7, font=('times new roman',17))
    studentEmailEntry.grid(row=3,column=1,sticky=W,padx=20,pady=20)

    sGenderLabel=Label(updatestudentwindow, text='Gender', font=('times new roman', 17))
    sGenderLabel.grid(row=4,column=0,sticky=W,padx=20,pady=20)
    sGenderEntry = Entry(updatestudentwindow, bd=7,font=('times new roman',17))
    sGenderEntry.grid(row=4,column=1,sticky=W,padx=20,pady=20)

    studentDoBLabel=Label(updatestudentwindow, text='DOB', font=('times new roman', 17))
    studentDoBLabel.grid(row=5,column=0,sticky=W,padx=20,pady=20)
    studentDoBEntry=Entry(updatestudentwindow, bd=7, font=('times new roman',17))
    studentDoBEntry.grid(row=5,column=1,sticky=W,padx=20,pady=20)

    EmerContactLabel=Label(updatestudentwindow, text='Emergency Contact', font=('times new roman', 17))
    EmerContactLabel.grid(row=6,column=0,sticky=W,padx=20,pady=20)
    EmerContactEntry=Entry(updatestudentwindow, bd=7, font=('times new roman',17))
    EmerContactEntry.grid(row=6,column=1,sticky=W,padx=20,pady=20)

    EmernumLabel=Label(updatestudentwindow, text='Emergency #', font=('times new roman', 17))
    EmernumLabel.grid(row=7,column=0,sticky=W,padx=20,pady=20)
    EmernumEntry=Entry(updatestudentwindow, bd=7, font=('times new roman',17))
    EmernumEntry.grid(row=7,column=1,sticky=W,padx=20,pady=20)

    update_studentButton=ttk.Button(updatestudentwindow, text='Update Student', command=update_input)
    update_studentButton.grid(rowspan=8,columnspan=2, pady=15)

    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    updatedata=content['values']
    studentidEntry.insert(0,updatedata[0])
    studentnameEntry.insert(0,updatedata[1])
    studentPhoneEntry.insert(0, updatedata[2])
    studentEmailEntry.insert(0, updatedata[3])
    sGenderEntry.insert(0, updatedata[4])
    studentDoBEntry.insert(0, updatedata[5])
    EmerContactEntry.insert(0, updatedata[6])
    EmernumEntry.insert(0, updatedata[7])



def connect_database():
    def connect():
        global conncursor, conn
        try:
            conn=pymysql.connect(host='localhost',user='root',password='1234!?')
            conncursor=conn.cursor()
            messagebox.showinfo('Success', 'Succesfully Connected to Database', parent=connectdbWindow)
        except:
            messagebox.showerror('Error', 'Credentials are Invalid', parent=connectdbWindow)
            return
        try:
            query='create database sms'
            conncursor.execute(query)
            query='use sms'
            conncursor.execute(query)

        except:
            query='use sms'
            conncursor.execute(query)

    connectdbWindow = Toplevel()
    connectdbWindow.grab_set()
    connectdbWindow.geometry('400x225+700+200')
    connectdbWindow.title('Connect to Database')
    connectdbWindow.resizable(0, 0)

    hostnameLabel=Label(connectdbWindow, text='Host Name',font=('times new roman', 15, 'bold'))
    hostnameLabel.grid(row=0, column=0, padx=20)
    hostEntry=Entry(connectdbWindow, font=('time new roman', 10, 'bold'), bd=2)
    hostEntry.grid(row=0, column=1, padx=30, pady=20)

    usernameLabel=Label(connectdbWindow, text='Username',font=('times new roman', 15, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)
    usernameEntry = Entry(connectdbWindow, font=('time new roman', 10, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=30, pady=20)

    pwLabel = Label(connectdbWindow, text='Password', font=('times new roman', 15, 'bold'))
    pwLabel.grid(row=2, column=0, padx=20)
    pwEntry = Entry(connectdbWindow, font=('time new roman', 10, 'bold'), bd=2)
    pwEntry.grid(row=2, column=1, padx=30, pady=20)

    connectButton = ttk.Button(connectdbWindow, text='CONNECT', command=connect)
    connectButton.grid(row=3, columnspan=2)

def connect_eventdb():
    def eventconnect():
        global mycursor, con
        try:
            con=pymysql.connect(host='localhost', user='root', password='1234!?')
            mycursor = con.cursor()
            messagebox.showinfo('Success', 'Connect to Calendar', parent=eventdbWindow)
        except:
            messagebox.showerror('Error', 'Credentials are Invalid', parent=eventdbWindow)
        try:
            query='create database eventcal'
            mycursor.execute(query)
            query='use eventcal'
            mycursor.execute(query)
            query='create table events(event varchar(100) not null, date varchar(10), time varchar(10), location varchar(50))'
            mycursor.execute(query)
        except:
            query='use eventcal'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Connect to Calendar', parent=eventdbWindow)
        eventdbWindow.destroy()
        addeventButton.config(state=NORMAL)
        searcheventButton.config(state=NORMAL)
        deleteeventButton.config(state=NORMAL)
        displayCalButton.config(state=NORMAL)

    eventdbWindow=Toplevel()
    eventdbWindow.grab_set()
    eventdbWindow.geometry('400x225+700+200')
    eventdbWindow.title('Calendar Connection')
    eventdbWindow.resizable(0, 0)

    hostnameLabel = Label(eventdbWindow, text='Host Name', font=('times new roman', 15, 'bold'))
    hostnameLabel.grid(row=0, column=0, padx=20)
    hostEntry = Entry(eventdbWindow, font=('time new roman', 10, 'bold'), bd=2)
    hostEntry.grid(row=0, column=1, padx=30, pady=20)

    usernameLabel = Label(eventdbWindow, text='Username', font=('times new roman', 15, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)
    usernameEntry = Entry(eventdbWindow, font=('time new roman', 10, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=30, pady=20)

    pwLabel = Label(eventdbWindow, text='Password', font=('times new roman', 15, 'bold'))
    pwLabel.grid(row=2, column=0, padx=20)
    pwEntry = Entry(eventdbWindow, font=('time new roman', 10, 'bold'), bd=2)
    pwEntry.grid(row=2, column=1, padx=30, pady=20)

    eventconnectButton = ttk.Button(eventdbWindow, text='CONNECT', command=eventconnect)
    eventconnectButton.grid(row=3, columnspan=2)


#GUI
root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('clearlooks')

root.geometry('1450x875+250+85')
root.resizable(0,0)
root.title('Student Management System')

bgImage=PhotoImage(file='smsbg.png')
bgLabel=Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

datetimeLabel = Label(root, text='', font=('times new roman', 8, 'bold'))
datetimeLabel.place(x=5, y=5)
clock()
s = "S.M.S"
sliderLabel = Label(root, text=s, font=('times new roman', 35, 'bold'))
sliderLabel.place(x=200, y=5)

##Student DB Buttons##
addstudentButton=ttk.Button(root, text=' Add Student', command=add_student)
addstudentButton.place(x=455, y=80)

updateStudentButton=ttk.Button(root, text='Update Student', command=updatestudent)
updateStudentButton.place(x=620, y=80)

deletestudentButton=ttk.Button(root, text='Delete Student', command=deletestudent)
deletestudentButton.place(x=785, y=80)

searchStudentButton=ttk.Button(root, text='Search Student', command=searchstudent)
searchStudentButton.place(x=960, y=80)

displayStudentButton=ttk.Button(root, text='Display Student', command=displaystudent)
displayStudentButton.place(x=1140, y=80)

exportStudentButton=ttk.Button(root, text='Export')
exportStudentButton.place(x=1320, y=80)


#Calendar
leftlowerFrame = Frame(root)
leftlowerFrame.place(x=20, y=80, width=400, height=330)

leftlowerFrame = Frame(root, relief=RAISED)
leftlowerFrame.place(x=20, y=80, width=400, height=330)

def getSelectedDate():
      nowDate = cal.get_date()
      self.ResultDate.set(nowDate)

cal = Calendar(leftlowerFrame, selectmode="day", date_pattern='dd-mm-yyyy', font=('times new roman', 9, 'bold'), padx=100)
cal.grid(row=0, column=0)

cal.pack(fill=BOTH, expand=1)

#Events Frame
caleventFrame = Frame(root,highlightbackground='green', highlightthickness=2, relief=GROOVE)
caleventFrame.place(x=20, y=460, width=900, height=380)

addeventButton=ttk.Button(root, text='Add Event',state=DISABLED, command=add_event)
addeventButton.place(x=30, y=420)

searcheventButton=ttk.Button(root, text='Search Events', state=DISABLED, command=searchevent)
searcheventButton.place(x=150, y=420)

deleteeventButton=ttk.Button(root, text='Delete Event', state=DISABLED, command=deleteevent)
deleteeventButton.place(x=280, y=420)

eventdbButton = ttk.Button(root, text='Connect to Calendar', command=connect_eventdb)
eventdbButton.place(x=780, y=420)

displayCalButton=ttk.Button(root, text='View Calendar', state=DISABLED, command=displayevents)
displayCalButton.place(x=400, y=420)

##Event Display Frame##
scrollBarX=Scrollbar(caleventFrame, orient=HORIZONTAL)
scrollBarY=Scrollbar(caleventFrame, orient=VERTICAL)

calen = ttk.Treeview(caleventFrame, columns=('Event', 'Date', 'Time', 'Location'),
                     xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

scrollBarX.config(command=calen.xview)
scrollBarY.config(command=calen.yview)

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

calen.pack(fill=BOTH, expand=1)

calen.heading('Event',text='Event')
calen.heading('Date', text='Date')
calen.heading('Time', text='Time')
calen.heading('Location', text='Location')

calen.config(show='headings')
#Database Frame

centerupperFrame = Frame(root, highlightbackground='green', highlightthickness=2, relief=GROOVE)
centerupperFrame.place(x=435, y=115, width=950, height=295)

scrollBarX=Scrollbar(centerupperFrame, orient=HORIZONTAL)
scrollBarY=Scrollbar(centerupperFrame, orient=VERTICAL)

#Dis/Con Frame in DB Frame

displayButton=ttk.Button(centerupperFrame, text='Display Database', command=displaydatabase)
displayButton.pack(side=tkinter.TOP, anchor=W)


databaseButton=ttk.Button(centerupperFrame, text='Connect to Database', command=connect_database)
databaseButton.pack(side=tkinter.TOP, anchor=E)

#Database Frame

studentTable = ttk.Treeview(centerupperFrame, columns=('ID', 'Name', 'Mobile', 'Email', 'Gender', 'DOB',
                                                       'Emergency Contact', 'Emergency #'),
                            xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)
scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

studentTable.pack(fill=BOTH, expand=1)

studentTable.heading('ID',text='Student ID')
studentTable.heading('Name', text='Name')
studentTable.heading('Mobile', text='Mobile')
studentTable.heading('Email', text='Email')
studentTable.heading('Gender',text='Gender')
studentTable.heading('DOB', text='DOB')
studentTable.heading('Emergency Contact', text='Emergency Contact')
studentTable.heading('Emergency #', text='Emergency #')
studentTable.config(show='headings')

studentTable.column('ID',anchor=CENTER)



def new_file():
    my_text.delete('1.0', END)
    status_bar.config(text='New File       ')

def open_file():
    my_text.delete('1.0', END)
    textfile = filedialog.askopenfilename(title='Open File', filetypes=("Text Files", "*.txt"))
    name=textfile
    status_bar.config(text=name)
#Create Notes Frame
notesFrame = Frame(root, highlightbackground='green', highlightthickness=2, relief=GROOVE)
notesFrame.place(x=960, y=460, width=425, height=374)
n = "NOTES:"
sliderLabel = Label(root, text=n, font=('times new roman', 25, 'bold'))
sliderLabel.place(x=960, y=415)

#Scollbar
text_scroll = Scrollbar(notesFrame)
text_scroll.pack(side=RIGHT, fill=Y)

#Create Notes Text Box
my_text = Text(notesFrame, width=410, height=410, font=('times new roman', 16), selectbackground='yellow',
              selectforeground='black', undo=TRUE, yscrollcommand=text_scroll.set)
my_text.pack(pady=5)
#Scrollbar Config
text_scroll.config(command=my_text.yview)
#Menu Creation
my_menu = Menu(root)
root.config(menu=my_menu)
#File Menu
file_menu = Menu(my_menu, tearoff=FALSE)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save')
file_menu.add_command(label='Save As')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)
#Edit
edit_menu = Menu(my_menu, tearoff=FALSE)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Paste')
edit_menu.add_command(label='Undo')
edit_menu.add_command(label='Redo')
#Status
status_bar = Label(root, text='Ready       ', anchor=W)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

#Gradebook

#GradeDBFrame = Frame(root, highlightbackground='green', highlightthickness=2, relief=GROOVE)
#GradeDBFrame.place(x=950, y=460, width=425, height=374)
#n = "GRADEBOOK:"
#sliderLabel = Label(root, text=n, font=('times new roman', 25, 'bold'))
#sliderLabel.place(x=880, y=415)


root.mainloop()