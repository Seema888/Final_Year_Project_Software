from tkinter import *
import tkinter as tk  
from tkinter import ttk,font
from tkinter import filedialog
from tkinter import colorchooser 
from PIL import Image,ImageTk 
from tkinter import messagebox
  
class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (LoginPage, CertiGen):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(LoginPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class LoginPage(tk.Frame):
    def __init__(self,root, parent, controller):
        tk.Frame.__init__(self, parent)
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
    

  
          
  
  
# second window frame page1
class CertiGen(tk.Frame):
     
    def __init__(self,root, parent, controller):
         
        tk.Frame.__init__(self, parent)
        root.title("CertiGen")
        root.geometry("1199x700+100+50")  
        #ttk.Label(root, text="Automatic Certificate Generation System").pack()  
        #Create Panedwindow  
        panedwindow=ttk.Panedwindow(root, orient=HORIZONTAL)  
        panedwindow.pack(fill=BOTH, expand=True)  
        #Create Frams  
        fram1=ttk.Frame(panedwindow,width=400,height=300,relief=SUNKEN)  
        fram2=ttk.Frame(panedwindow,width=400,height=400,relief=SUNKEN)  
        panedwindow.add(fram1)  
        panedwindow.add(fram2)

        img1 = ImageTk.PhotoImage(Image.open("C:\\Users\Dell\OneDrive\Desktop\Certificates\project\CG.png"))
        label = Label(fram1,image=img1)
        label.place(x=0,y=0,relwidth=1,relheight=1)

        tabs=ttk.Notebook(fram2)

        tab1=Frame(tabs)
        tab2=Frame(tabs)
        tabs.add(tab1,text="Home")
        tabs.add(tab2,text="Customize")
        tab3=Frame(tabs,bg="yellow")
        tab4=Frame(tabs,bg="red")
        tabs.add(tab3,text="Destination")
        tabs.add(tab4,text="Email")
        tab5=Frame(tabs,bg="yellow")
        tabs.add(tab5,text="Generating")

        tabs.pack(expand=1,fill=BOTH)

        title=Label(tab1,text='Choose Your Excel File',font=('Arial',25,'bold'),fg='black').place(x=10,y=10)

        def browsefunc():
            tab1.path =filedialog.askopenfilename(initialdir="/",title="Select file",filetypes=(("txt files","*.txt"),("All files","*.*")))
    
        ent1=Entry(tab1,width=50)
        ent1.place(x=20,y=70)

        b1=Button(tab1,text="OPEN FILE",command=browsefunc)
        b1.place(x=350,y=70)

        title=Label(tab1,text='Choose Your Blank Certificate',font=('Arial',25,'bold'),fg='black').place(x=10,y=210)

        def browsefunc():
            tab1.path =filedialog.askopenfilename(initialdir="/",title="Select file",filetypes=(("txt files","*.txt"),("All files","*.*")))
    
        ent1=Entry(tab1,width=50)
        ent1.place(x=20,y=270)

        b1=Button(tab1,text="OPEN FILE",command=browsefunc)
        b1.place(x=350,y=270)

        Next_btn=Button(tab1,cursor="hand2",text='Next',fg='black',font=('times new roman',15)).place(x=350,y=470,width=100,height=25)  


        title=Label(tab2,text='Choose Columns ',font=('Arial',20,'bold'),fg='black').place(x=10,y=10)
        listbox=Listbox(tab2,selectmode=SINGLE)
        listbox.insert(1,'Name')
        listbox.insert(2,'Role')
        listbox.insert(3,'Branch')
        listbox.insert(4,'College')
        listbox.insert(5,'Email Id')
        listbox.place(x=10,y=50)

        def my_window():
            top=Toplevel()
            top.title("Selet Region")
            top.geometry("750x700+100+50")
            top.resizable(False,False)
            #ttk.Label(top, text="Select Region for ' ' column and hit Done",font=('Arial,20')).pack()  
            img = ImageTk.PhotoImage(Image.open("C:\\Users\Dell\OneDrive\Desktop\Certificates\project\certificate3.jpg"))
            label = Tk.Label(top,image=img)
            label.place(x=0,y=0,relwidth=1,relheight=1)


            Select_Region_btn=Button(tab2,cursor="hand2",text='Select Region',command=my_window,fg='black',font=('times new roman',15)).place(x=10,y=250,width=150,height=25)  
            Back_btn=Button(tab2,cursor="hand2",text='Back',fg='black',font=('times new roman',15)).place(x=10,y=500,width=100,height=25)  


            my_font=font.families()
            title=Label(tab2,text='Configure Fonts',font=('Arial',20,'bold'),fg='black').place(x=270,y=10)
            title=Label(tab2,text='Font Family',font=('Arial',15),fg='black').place(x=270,y=50)
            com=ttk.Combobox(tab2,width=40,values=my_font)
            com.current(12)
            com.place(x=270,y=90)

            title=Label(tab2,text='Font Size',font=('Arial',15),fg='black').place(x=270,y=130)
            listbox=Listbox(tab2,selectmode=SINGLE)
            listbox.insert(1,8)
            listbox.insert(2,10)
            listbox.insert(3,12)
            listbox.insert(4,14)
            listbox.insert(5,16)
            listbox.insert(6,18)
            listbox.insert(7,20)
            listbox.insert(8,36)
            listbox.insert(9,48)
            listbox.place(x=270,y=160)

            title=Label(tab2,text='Font Color',font=('Arial',15),fg='black').place(x=270,y=330)
            def click():
                color=colorchooser.askcolor()

                button=Button(tab2,text='Choose Color',width=20,command=click)
                button.place(x=270,y=370)

                Next_btn=Button(tab2,cursor="hand2",text='Next',fg='black',font=('times new roman',15)).place(x=390,y=490,width=100,height=25)  

  
  
# Driver Code
app = tkinterApp()
app.mainloop()