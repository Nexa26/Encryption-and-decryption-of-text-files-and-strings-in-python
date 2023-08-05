
from tkinter import *

import tkinter.font as font
  
# Create object  
root = Tk() 
root.title("ENCRYPTION AND DECRYPTION")

# Adjust size  
root.geometry("400x400") 
 
# Add image file 
bg = PhotoImage(file = "bgimg4.png") 
  
# Create Canvas 
canvas1 = Canvas( root, width = 400, 
                 height = 400) 
  
canvas1.pack(fill = "both", expand = True) 
  
# Display image 
canvas1.create_image( 0, 0, image = bg, anchor = "nw") 

# Add Text 

canvas1.create_text( 700,50, text = "ENCRYPTION AND DECRYPTION",fill='white',font='bold') 
#canvas1.create_text(500,500,text="Hi",fill='white',font='bold')
def strings():
    import string_ednc

# Create Buttons 
#button1 = Button( root, text = "Exit",command=strings) 
button3 = Button( root, text = "Start",command=strings) 
#button2 = Button( root, text = "Reset") 
  
# Display Buttons 

#button1_canvas = canvas1.create_window( 100, 10,  
                                       #anchor = "nw", 
                                       #window = button1) 
  
#button2_canvas = canvas1.create_window( 100, 40, 
                                      # anchor = "nw", 
                                      # window = button2) 
  
button3_canvas = canvas1.create_window( 100, 70, anchor = "nw", 
                                       window = button3) 

# Execute tkinter 
root.mainloop() 

