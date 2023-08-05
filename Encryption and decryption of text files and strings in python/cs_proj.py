from tkinter import *
from PIL import ImageTk,Image 
import tkinter.font as font
  
# Create object  
root = Tk() 
root.geometry("2000x2000") 
root.title("ENCRYPTION AND DECRYPTION")

root['background']='black'
Bg=PhotoImage(file=r"D:\PES\Previous_projects\sem1_python\img7.png")

lb1=Label(root,image=Bg)
lb1.place(x=0,y=0)
l1=Label(root,text="Do you want to work with files or strings?",fg='snow',bg='black',font=('Algerian',30,'underline','italic'))
l1.place(x=285,y=200)
def string_edn():
    import string_ednc
def files_edn():
    import upl
b1=Button(root,text='Strings',command=string_edn,bg = "black",fg = "sky blue",font=('Castellar',18,'bold','italic'),borderwidth = 5,width = 10,relief="groove")
b1.place(x=425,y=350)
b2=Button(root,text='Files',command=files_edn,bg = "black",fg = "sky blue",font=('Castellar',18,'bold','italic'),borderwidth = 5,width = 10,relief="groove")
b2.place(x=875,y=350)
root.mainloop()