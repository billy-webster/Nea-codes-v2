from tkinter import *
import sqlite3
import re
from tkinter.font import Font

#create db
#conn=sqlite3.connect("db.db")
#conn.execute("""
#CREATE TABLE ACCOUNTS(
#ACCOUNTS_ID INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL ,
#USERNAME TEXT NOT NULL, 
#PASSWORD TEXT NOT NULL,
#EMAIL TEXT NOT NULL)
#""")
#insert data

conn=sqlite3.connect("db.db")


conn.execute("INSERT INTO ACCOUNTS(USERNAME,PASSWORD,EMAIL) VALUES ('billy', '123', 'billywebster2019@outlook.com')");

conn.execute("INSERT INTO ACCOUNTS(USERNAME,PASSWORD,EMAIL) VALUES ('dan', '456','s201027@greenhead.ac.uk')");


conn.commit()

conn.close()

#read table
conn = sqlite3.connect('db.db')

cursor = conn.execute("SELECT * from ACCOUNTS")
print("ID\tUSERNAME\tPASSWORD\tEMAIL")
for row in cursor:
   print ("{}\t{}\t\t{}\t\t{}".format(row[0],row[1],row[2],row[3]))
conn.close()

def log_in():
    username1=username.get()
    password1=password.get()
    email2=email.get()
    if username1=="" or password1=="":
        message.set("Enter A Value")
    else:
        connect1 = sqlite3.connect("db.db")
        take = connect1.execute('SELECT * from ACCOUNTS where USERNAME="%s" and PASSWORD="%s" and EMAIL="%s"'%(username1,password1,email2))
        if take.fetchone():
            message.set("login success")
            import test
        else:
            message.set("invalid details")

#NOT USED IN CODE- TEMPLATE FOR CHECKING IF AN EMAIL IS A VALID FORMAT
def email_vaild(useremail1):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex,useremail1)):
        message1.set("valid email")
        return True

    else:
        message1.set("Use correct email format")
        return False




def sign_up():
    username2=username.get()
    password2=password.get()
    email2 = email.get()

    if username2=="" or password2=="" or email2=="":
        message.set("Enter A Value")
   
    else:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex,email2)):
            connect__ = sqlite3.connect("db.db")
            connect__.execute("INSERT INTO ACCOUNTS(USERNAME,PASSWORD,EMAIL) VALUES (?,?,?)",(username2,password2,email2))
            connect__.commit()
            connect__.close()     
            message.set("Account made")
        else:
            message.set("use correct email formaat")


def main_screen():
    
    #style-stuff
    mainscreen = Tk()
    mainscreen.geometry("500x500")
    mainscreen.title("Log In Form")
    mainscreen.resizable(0,0)
    mainscreen["bg"]="#b0bea9"
    

    OpenSans = Font(
    family="Open Sans Light",
    size=12,
    underline=0)

    
    # create text fields
    global message
    global message1
    global username
    global password
    global email
    username = StringVar()
    password = StringVar()
    message = StringVar()
    email = StringVar()
    message1 = StringVar()



    # create Labels
    Label(mainscreen,width="300", text="Login Form", bg="#92aa83",fg="white",font=("OpenSans",12,"normal")).pack()
    
    Label(mainscreen, text="Username: ",bg="#b0bea9",fg="white",font=("Arial",12,"bold")).place(x=20,y=50)
    Entry(mainscreen, textvariable=username,bg="#92aa83",fg="white",font=("Arial",12,"bold")).place(x=160,y=50)

    Label(mainscreen, text="Password: ",bg="#b0bea9",fg="white",font=("Arial",12,"bold")).place(x=20,y=90)
    Entry(mainscreen, textvariable=password,bg="#92aa83",fg="white",font=("Arial",12,"bold")).place(x=160,y=90)

    Label(mainscreen, text="Email: ",bg="#b0bea9",fg="white",font=("Arial",12,"bold")).place(x=20,y=130)
    Entry(mainscreen, textvariable=email,bg="#92aa83",fg="white",font=("Arial",12,"bold")).place(x=160,y=130)


    #Label for displaying login status[success/failed]
    Label(mainscreen, text="",textvariable=message,bg="#b0bea9",fg="white",font=("Arial",12,"bold")).place(x=100,y=320)
    Label(mainscreen, text="",textvariable=message1,bg="#b0bea9",fg="white",font=("Arial",12,"bold")).place(x=100,y=330)

    # create Login Buttons
    Button(mainscreen, text="Login", width=30, height=1,command=log_in, bg="#92aa83",fg="white",font=("Arial",12,"bold")).place(x=100,y=170)
    Button(mainscreen, text="SignUp", width=30, height=1,command=sign_up,bg="#92aa83",fg="white",font=("Arial",12,"bold")).place(x=100,y=250)
    
    
    


    #Icons and images
    mainscreen.iconbitmap(default='transparent.ico')
    photo = PhotoImage(file = "icon.png")
    
   
   





    mainscreen.mainloop()




main_screen()
