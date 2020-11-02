from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import mysql.connector
import re
from operator import itemgetter



def create():
    con = mysql.connector.connect(host='localhost', user='root', passwd='1237890',database="ocr")
    cur=con.cursor()

    cur.execute("create table if not exists admin(username varchar(20) PRIMARY KEY, password varchar(20))")
    cur.execute("create table if not exists createaccount(fname varchar(20) ,lname varchar(20),email varchar(20), password varchar(20))")
    cur.execute("create table if not exists crimedetails (fname varchar(20), lname varchar(20),gender varchar(20),faname varchar(20),state varchar(20),city varchar(20),street_no varchar(20),house_no varchar(20),deatils varchar(20),proof varchar(20))")
def createadmin():
        con = mysql.connector.connect(host='localhost', user='root', passwd='1237890',database="ocr")
        cur=con.cursor()
        cur.execute("select * from admin where username='admin'")
        status = cur.fetchall()
        if (len(status)) == 0:
            cur.execute("insert into admin values ('admin', 'admin')")
            con.commit()
            con.close()
        else:
            flag = 0



def create_acc():

    create_win = Toplevel()
    create_win.geometry("900x600+300+100")
    create_win.resizable(0, 0)
    create_win.configure(bg="yellow")
    Label(create_win, text="CREATE AN ACCOUNT", font="Helvetica 15 bold", fg='white', bg='#34383C').place(x=300, y=60)

    fname = Entry(create_win, font=(13))
    Label(create_win, text='first name', fg='#34383C', bg='white', font='Helvetica 11 bold').place(x=300, y=160)

    lname = Entry(create_win, font=(13))
    Label(create_win, text='last name', fg='#34383C', bg='white', font='Helvetica 11 bold').place(x=300, y=260)

    email = Entry(create_win,font=(13))
    Label(create_win, text='email', fg='#34383C', bg='white', font='Helvetica 11 bold').place(x=300, y=360)

    password = Entry(create_win, font=(13))
    Label(create_win,text='Password', fg='#34383C', bg='white', font='Helvetica 11 bold').place(x=300, y=460)

    fname.place(x=300, y=200)
    lname.place(x=300, y=300)
    email.place(x=300, y=400)
    password.place(x=300,y=500)

    Button(create_win, text=' ' * 20 + ' SUBMIT' + ' ' * 22, bg='#00BC90', fg='#34383C', font='Helvetica 15',borderwidth=0, command=lambda :submit()).place(x=270, y=550)

    def submit():
        if fname.get()=="" or lname.get()=="" or email.get() == "" or password.get()=="" :
            tkinter.messagebox.showerror('error',"all fields are required")

        elif (not (bool(re.match('[a-zA-Z\s]+$', fname.get())))):
            tkinter.messagebox.showerror(title="Error", message="Please Enter a Valid Name")

        elif (not (bool(re.match('[a-zA-Z\s]+$', lname.get())))):
            tkinter.messagebox.showerror(title="Error", message="Please Enter a Valid Name")

        elif (not (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email.get()))):
            tkinter.messagebox.showerror(title="Error", message="Please Enter a Valid email")



        elif (len(password.get()) < 8):
            tkinter.messagebox.showerror(title="Error", message="Please Enter a Strong Password")

        else:
            conn=mysql.connector.connect(host='localhost', user='root', passwd='1237890', database='OCR')
            cur1=conn.cursor()
            cur1.execute("select email from createaccount")
            p = []
            for i in cur1:
                p.append(i)

            res = list(map(itemgetter(0), p))
            email_no = email.get()
            k = len(res)
            i, flag = 0, 0
            while i < k:
                if res[i] == email.get():
                    tkinter.messagebox.showerror("Error", "Student with Entered EMAIL ADDRESS was Already Registered")
                    flag = 1
                    break
                i += 1
            conn.commit()
            if flag==0:
                conn1 = mysql.connector.connect(host='localhost', user='root', passwd='1237890', database='OCR')
                cur=conn1.cursor()
                cur.execute("insert into createaccount values(%s,%s,%s,%s)",(fname.get(),lname.get(),email.get(),password.get()))
                conn1.commit()
                tkinter.messagebox.showinfo("SUCCESS", "account register succesfully")
                conn1.close()



    create_win.mainloop()




def sign_in(root, username, password):
    con = mysql.connector.connect(host='localhost', user='root', passwd='1237890', database='ocr')
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM createaccount WHERE fname=%s and password=%s", (username, password))
    status = cur.fetchall()
    con.commit()
    if status[0][0] == 1:
        root.destroy()
        crimedetails()

    else:
        tkinter.messagebox.showerror("error","sign in failed")
        root.destroy()





