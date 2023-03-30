from tkinter import *  
from tkinter import ttk,font
from tkinter import filedialog
from tkinter import colorchooser 
from PIL import Image,ImageTk 
root=Tk()  
#App Title  
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















#Calling Main()  
root.mainloop()  