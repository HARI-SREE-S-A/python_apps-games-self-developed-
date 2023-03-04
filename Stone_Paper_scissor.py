import random
score1 = 0
score2 = 0
lisst1 = ["stone","paper","scissor"]
h

while score1 < 5 and score2 < 5:
    player1 = input(str(("player1 enter your choice ")))
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
        print(player2)

winner = max(score1,score2)

print("player1 ",score1,"player2 ",score2)
