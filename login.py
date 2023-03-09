from tkinter import *
from tkinter import messagebox

def login():
    if userEntry.get()=='' or passEntry.get()=='' :
        messagebox.showerror('Error', 'Please input Username and Password')
    elif userEntry.get()== 'admin' and passEntry.get()=='1234' :
        messagebox.showinfo('Login Successful', 'Welcome')
        lgwindow.destroy()
        import sms

    else:
        messagebox.showerror('Error', 'Please enter correct Username and Password')

lgwindow=Tk()

lgwindow.geometry('1280x700+300+150')
lgwindow.title('Student Management System Login')

lgwindow.resizable(False, False)

bgImage=PhotoImage(file='plantbg.png')
bgLabel=Label(lgwindow, image=bgImage)
bgLabel.place(x=0, y=0)

lgFrame=Frame(lgwindow, bg='#e9e8e6')
lgFrame.place(x=60, y=80)

LogoImage=PhotoImage(file='lab.png')
logoLabel=Label(lgFrame, image=LogoImage)
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)
userImage=PhotoImage(file='user.png')
userLabel=Label(lgFrame, image=userImage, text='Username', compound=LEFT
                ,font=('times new roman', 24, 'bold'), bg='#e9e8e6')
userLabel.grid(row=1, column=0, pady=10, padx=20)

userEntry=Entry(lgFrame, font=('times new roman', 24, 'bold'), bd=5, fg='Black')
userEntry.grid(row=1, column=1, pady=10, padx=20)

passImage=PhotoImage(file='padlock.png')
passLabel=Label(lgFrame, image=passImage, text='Password', compound=LEFT
                ,font=('times new roman', 24, 'bold'), bg='#e9e8e6')
passLabel.grid(row=2, column=0, pady=10, padx=20)

passEntry=Entry(lgFrame, font=('times new roman', 24, 'bold'), bd=5, fg='Black')
passEntry.grid(row=2, column=1, pady=10, padx=20)

loginButton=Button(lgFrame, text= 'Login', font=('times new roman', 15, 'bold'), command=login ,cursor='hand2', width=20
                   ,bg='green', activebackground='green')
loginButton.grid(row=3, column=1, pady=10)


lgwindow.mainloop()