#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 17:59:07 2021

@author: luis
"""

from os import system
class Player:
    
    def __init__(self, name):
        self.name = name 
        self.cheap = [] 
        
    def __str__(self):
        return self.name + ' cheap:\n' + str(len(self.cheap))
    
    
def create_players():
    players = {}
    name = input('Name of Player 1: ')
    players['player1'] = Player(name)
    name = input('Name of Player 2: ')
    players['player2'] = Player(name)
    system('clear')
    print('jogadores criados:\n')
    return players


players = create_players()
for p in players:
    print(players[p])
    