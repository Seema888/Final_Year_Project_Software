from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1199x700+100+50")
        self.root.resizable(False,False)
        #BG IMage
         
        #self.bg=ImageTk.PhotoImage(file="C:\\Users\Dell\OneDrive\Desktop\Certificates\login1.jpg")
        #self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        self.root.configure(bg='blue')

        #Login Frame

        Frame_login=Frame(self.root,bg='white')
        Frame_login.place(x=150,y=150,height=340,width=500)

        title=Label(Frame_login,text='Login Here',font=('Impact',35,'bold'),fg='#d77337',bg='white').place(x=90,y=30)
        
        desc=Label(Frame_login,text='Admin',font=('Goudy old style',15,'bold'),fg='#d25d17',bg='white').place(x=90,y=100)
        lbl_user=Label(Frame_login,text='Username',font=('Goudy old style',15,'bold'),fg='gray',bg='white').place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=('times new roman',15),bg='lightgray')
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass=Label(Frame_login,text='Password',font=('Goudy old style',15,'bold'),fg='gray',bg='white').place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=('times new roman',15),show='*',bg='lightgray')
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        forget_btn=Button(Frame_login,text='Forgat Password?',cursor="hand2",command=self.forget_password,bg='white',fg='#d77337',bd=0,font=('times new roman',12)).place(x=90,y=290)  
        Login_btn=Button(self.root,command=self.login_function,cursor="hand2",text='Login',fg='white',bg='#d77337',font=('times new roman',20)).place(x=300,y=470,width=180,height=40)  

    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_user.get()!="seema" or self.txt_pass.get()!="123456":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}\nYou have successfully login",parent=self.root)                

    def forget_password(self):
        self.root1=Tk()
        self.root1.title("Forget Password")
        self.root1.geometry("350x350+450+150")
        self.root1.config(bg="white")
        self.root1.resizable(False,False)

        t=Label(self.root1,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
        
        lbl_newpass=Label(self.root1,text='New password',font=('Goudy old style',15,'bold'),fg='gray',bg='white').place(x=50,y=100)
        self.txt_newpass=Entry(self.root1,font=('times new roman',15),show='*',bg='lightgray')
        self.txt_newpass.place(x=50,y=130,width=250,height=35)

        lbl_confirmpass=Label(self.root1,text='Confirm password',font=('Goudy old style',15,'bold'),fg='gray',bg='white').place(x=50,y=170)
        self.txt_confirmpass=Entry(self.root1,font=('times new roman',15),show='*',bg='lightgray')
        self.txt_confirmpass.place(x=50,y=210,width=250,height=35)

        Changepassword_btn=Button(self.root1,cursor="hand2",text='Change Password',fg='white',bg='red',font=('times new roman',15)).place(x=80,y=260)  


root=Tk()
obj=Login(root)
root.mainloop()    
