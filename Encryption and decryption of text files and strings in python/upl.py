from tkinter import filedialog
from tkinter import *
from cryptography.fernet import Fernet
from key_file import key
root=Tk()
root.title('ENCRYPTION AND DECRYPTION OF FILES')
root['background']='black'
l1=Label(root,text='Select file for encryption',fg='cyan',bg='black',font=('broadway',25,'underline'))
l1.pack(pady=5)
f = Fernet(key)
filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
 
l2=Label(root,text=filename,fg='azure',bg='black',font=('Lucida Handwriting',15))
l2.pack()
l3=Label(root,text=" is the path and name of the file selected for encryption and decryption",fg='azure',bg='black',font=('Copperplate Gothic Bold',15))
l3.pack()



fh = open(filename)
with open(filename, 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)
l4=Label(root,text="Enter the name of the encrypted file:",font=('Lucida Handwriting',15),fg='white',bg='black')
l4.pack(pady=5)
m = Entry(root, width = 50)
m.pack()
m.insert(0,'')
def saving_encfile():
    fl=m.get()
    f = Fernet(key)
    with open (fl, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    
    l5=Label(root,text="File has been encrypted",fg='white',bg='black',font=('Lucida Handwriting',15))
    l5.pack()
    def dec_file():
        with open(fl, 'rb') as encrypted_file:
            encrypted1= encrypted_file.read()
        decrypted = f.decrypt(encrypted1)
        l6=Label(root,text="Enter the name of the decrypted file:",font=('Lucida Handwriting',15),fg='white',bg='black')
        l6.pack()
        p= Entry(root, width = 50)
        p.pack()
        p.insert(0,'')
        def saving_decfile():
            fl1=p.get()
            with open(fl1, 'wb') as decrypted_file:
                decrypted_file.write(decrypted)
            l6=Label(root,text="File has been decrypted",font=('Lucida Handwriting',15),fg='white',bg='black')
            l6.pack()
            l7=Label(root,text="Do you want to view the content of the encrypted and decrypted files?",font=('Copperplate Gothic Bold',15),fg='white',bg='black')
            l7.pack()
            def disp():
                l9=Label(root,text="Encrypted file content",font=('Lucida Handwriting',15,'underline'),fg='white',bg='black')
                l9.pack()
                f=open(fl,'r')
                rd=f.read()
                rd=rd.strip()
                l8=Label(root,text=rd,font=('Arial',10),fg='white',bg='black')
                l8.pack()
                l10=Label(root,text="Decrypted file content",font=('Lucida Handwriting',15,'underline'),fg='white',bg='black')
                l10.pack()
                fl2=p.get()
                f1=open(fl2,'r')
                rd1=f1.read()
                rd1=rd1.strip()
                l11=Label(root,text=rd1,font=('Arial',10),fg='white',bg='black')
                l11.pack()
            def Close(): 
                root.destroy()
            b3=Button(root,text="View content",command=disp,font=('Algerian',10,'italic'),fg='black',bg='cyan',borderwidth = 5,width =11,relief="ridge")
            b3.pack(pady=5)
            b4 = Button(root, text="Exit", command=Close,font=('Algerian',10,'italic'),fg='black',bg='cyan',borderwidth = 5,width = 8,relief="ridge")
            b4.pack(pady=5)
        b3=Button(root,text="save file",command=saving_decfile,font=('broadway',15,'italic'),fg='black',bg='cyan',borderwidth = 6,width = 10,relief="ridge")
        b3.pack(pady=10)    
    b2=Button(root,text="Decrypt",command=dec_file,font=('broadway',11,'italic'),fg='black',bg='turquoise',borderwidth = 6,width = 8,relief="ridge")
    b2.pack()
    
b1=Button(root,text="Save file",command=saving_encfile,font=('broadway',15,'italic'),fg='black',bg='cyan',borderwidth = 6,width = 10,relief="ridge")
b1.pack(pady=8)

root.mainloop()

