#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 18:07:33 2021

@author: luis
"""

import class_card as cc
import class_player as cp
from os import system
import random

# create cards and players

cards = cc.create_cards()

players = cp.create_players()

    
#print(cards)

# distribute cards for players 
for p in players:
    for i in range(1,27):
        
        choose = random.choice(list(cards))
        players[p].cheap.append(cards[choose])
        del cards[choose]
        
#print(players['player1'].cheap)
#print(players['player2'].cheap)
#print(cards)

# Game 

def draw_game():
    res = []

    stop = 0
    while stop != 1:
        res.append(players['player1'].cheap[0])
        res.append(players['player2'].cheap[0])
        del players['player1'].cheap[0]
        del players['player2'].cheap[0]
        res.append(players['player1'].cheap[0])
        res.append(players['player2'].cheap[0])
        del players['player1'].cheap[0]
        del players['player2'].cheap[0]
        print(players['player1'].name+" :"+str(players['player1'].cheap[0])+"("+str(players['player1'].cheap[0].power)+")")
        print(players['player2'].name+" :"+str(players['player2'].cheap[0])+"("+str(players['player2'].cheap[0].power)+")")
        
        if int(players['player1'].cheap[0].power) > int(players['player2'].cheap[0].power):
            res.append(players['player1'].cheap[0])
            res.append(players['player2'].cheap[0])
            del players['player1'].cheap[0]
            del players['player2'].cheap[0]
            for c in res:
                players['player1'].cheap.append(c) 
            stop = 1
            wr = players['player1'].name
        elif int(players['player1'].cheap[0].power) < int(players['player2'].cheap[0].power):
            res.append(players['player1'].cheap[0])
            res.append(players['player2'].cheap[0])
            del players['player1'].cheap[0]
            del players['player2'].cheap[0]
            for c in res:
                players['player2'].cheap.append(c) 
            stop = 1
            wr = players['player2'].name
        
    return wr
        
        
       
def game(r) :
    wr = ""
    system('clear')
    print("round: "+str(r))
    print(players['player1'].name+" :"+str(players['player1'].cheap[0])+"("+str(players['player1'].cheap[0].power)+")")
    print(players['player2'].name+" :"+str(players['player2'].cheap[0])+"("+str(players['player2'].cheap[0].power)+")")
    
    if int(players['player1'].cheap[0].power) > int(players['player2'].cheap[0].power):
        players['player1'].cheap.append(players['player1'].cheap[0])
        players['player1'].cheap.append(players['player2'].cheap[0])
        del players['player1'].cheap[0]
        del players['player2'].cheap[0]
        wr = players['player1'].name
        
    elif int(players['player1'].cheap[0].power) < int(players['player2'].cheap[0].power):
        players['player2'].cheap.append(players['player2'].cheap[0])
        players['player2'].cheap.append(players['player1'].cheap[0])
        del players['player1'].cheap[0]
        del players['player2'].cheap[0]
        wr = players['player2'].name
        
    else:
        wr = draw_game()    
    return wr
        


def resume(r, wr) :
    r = r + 1
    print("winner round: "+ wr)
    print("\n player1: " + str(len(players['player1'].cheap)))
    print("\n player2: " + str(len(players['player2'].cheap))) 
    return r
        
finalgame = 1 
r = 1   
while finalgame != 0:
    
    if len(players['player1'].cheap) >= 50:
        vencedor = players['player1'].name
        print("fim do jogo vendedor: "+str(vencedor))
        finalgame = 0
        
    elif len(players['player2'].cheap) >= 50:
        vencedor = players['player2'].name
        print("fim do jogo vendedor: "+str(vencedor))
        finalgame = 0
    else:
        wr = game(r)
        r = resume(r, wr)
        input("Click Enter to Continue: ")
        
    
        
