#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 17:20:39 2021

@author: luis
"""



#Object Card 
class Card:
    
    def __init__(self, rank, suite, power):
        self.rank = rank
        self.suite = suite
        self.power = power
        
    def __str__(self):
        return self.rank +" of "+ self.suite
        
    

# CREATE Dictionary of Cards
def create_cards():
    cards = {}
    SUITE = 'H D S C'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    POWER = '0 1 2 3 4 5 6 7 8 9 10 11 12'.split()
    
    for s in SUITE:
        for c in range(len(RANKS)):
            cards[str(RANKS[c])+" of "+str(s)] = Card(RANKS[c], s, POWER[c])
    
    return cards




            
    