def crimedetails():
    root = Tk()
    root.geometry("900x600+300+100")
    root.resizable(0, 0)
    root.configure(bg="cyan")


    userframe = Frame(root, bg="white", bd=5)
    userframe.place(x=20, y=50, width=350, height=548)
    title = Label(root, text="USER DETAILS", font=("times new roman", 15, "bold"), bg="red")
    title.place(x=70, y=10)

    Label(root, text='FIRST  NAME: ', font='Helvetica 11 bold', bg='#34383C', fg='white', borderwidth=0).place(x=40,
                                                                                                               y=100)
    fname = Entry(root, font='Helvetica 11 bold', fg='#373E44', bd=3)
    fname.place(x=150, y=100)

    Label(root, text='last name: ', font='Helvetica 11 bold', bg='#34383C', fg='white').place(x=40, y=160)
    lname = Entry(root, font='Helvetica 11 bold', fg='#373E44', bd=3)
    lname.place(x=150, y=160)

    Label(root, text='Gender: ', font='Helvetica 11 bold', bg='#34383C', fg='white').place(x=40, y=220)
    gender = Entry(root, font='Helvetica 11 bold', fg='#373E44')
    gender.place(x=150, y=220)

    Label(root, text='Fathers name: ', font='Helvetica 11 bold', bg='#34383C', fg='white').place(x=40, y=280)
    faname = Entry(root, font='Helvetica 11 bold', fg='#373E44')
    faname.place(x=150, y=280)

    Label(root, text='State: ', font='Helvetica 11 bold', bg='#34383C', fg='white').place(x=40, y=340)
    state = Entry(root, font='Helvetica 11 bold', fg='#373E44')
    state.place(x=150, y=340)

    Label(root, text='City: ', font='Helvetica 11 bold', bg='#34383C', fg='white').place(x=40, y=400)
    city = Entry(root, font='Helvetica 11 bold', fg='#373E44')
    city.place(x=150, y=400)

    Label(root, text='Street No: ', font='Helvetica 11 bold', bg='#34383C', fg='white').place(x=40, y=460)
    street_no = Entry(root, font='Helvetica 11 bold', fg='#373E44')
    street_no.place(x=150, y=460)

    Label(root, text='House No: ', font='Helvetica 11 bold', bg='#34383C', fg='white').place(x=40, y=520)
    house_no = Entry(root, font='Helvetica 11 bold', fg='#373E44')
    house_no.place(x=150, y=520)
    submit_details = Button(root, text="submit", bg="white", fg="black", font=14,command=lambda :submit())
    submit_details.place(x=80, y=560)

    detailsframe = Frame(root, bg="white", bd=5)
    detailsframe.place(x=530, y=50, width=350, height=548)
    title = Label(root, text="CRIME DETAILS", font=("times new roman", 15, "bold"), bg="red")
    title.place(x=600, y=10)

    Label(root, text="ENTER COMPLAINT DETAILS INCLUDING DATE AND TIME ", font='Helvetica 9 bold', bg='#34383C',fg='white').place(x=540, y=100)
    details = Entry(root, font='Helvetica 11 bold', fg='#373E44')
    details.place(x=560, y=160)

    Label(root, text="proof if any", font='Helvetica 10 bold', bg='#34383C', fg='white').place(x=540, y=200)
    proof = Entry(root, font='Helvetica 11 bold', fg='#373E44', bd=5)
    proof.place(x=560, y=240)



    def submit():
        if fname.get() == "" or lname.get() == "" :
            tkinter.messagebox.showerror('error', "all fields are required")

        else:
            con = mysql.connector.connect(host='localhost', user='root', passwd='1237890', database='ocr')
            cur = con.cursor()
            cur.execute("insert into crimedetails values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (fname.get(), lname.get(), gender.get(), faname.get(),state.get(),city.get(),street_no.get(),house_no.get(),details.get(),proof.get()))
            con.commit()
            tkinter.messagebox.showinfo("SUCCESS", "DETAILS SUBMITTED SUCCESSFULLY")
            con.close()


    root.mainloop()






def adminlogin(root, username, password):
    con = mysql.connector.connect(host='localhost', user='root', passwd='1237890',database="ocr")
    cur=con.cursor()
    cur.execute("SELECT COUNT(*) FROM admin WHERE username=%s and password=%s", (username, password))
    status = cur.fetchall()
    con.commit()
    if status[0][0] == 1:
        table()
    else:
        tkinter.messagebox.showerror("error", "signin failed")
        root.destroy()

def table():
    root = Tk()
    root.title("hello")
    root.geometry("800x600+300+100")
    frame = Frame(root, bd=4, relief=RIDGE, bg="red")
    frame.place(x=20, y=10, width=700, height=550)
    scroll_x = Scrollbar(frame, orient=HORIZONTAL)
    scroll_y = Scrollbar(frame, orient=VERTICAL)
    table = ttk.Treeview(frame, columns=(
            "fname", "lname", "gender", "faname", "state", "city", "street_no", "house_no", "details", "proof"),
                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=table.xview)
    scroll_y.config(command=table.yview)
    table.heading("fname", text="first name")
    table.heading("lname", text="last name")
    table.heading("gender", text="gender")
    table.heading("faname", text="father name")
    table.heading("state", text="state")
    table.heading("city", text="city")
    table.heading("street_no", text="street no")
    table.heading("house_no", text="house no")
    table.heading("details", text="details")
    table.heading("proof", text="proof")
    table['show'] = 'headings'
    table.pack(fill=BOTH, expand=1)

    def fetch():
        con = mysql.connector.connect(host='localhost', user='root', passwd='1237890', database='ocr')
        cur = con.cursor()
        cur.execute("select * from crimedetails ")

        for row in cur:
            table.insert("", END, values=row)
        con.commit()

        con.close()

    button = Button(frame, text="view", command=lambda: fetch()).place(x=10, y=500)
    root.mainloop()





