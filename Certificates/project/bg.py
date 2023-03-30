import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
root=tk.Tk()
root.title('CertiGen')
root.geometry("1199x700+100+50")
img1 = ImageTk.PhotoImage(Image.open("C:\\Users\Dell\OneDrive\Desktop\Certificates\project\sw.jpg"))
label = tk.Label(root,image=img1)
label.place(x=0,y=0,width=1199,height=700)

root.mainloop()