from tkinter import *
from tkinter import messagebox
import random

def play():
    player2 = "paper"
    if vari.get() == "stone" and player2 == "paper":
        Label(root,text = player2,font = ("Calibri(Body)",12,'bold')).place(x = 200,y = 250)
        
       


root = Tk()
root.title("game")
root.geometry("600x600")


options = ['stone','paper','scissor']



player1 = Label(root,text = "select an option ",font = ('Calibri(Body)',13,'bold'))
player1.place(x=50,y = 150)
vari = StringVar()
vari.set(options[0])
p_selection = OptionMenu(root,vari,*options)
p_selection.place(x = 250,y = 150)


playy = Button(root,text = "Play",width = 7,font = ("Calibri(Body)",13,'bold'),command = play)
playy.place(x = 300,y = 200)











root.mainloop()
