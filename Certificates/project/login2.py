from tkinter import *
from PIL import ImageTk
win = Tk()
win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.pack()
#frame.place(anchor='center', relx=0.5, rely=0.5)

img = open(file=("C:\\Users\Dell\OneDrive\Desktop\Certigen.PNG"))

label = Label(frame, image = img)
label.pack()

win.mainloop()