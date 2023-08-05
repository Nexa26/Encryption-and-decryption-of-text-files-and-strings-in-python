from tkinter import *
from cryptography.fernet import Fernet
from PIL import ImageTk,Image 
from key_string import key
# value of key is assigned to a variable 
f = Fernet(key) 
Root=Tk()
Root.title("ENCRYPTION OF STRINGS")
Root['background']='black'
Root.geometry("2000x2000")

# the plaintext is converted to ciphertext 
lb0=Label(Root,text= "Enter text to encrypt",font=('Algerian',20,'underline'),fg='white',bg='black')
lb0.pack(pady=25)
e = Entry(Root, width = 50)
e.pack(pady=10)
e.insert(0,'') 
def myClick1():
    
             inl=Label(Root,text="Text entered is",font=('Copperplate Gothic Bold',13),fg='blue',bg='black')
             inl.pack()
             #k="Text entered is:  " +e.get()
             k=e.get()
             message = k.encode()
             lb1 = Label(Root, text =message,font=('Arial',15),bg='black',fg='white')
             lb1.pack()

             lb2= Label(Root, text ="The encrypted message is :",font=('Copperplate Gothic Bold',13),fg='blue',bg='black')
             lb2.pack()
            
             encrypted = f.encrypt(message)
             lb3= Label(Root, text = encrypted,font=('Arial',15),bg='black',fg='white')
             lb3.pack()
             dip=Label(Root,text="View decrypted text",bg='black',font=('Copperplate Gothic Bold',13),fg='blue')
             dip.pack()
             
            
             def myClick2():
             
             
                
                
                    decrypted= f.decrypt(encrypted)
                    lb4= Label(Root, text="The message after decryption is:",font=('Copperplate Gothic Bold',13),fg='blue',bg='black')
                    lb4.pack()
                    lb5= Label(Root, text=decrypted,font=('Arial',15),bg='black',fg='white')
                    lb5.pack()
             bt2=Button(Root,text="Decrypt",command = myClick2,font=('Copperplate Gothic Bold',15),bg = "SkyBlue",fg = "white",borderwidth = 6,width = 10,relief="ridge")
             bt2.pack(pady=10)

               
            
             
        #print(decrypted_encrypted)
       # print('b’ in front of the original message indicates the byte format')
       # print()
        #print("Message without 'b':")
        #print(decrypted_encrypted.decode())
      

#print(decrypted_encrypted)
#b’ in front of the original message indicates the byte format

bt1 = Button(Root, text = "Encrypt", command = myClick1,font=('Copperplate Gothic Bold',15),bg = "SkyBlue",fg = "white",borderwidth = 6,width = 10,relief="ridge")#callback
bt1.pack(pady=15)
Root.mainloop()
