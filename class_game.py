# Description - Computer game
# Dev - ak-foster, jk-morris

# -- create game variables and player data  -- #
# Name the game
# title = 'The Game of Choice'
title = 'The Greatest Game Ever to be Gamed'

import pickle

from pprint import pprint as prnt

# Create 'blue print' for players by making a class that starts each new player with the same name, stats, and motto
class Player(object):
    # name = 'Merv'
    # lives = 3
    # health = 100
    inventory = []
    # character_xp = 0
    __level = 1

    def __init__(self, name = 'Merv', lives = 3, health = 100, character_xp = 0):
        self.__name = name
        self.__lives = lives
        self.__health = health
        self.__character_xp = character_xp
        Player.__level_up()
    
    @property # (accessor)
    def name(self):
        return self.__name
    
    @name.setter # (mutator)
    def name(self, new_name):
        new_name = input('Please name your character: ')
        self.__name = new_name
        print(f'Name updated to: {new_name}')

    @staticmethod
    def motto():
        prnt('We all make choices in life, but in the end our choices make us.')  # credit: Andrew Ryan, Bioshock

    # Player levels up
    @staticmethod
    def __level_up():
        Player.__level += 1
    
    # Given player xp, return their level
    def level(whatever):  # name a function parameter whatever you want, just use the same name in your function
        your_level = whatever // 50  # using // to get the floor aka rounding down after dividing
        return your_level

    # Display player inventory
    def inventory_items():
        print(f'You have {len(p1.inventory)} items in your inventory.')  # single quote works with f strings too
        if len(p1.inventory) > 0:
            print("The items in inventory are:")  # double quotes also work with strings
            for item in p1.inventory:  # looping through each position (item) in the sequence (inventory)
                print(item)

# Create Child class from Parent class
class NPC(Player):
    # Class for NPC information
    __Coins = 10
    # __NpcCount = 0
    
    @staticmethod
    def greetings():
        prnt("Can't wait to count out your coin") # Credit to Skyrim
        
    def __init__(self, name = ''):
        self.__name = name
        NPC.__SetCoins()
        # NPC.__SetNpcCount() 
    
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
        return NPC.__Coins
            
    @staticmethod
    def __SetCoins():
        NPC.__Coins += 3
        
    # @staticmethod
    # # def __SetNpcCount():
    # #     NPC.__NPCCount += 1    
    
# Create NPC
NPC1 = NPC('Appleseed')

# print(NPC1.name)

# Create player 1
p1 = Player('Chuano')
# Create player 2
p2 = Player('Marley', lives=2, health=150)

# print(p1.name)
# print(p2.name)

# -- game functionality -- #


# -- plot progression or player advancement -- #

# Quest - Player dies every time, unless they have a carrot in inventory
def certain_demise():
    print(f"A killer bunny attacks {p1.name}!")   # an f string is another way to print variables
    if 'carrot' not in p1.inventory_items:
        while p1.health > 0:
            print(f"{p1.name}'s health is: {p1.health}")
            p1.health = p1.health - 40
            print(f"Oh no, {p1.name} is hurt and the rabbit is still attacking...do something quick!")
        print(p1.name, "has perished.")
        p1.lives -= 1  # player looses a life
        p1.health = 100  # new life replenishes health
        print(f"{p1.lives} lives remain.")
    else:
        print(f"{p1.name} pulls out a carrot and tosses it toward the hungry bunny, sparing {p1.name}'s life.")
        p1.inventory_items.remove('carrot')


