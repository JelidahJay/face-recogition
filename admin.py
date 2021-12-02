from tkinter import*
from PIL import ImageTk
import pymysql
from tkinter import messagebox


root=Tk()
class Mainwindow:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN SYSTEM")
        self.root.geometry("1200x780+200+70")
        self.root.resizable(True,True)
        

#########ADDING IMAGE IN ROOT WINDOW ########
        self.image=ImageTk.PhotoImage(file="photos/bg4.jpg")
        self.label=Label(self.root,image=self.image)
        self.label.pack()
        
######## CREATING FRAME ON ROOT #######
        self.frame=Frame(self.root)
        self.frame.place(x=390,y=170,width=450,height=400)
        


######## CREATING LABELS AND ENTRY BOX ON FRAME ########
        self.userlabel=Label(self.frame,text="Identification",font=("Andalus",15),fg='gray')
        self.userlabel.place(x=80,y=50)

        self.entry1=Entry(self.frame,show="*",font=("times new roman", 15))
        self.entry1.place(x=80,y=100,width=250)

        self.passlabel=Label(self.frame,text="Password",font=("Andalus",15),fg='gray')
        self.passlabel.place(x=80,y=150)

        self.entry2=Entry(self.frame,show="*",font=("times new roman",15))
        self.entry2.place(x=80,y=200,width=250)

        self.button=Button(self.frame,text='Sign in',activebackground="#00B0F0",foreground='white',fg='gray',bg='#F0F8FF',font=("Arial",15),command=lambda:self.logindata())
        self.button.place(x=80,y=250,width=250)

        ########## create a database ########
    def logindata(self):
        con = pymysql.connect(host = "localhost", user = "root", password = "", database = "student_management")
        cur=con.cursor()
        cur.execute("Select * from admin where identification=%s and password=%s", (self.entry1.get(),self.entry2.get()))
        row=cur.fetchone()
        if row==None:
                messagebox.showerror("User not recognized")
        else:
                messagebox.showinfo("Successful Login")
                root.destroy()
                import attendance_with_antispoofing

main=Mainwindow(root)
root.mainloop()