# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 13:23:24 2018

@author: takyon
"""
print("Welcome to a game of Rock, Paper, Scissors")
score_player1=0
score_player2=0

while True:
    print("             Score         ") 
    print("    Player1-{0}  :  Plaeyer2-{1}".format(score_player1,score_player2))
    player1=input("Player 1, please write a r for a rock, s for a scissors and p for paper: ")
    player2=input("Player 2, please write a r for a rock, s for a scissors and p for paper: ")
    
    RPS_dict={'r':1,'s':2,'p':3}
    p1=RPS_dict.get(player1)
    p2=RPS_dict.get(player2)
    ans=p1-p2

    if ans in [-1,2]:
        score_player1+=1
        print ("Player1 won!")
        resume=input("Do you want to play another one? press n for a new game, press any other key to quit")
        if resume == 'n':
            continue
        else:
            break
    elif ans in [1,-2]:
        score_player2+=1
        print ("Player2 won!")
        resume=input("Do you want to play another one? press n for a new game, press any other key to quit")
        if resume == 'n':
            continue
        else:
            break
    else:
        print ("Tie.Play again")
        