# Quest - Player translates words and receives loot if successful
def translate_quest():
    loot = ['gold', 'water']
    words = 'Zkalet meh jonpass.'
    print(f'The gatekeeper says, "{words}"')
    # Use words to make a string that says 'let me PASS' by using only slicing and string methods we've covered
    answer = words[3:9] + words[10] + words[-5:-1].upper()
    user_yn = ask_yn('The guard is speaking another language.  Would you like to respond in that language?')
    # If successful, notify user and award with new items for inventory
    if answer == 'let me PASS' and user_yn == 'yes':
        if 'note' in p1.inventory:  # if the character has completed helpful_tip quest, they have a note
            print(f'{p1.name} says, "It is a nice blue sky day...wont you {answer}?" The guard nods and moves aside.')
            print(f'While walking by the guard throws {p1.name} a backpack.')
            loot += ['crossbow', 'medical kit']  # bonus loot for having the note, adds to loot normally awarded
        else:
            print(f'{p1.name} says, "Please {answer} and walks past the guard."')
        p1.inventory += loot
        print('Quest complete. Check your inventory for new loot!')
    else:
        print(f'{p1.name} says nothing and attempts to walk past the guard.  The guard pushes {p1.name} off the bridge.')
        p1.lives -= 1
        print(f'{p1.name} has perished.  {p1.lives} lives remain.')


# Quest - Player receives a note containing helpful tip
def helpful_tip():
    print('A stranger hands you a note that reads-- secret pass phrase at the bridge '
          'is "blue sky". Say it to the guard to earn extra loot.')
    loot = ['note']
    if 'note' not in p1.inventory:
        p1.inventory += loot

# TODO: use helpful_tip() after a player completes something


# --- user I/O --- #

# Print out the player stats
def player_stats():
    print('=' * 30)
    print('  :::: Character Stats ::::\n')
    print(f'Name: \t\t\t', f'{p1.name}')
    print('Experience: \t', f'{p1.character_xp} XP')
    print('Level: \t\t\t', f'{p1.level(p1.character_xp)}')
    print('Vitality: \t\t', p1.lives, 'lives and', p1.health, 'health')
    print('Inventory: \t\t', f'{len(p1.inventory)} items')
    print('=' * 30)
    input('\nPress ENTER to return the game menu...')


# Given a question, return yes or no answer from user
def ask_yn(question):
    answer = input(f'{question} (yes or no): ').strip()
    return answer.lower()  # TODO: enforce yes or no responses, don't return any user string


# Display the menu for quests and prompt users for a selection, keep playing while lives remain
def quests_menu():
    while p1.lives > 0:
        response = int(input("""
    To select a quest from the menu, enter the number:
        - 1 - Translate
        - 2 - Certain Demise
        - 0 - To return to the game menu
        """))
        if response == 1:
            print('*' * 40)
            translate_quest()
            print('*' * 40)
        elif response == 2:
            print('*' * 40)
            certain_demise()
            print('*' * 40)
        elif response == 0:
            game_menu()
        else:
            print('Invalid input. Try again.')  # if the user enters anything unexpected, start over


# Display the game options menu and prompt for a selection, keep playing while lives remain
def game_menu():
    while p1.lives > 0:  # TODO: fix int() below that causes crash when user doesn't input a number
        response = int(input(""" 
    To select an option from the menu, enter the number:
        - 1 - Player motto
        - 2 - Player stats
        - 3 - Open inventory
        - 4 - Start a quest
        - 0 - Return to main menu
        """))
        if response == 1:
            p1.motto()
        elif response == 2:
            player_stats()
        elif response == 3:
            p1.inventory_items()
        elif response == 4:
            quests_menu()
        elif response == 0:
            main_menu()
        else:
            print('Invalid input. Try again.')  # if the user enters anything unexpected, start over


# Display options available outside the game play, prompt for selection
def main_menu():
    while True:
        print(f'Welcome to {title}')
        response = int(input("""
    To select an option from the menu, enter the number:
        - 1 - Play game
        - 2 - Change name
        - 3 - Save
        - 0 - Exit 
        """))
        if response == 1:
            game_menu()
        elif response == 2:
            prnt('Please enter a new name.')
            p1.name(input('> '))
        elif response == 3:
            pass  # TODO: create ability to save game state
        elif response == 0:
            exit()
        else:
            print('Invalid input. Please select from the menu.')


# Call main menu to prompt the user
main_menu()

# Outside the loop which means no lives are left.
print(f'GAME OVER. {p1.name} is no more.')