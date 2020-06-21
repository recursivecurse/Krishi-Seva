from tkinter import *
from algorithms import *
from Registrationform import *
from simple_linear_regression import *
from PIL import ImageTk,Image

#Defining Functions

def Quit():
    exit()

def Register():
    RegistrationForm()

def Analytics():
    Analysis()

window = Tk()
window.geometry("1300x800")
#window.config()
window.title("Krishi Seva")


C = Canvas(window,height=800,width=1000)
image = Image.open('farmer1.jpg')
photo = ImageTk.PhotoImage(image)
lab0 = Label(window,image=photo).place(x=0,y=0)
C.pack()
#but1 = Button(text="Click Me",font=("arial",14,"bold"),command=Predict).place(x=100,y=100)
label1 = Label(window,text="Welcome to Krishi Seva",font=("arial",20,"bold"),bg="#00FF00").place(x=500,y=30)
label2 = Label(window,text="Click below for Registration",font=("arial",20,"bold")).place(x=900,y=100)
but1    = Button(window,text="Click Me",font=("arial",14,"bold"),command=Register).place(x=900,y=200)

label3 = Label(window,text="Click below for Analytics Section",font=("arial",20,"bold")).place(x=10,y=100)
but2   = Button(window,text="Click Me",font=("arail",14,"bold"),command=Analytics).place(x=50,y=200)

but3  = Button(window,text="Quit",font=("arial",14,"bold"),command=Quit).place(x=1000,y=700)

window.mainloop()


