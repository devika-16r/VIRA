from tkinter import*
from PIL import Image , ImageTk
import action 
import spech_to_text 


def User_send():
    send = entry1.get()
    VIRA = action.Action(send)
    text.insert(END, "Me --> "+send+"\n")
    if VIRA != None:
        text.insert(END, "VIRA <-- "+ str(VIRA)+"\n")
    entry1.delete(0, END)
    if VIRA == "ok sir":
          root.destroy()  
          

def ask():

    ask_val= spech_to_text.spech_to_text()
    VIRA_val = action.Action(ask_val)
    text.insert(END, "Me --> "+ask_val+"\n") 
    if VIRA_val != None:
       text.insert(END, "VIRA <-- "+ str(VIRA_val)+"\n")
    if VIRA_val == "ok sir":
        root.destroy()

def delete_text():
    text.delete("1.0", "end")


root = Tk()
root.geometry("600x700")
root.title("VIRA")
root.resizable(False,False)
root.config(bg="#0F172A")

  


# Main Frame
Main_frame = LabelFrame(root , padx=100 ,  pady=7 , borderwidth=3 ,  relief="raised")
Main_frame.config(bg="#1E293B")
Main_frame.grid(row = 0 ,  column= 1 ,  padx= 55 ,  pady =  10)

# Text Lable 
Text_lable = Label(
    Main_frame,
    text="VIRA",
    font=("Poppins", 20, "bold"),
    bg="#1E293B",
    fg="#38BDF8"
)
Text_lable.grid(row=0 ,  column=0 , padx=20 , pady= 10)


# Image 
img = Image.open("image/vira.png")

img = img.resize((240, 240), Image.LANCZOS)

Display_Image = ImageTk.PhotoImage(img)

Image_Lable = Label(Main_frame, image=Display_Image)

Image_Lable.image = Display_Image

Image_Lable.grid(row=1, column=0, pady=20)


# Add a text widget

#text=Text(root , font= ('Courier 10 bold') , bg = "#356696")
text = Text(
    root,
    font=('Courier 10 bold'),
    bg="#111827",      # background
    fg="white",        # text color
    insertbackground="white",
    bd=0
)
text.grid(row = 2,  column= 0)
text.place(x= 100, y= 375, width= 375, height= 100) 




# Add a entry widget
# Entry Box
entry1 = Entry(
    root,
    justify=CENTER,
    font=("Poppins", 12),
    bg="white",
    fg="black",
    insertbackground="black",
    bd=3,
    relief=FLAT
)

entry1.place(x=100, y=500, width=350, height=40)
entry1.bind("<Return>", lambda event: User_send())



# ASK Button
button1 = Button(
    root,
    text="ASK",
    font=("Poppins", 10, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#38BDF8",
    activeforeground="black",
    pady=12,
    padx=35,
    borderwidth=0,
    relief=SOLID,
    cursor="hand2",
    command=ask
)

button1.place(x=140, y=560)


# SEND Button
'''button2 = Button(
    root,
    text="SEND",
    font=("Poppins", 10, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#38BDF8",
    activeforeground="black",
    pady=12,
    padx=35,
    borderwidth=0,
    relief=SOLID,
    cursor="hand2",
    command=User_send
)

button2.place(x=400, y=575)'''


# DELETE Button
button3 = Button(
    root,
    text="DELETE",
    font=("Poppins", 10, "bold"),
    bg="#DC2626",
    fg="white",
    activebackground="#F87171",
    activeforeground="black",
    pady=12,
    padx=30,
    borderwidth=0,
    relief=SOLID,
    cursor="hand2",
    command=delete_text
)

button3.place(x=320, y=560)

root.mainloop()