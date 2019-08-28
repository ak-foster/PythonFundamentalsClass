# Description - Computer game
# Dev - jk-morris

# -- create game variables and npc data  -- #

from pprint import pprint as prnt

class Npc(object):
    
    __Coins = 10
    __NpcCount = 0
    
    @staticmethod
    def greetings():
        print("Can't wait to count out your coin") # Credit to Skyrim
        
    def __init__(self, name = ''):
        self.__name = name
        Npc.__SetCoins()
        Npc.__SetNpcCount() 
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    def SetNpcName(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def GetCoins():
        return Npc.__Coins
            
    @staticmethod
    def __SetCoins():
        Npc.__Coins += 3
        
    @staticmethod
    def __SetNpcCount():
        Npc.__NpcCount += 1
        