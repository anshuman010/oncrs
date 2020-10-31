from tkinter import *
import back

#calling functions to create database tables
back.create()
back.createadmin()



#admin login window
def admin():

    root= Tk()
    root.geometry("400x600+450+100")
    root.resizable(0, 0)
    root.configure(bg="cyan")
    title=Label(root,text="ADMIN LOGIN",font=("times new roman",35,"bold"),bg="red")
    title.place(x=25,y=8)
    frame=Frame(root,bd=4,relief=RIDGE,bg="white")
    frame.place(x=20,y=70,width=350,height=520)

    varA=StringVar(root)
    varB=StringVar(root)
    
    username = Entry(root, font=13, bd=2, textvariable=varA)
    Label(root, text='admin id',bd=2, fg='#34383C', bg='white', font=('Helvetica 11 bold', 14), width="10").place(x=75, y=150)

    password = Entry(root, font=13,bd=2, textvariable=varB)
    Label(root, text='Password', fg='#34383C', bg='white', font=('Helvetica 11 bold',14),width="10").place(x=75, y=260)

    username.place(x=80, y=200)
    password.place(x=80, y=300)

    login = Button(root,text="login", bg='black',fg="white", borderwidth=2,width='10',command=lambda :back.adminlogin(root,varA.get(),varB.get()))
    login.place(x=80, y=350)





    root.mainloop()
#user login window
def userlogin():
    root = Tk()
    root.geometry("400x600+450+100")
    root.resizable(0, 0)
    root.configure(bg="cyan")
    title = Label(root, text="USER LOGIN", font=("times new roman", 35, "bold"), bg="red")
    title.place(x=25, y=8)
    frame = Frame(root, bd=4, relief=RIDGE, bg="white")
    frame.place(x=20, y=70, width=350, height=520)

    varA=StringVar(root)
    varB=StringVar(root)
    
    username = Entry(root, font=13, bd=2, textvariable=varA)
    Label(root, text='user id', bd=2, fg='#34383C', bg='white', font='Helvetica 11 bold', width="5").place(x=80, y=150)

    password = Entry(root, font=13, bd=2, textvariable=varB)
    Label(root, text='Password', fg='#34383C', bg='white', font='Helvetica 11 bold', width="10").place(x=80, y=250)

    username.place(x=80, y=200)
    password.place(x=80, y=300)

    login = Button(root, text="login", bg='black', fg="white", borderwidth=2, width='10', command=lambda: back.sign_in(root, varA.get(), varB.get()))

    login.place(x=80, y=350)

    
    #ui
def index():
    win=Tk()
    title=win.title("hello")
    win.geometry("900x600+300+100")
    win.resizable(0, 0)
    win.title("oncrs")
    bg = PhotoImage(file="background.gif")
    Label(win, image=bg).grid(row=0, column=0, rowspan=20, columnspan=20)
    Label(win, text='Welcome', font='Helvetica 18 ', fg='white', bg='#34383C').place(x=50, y=230)
    Label(win, text=' online Criminal REPORTING System', font='Helvetica 12 ', fg='white', bg='#34383C').place(x=50, y=260)
    Label(win, text='Add and view the records using this interactive application',font='Helvetica 10', fg='#0D90CB', bg='#34383C').place(x=50, y=290)


    login_button = Button(win,text="admin login", width='12', height='2', borderwidth=0, bg='#1A2E39', fg="white",command=admin)
    login_button.place(x=640, y=200)

    login = Button(win, text="user login", width='12', height='2', borderwidth=0, bg='#1A2E39', fg="white",command=lambda :userlogin()).place(x=640, y=280)

    reg = Button(win, text="user registration", width='12', height='2', borderwidth=0, bg='#1A2E39', fg="white", command=back.create_acc)
    reg.place(x=640, y=360)

    win.mainloop()

index()
