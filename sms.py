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

def displaystudent():

    q='select *from students'
    conncursor.execute(q)
    fetched = conncursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched:
        studentTable.insert('', END, value=data)


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

    #studentPhoneLabel = Label(searchstudentwindow, text='Mobile', font=('times new roman', 17))
    #studentPhoneLabel.grid(row=2, column=0, sticky=W, padx=20, pady=20)
    #studentPhoneEntry = Entry(searchstudentwindow, bd=7, font=('times new roman', 17))
    #studentPhoneEntry.grid(row=2, column=1, sticky=W, padx=20, pady=20)

    #studentEmailLabel = Label(searchstudentwindow, text='Email', font=('times new roman', 17))
    #studentEmailLabel.grid(row=3, column=0, sticky=W, padx=20, pady=20)
    #studentEmailEntry = Entry(searchstudentwindow, bd=7, font=('times new roman', 17))
    #studentEmailEntry.grid(row=3, column=1, sticky=W, padx=20, pady=20)

    #sGenderLabel = Label(searchstudentwindow, text='Gender', font=('times new roman', 17))
    #sGenderLabel.grid(row=4, column=0, sticky=W, padx=20, pady=20)
    #sGenderEntry = Entry(searchstudentwindow, bd=7, font=('times new roman', 17))
    #sGenderEntry.grid(row=4, column=1, sticky=W, padx=20, pady=20)

    #studentDoBLabel = Label(searchstudentwindow, text='DOB', font=('times new roman', 17))
    #studentDoBLabel.grid(row=5, column=0, sticky=W, padx=20, pady=20)
    #studentDoBEntry = Entry(searchstudentwindow, bd=7, font=('times new roman', 17))
    #studentDoBEntry.grid(row=5, column=1, sticky=W, padx=20, pady=20)

    #EmerContactLabel = Label(searchstudentwindow, text='Emergency Contact', font=('times new roman', 17))
    #EmerContactLabel.grid(row=6, column=0, sticky=W, padx=20, pady=20)
    #EmerContactEntry = Entry(searchstudentwindow, bd=7, font=('times new roman', 17))
    #EmerContactEntry.grid(row=6, column=1, sticky=W, padx=20, pady=20)

    #EmernumLabel = Label(searchstudentwindow, text='Emergency #', font=('times new roman', 17))
    #EmernumLabel.grid(row=7, column=0, sticky=W, padx=20, pady=20)
    #EmernumEntry = Entry(searchstudentwindow, bd=7, font=('times new roman', 17))
    #EmernumEntry.grid(row=7, column=1, sticky=W, padx=20, pady=20)

    search_studentButton = ttk.Button(searchstudentwindow, text='Search Student', command=search_input)
    search_studentButton.grid(rowspan=8, columnspan=2, pady=15)

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

def updatestudent():
    def update_input():
        q='update students set name=%s,mobile=%s,email=%s,gender=%s,dob=%s,emergency_contact=%s,emergency_number=%s'
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
            query="create table students(id int not null primary key, name varchar(30), mobile varchar(10)," \
              " email varchar(30), gender varchar(10), dob varchar(20), emergency contact varchar(30)," \
                  " emergency number varchar(10))"
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



#Student Info Frame
#leftupperFrame = Frame(root, highlightbackground='green', highlightthickness=2, relief=GROOVE)
#leftupperFrame.place(x=20, y=80, width=435, height=360)



#Buttons Frame

leftcenterFrame = Frame(root,highlightbackground='green', highlightthickness=2, relief=GROOVE)
leftcenterFrame.place(x=455, y=80, width=900, height=60)

addstudentButton=ttk.Button(leftcenterFrame, text=' Add Student', command=add_student)
addstudentButton.grid(row=1,column=0,padx=25)

updateStudentButton=ttk.Button(leftcenterFrame, text='Update Student', command=updatestudent)
updateStudentButton.grid(row=1,column=3, padx=25)

deletestudentButton=ttk.Button(leftcenterFrame, text='Delete Student', command=deletestudent)
deletestudentButton.grid(row=1,column=5, padx=25)

searchStudentButton=ttk.Button(leftcenterFrame, text='Search Student', command=searchstudent)
searchStudentButton.grid(row=1,column=2, padx=25)

displayStudentButton=ttk.Button(leftcenterFrame, text='Display Student', command=displaystudent)
displayStudentButton.grid(row=1,column=4, padx=25)

exportStudentButton=ttk.Button(leftcenterFrame, text='Export')
exportStudentButton.grid(row=1,column=6,pady=15, padx=25)


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
caleventFrame.place(x=20, y=420, width=400, height=413)

#Database Frame

centerupperFrame = Frame(root, highlightbackground='green', highlightthickness=2, relief=GROOVE)
centerupperFrame.place(x=435, y=150, width=950, height=260)

scrollBarX=Scrollbar(centerupperFrame, orient=HORIZONTAL)
scrollBarY=Scrollbar(centerupperFrame, orient=VERTICAL)

#Search Frame in DB Frame

searchFrame=ttk.Frame(centerupperFrame, relief=tkinter.GROOVE)
databaseButton=ttk.Button(centerupperFrame, text='Connect to Database', command=connect_database)
databaseButton.pack(side=tkinter.TOP, anchor=NE)

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
notesFrame.place(x=430, y=460, width=425, height=374)
n = "NOTES:"
sliderLabel = Label(root, text=n, font=('times new roman', 25, 'bold'))
sliderLabel.place(x=430, y=415)

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



root.mainloop()