import random
from tkinter import *
from tkinter import messagebox

def play():
    score1 = 0
    score2 = 0
    
    while score1 < 5 and score2 < 5:
        Label(root,text = "your choice").place(x=100,y=200)
        player1 = Entry(root,bd = 5)
        player1.place(x =300,y = 100)
        player1 = player1.get()
        lisst1 = ["stone","paper","scissor"]
        player2 = random.choice(lisst1)

        if player1 == 'stone' and player2 == 'paper':
            score2 += 1
            print(player2)
        elif player1 == 'scissor' and player2 == 'stone':
            score2 += 1
            print(player2)
        elif player1 == 'paper' and player2 == 'scissor':
            score2 += 1
            print(player2)
        else:
            score1 +=1
    print(player1)
    print(score1,score2)
root = Tk()
root.title("game")
root.geometry("600x600")
Button(root,text = "play",command = play,height = 4,width = 12).place(x = 200,y = 350)




root.mainloop()


