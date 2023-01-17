from tkinter import *
from tkinter import messagebox
import random
options = ['stone','paper','scissor']


 

def play():
    
    score1 = 0
    score2 = 0
    options = ['stone','paper','scissor']
    x =Label(root,text = "vs computer",font = ("Calibri(Body)",12,'bold')).place(x = 200,y = 250)
    if score1 or score2 <= 5 :
        player2 = random.choice(options)
        if vari.get() == "stone" and player2 == "paper":
            x = x.delete(0,'end')
            x=Label(root,text = player2,font = ("Calibri(Body)",12,'bold')).place(x = 200,y = 250)
            score2 += 1
        elif vari.get() == "paper" and player2 == "scissor":
            x = x.delete(0,'end')
            x =Label(root,text = player2,font = ("Calibri(Body)",12,'bold')).place(x = 200,y = 250)
            score2 += 1
        elif  vari.get() == "scissor" and player2 == "stone":
            x = x.delete(0,'end')
            x =Label(root,text = player2,font = ("Calibri(Body)",12,'bold')).place(x = 200,y = 250)
            score2 += 1
        elif vari.get() == player2  :
            score1 += 0
            score2 += 0
        else:
            score1+=1
    if score1 > score2:
        Label(root,text = "you won",font = ("Calibri(Body)",13,"bold")).place(x = 250,y = 300)
    else:
        Label(root,text = "you loss",font = ("Calibri(Body)",13,"bold")).place(x = 250,y = 300)
        
        
        
        
        
    
    





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
