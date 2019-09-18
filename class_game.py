# Description - Computer game
# Dev - ak-foster

import pickle
import quests

# -- create game variables and player data  -- #
# Name the game
title = 'The Game of Choice'


# Create 'blue print' for players by making a class that starts each new player with the same name, stats, and motto
class Player(object):
    total_players = 0
    inventory = []

    def __init__(self, name='Merv', lives=3, health=100, character_xp=0):
        self.name = name
        self.lives = lives
        self.health = health
        self.character_xp = character_xp
        Player.total_players += 1  # track of the number of players, adds one each time a Player object is created

    @staticmethod
    def motto():
        print('"We all make choices in life, but in the end our choices make us."')  # credit: Andrew Ryan, Bioshock


# Create Child class from Parent class
class Enemy(object):

    def __str__(self):
        return self.name

    def __init__(self, name='Fred the Monster', health=100):
        self.__name = name
        self.health = health

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def die(self, thing):
        print(f'With a dying breath {self.name} says, "Money cant buy life."')  # credit Bob Marley's last words
        del thing


# -- game functionality -- #

# Ask user new character name
def change_name():
    new_name = input('Please name your character: ')  # single or double quotes work with strings
    p1.name = new_name
    print(f'Name updated to: {p1.name}')  # single or double quotes also work with f strings,


# Given player xp, return their level
def level(whatever):  # name a function parameter whatever you want, just use the same name in your function
    your_level = whatever // 50  # using // to get the floor aka rounding down after dividing
    return your_level


# Display player inventory
def inventory_items():
    print(f'You have {len(p1.inventory)} items in your inventory.')
    if len(p1.inventory) > 0:
        print("The items in inventory are:")
        for item in p1.inventory:  # looping through each position (item) in the sequence (inventory)
            print(item)


# Save game
def save_progress(player):
    save_file = open('player.dat', 'wb+')
    pickle.dump(player, save_file)
    save_file.close()
    print(f'Progress for {player.name} has been saved.')


# Load game
def load_progress():
    save_file = open('player.dat', 'rb+')
    return pickle.load(save_file)


# --- user I/O --- #

# Print out the player stats
def player_stats():
    print('=' * 30)
    print('  :::: Character Stats ::::\n')
    print(f'Name: \t\t\t', f'{p1.name}')
    print('Experience: \t', f'{p1.character_xp} XP')
    print('Level: \t\t\t', f'{level(p1.character_xp)}')
    print('Vitality: \t\t', p1.lives, 'lives and', p1.health, 'health')
    print('Inventory: \t\t', f'{len(p1.inventory)} items')
    print('=' * 30)
    input('\nPress ENTER to return the game menu...')


# Display the menu for quests and prompt users for a selection, keep playing while lives remain
def quests_menu():
    while p1.lives > 0:
        response = int(input("""
    To select a quest from the menu, enter the number:
        - 1 - Translate
        - 2 - Certain Demise
        - 3 - Boss Fight
        - 0 - Return to the game menu
        """))
        if response == 1:
            print('*' * 40)
            quests.translate_quest(p1)
            print('*' * 40)
        elif response == 2:
            print('*' * 40)
            quests.certain_demise(p1)
            print('*' * 40)
        elif response == 3:
            print('*' * 40)
            quests.boss_fight(p1, boss)
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
            inventory_items()
        elif response == 4:
            quests_menu()
        elif response == 0:
            main_menu(p1)
        else:
            print('Invalid input. Try again.')  # if the user enters anything unexpected, start over


# Display options available outside the game play, prompt for selection
def main_menu(p1):
    while p1.lives > 0:
        print(f'Welcome to {title}')
        response = int(input("""
    To select an option from the menu, enter the number:
        - 1 - Play game
        - 2 - Change name
        - 3 - Save
        - 4 - Load
        - 0 - Exit 
        """))
        if response == 1:
            game_menu()
        elif response == 2:
            change_name()
        elif response == 3:
            save_progress(p1)
        elif response == 4:
            p1 = load_progress()  # TODO: fix load game by changing scope
        elif response == 0:
            exit()
        else:
            print('Invalid input. Please select from the menu.')


# Create player 1
p1 = Player()
boss = Enemy()

# Call main menu to prompt the user
main_menu(p1)

# Outside the loop which means no lives are left.
print(f'GAME OVER. {p1.name} is no more.')

