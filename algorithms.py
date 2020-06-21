from tkinter import *
from algorithms import *
from Registrationform import *
from simple_linear_regression import *
from Agricuture import *
from PIL import ImageTk,Image

def Analysis():


    def Predict():
        regression()
    def Agri():
        agriculture()


    window = Tk()
    window.geometry("500x200")
    window.title("Welcome to Analytics Section")

    but1 = Button(window,text="Rainfall",font=("arial",14,"bold"),command=Predict).place(x=50,y=50)
    but2 = Button(window,text="Agriculture",font=("arial",14,"bold"),command=Agri).place(x=200,y=50)
    window.mainloop()