# Description - Computer game
# Dev - ak-foster

# -- create game world  -- #
# Name the game
title = 'GoodGame'

# Create a character
character = 'Merv'

# Name the world, yourself
world = 'One World'

# Give the player three lives
lives = 3

# Create health
health = 100

# Define XP
character_xp = 500

# Create inventory that is empty
inventory = []


# -- game functionality -- #

# Ask user new character name
def get_name():
    change_name = input('Please name your character: ')
    return change_name


def level(whatever):
    your_level = whatever / 50
    print(your_level)


# Print out the player stats
def player_stats():
    print('=' * 30)
    print('Game Status')
    print('Welcome, ', character, title, 'your on', world)
    print('Level: \t', level())
    print('Vitality: \t', lives, 'lives and', health, 'health')
    print('=' * 30)


def inventory_items():
    print(f'You have {len(inventory)} items in your inventory.')  # single quote works with f strings too
    if len(inventory) > 0:
        print('The items in inventory are:')
        for items in inventory:
            print(items)


# -- plot progression or player advancement -- #

# Quest 1 - Player dies every time, unless they have a carrot in inventory
def certain_demise():
    global health  # it's bad practice to use global like this, when we learn more we'll fix this TODO: fix global
    global lives
    print(f"A killer bunny attacks {character}!")   # using an f string to demonstrate another way to print variables
    if 'carrot' not in inventory:
        while health > 0:
            print(f"{character}'s health is: {health}")
            health = health - 40
            print(f"Oh no, {character} is hurt and the rabbit is still attacking...do something quick!")
            # users cannot take any actions, they are not prompted TODO: create way for player to stop attack
        print(character, "has perished.")
        lives -= 1  # player looses a life
        health = 100  # new life replenishes health
        print(f"You have {health} health {lives} lives remaining.")
    else:
        print(f"{character} pulls out a carrot and tosses it toward the hungry bunny, sparing {character}'s life.")
        inventory.remove('carrot')

def translate_quest():
    global inventory # this is bad TODO: will fix
    words = 'Zkalet meh jonpass'
    print(f'The gatekeeper says {words}')
    # Use words to make a string that says 'let me PASS' by using only slicing and string methods we've covered
    print('')
    answer = words[3:9] + words[10] + words[-4:].upper()
    # If successful, notify user and award with new items for inventory
    print(f'{character} says, "{answer}!" The guard nods and moves aside to let {character} pass by.')
    if answer == 'let me PASS':
        print('Congrats you win! Check your inventory for new loot.')
        loot = ['gold', 'armor']
        inventory += loot


def helpful_tip():
    print('A stranger says the pass phrase at the bridge is "blue sky". Say it to the guard.')


def menu_quests():
    response = int(input("""
            To select an option from the menu, enter the number:

            - 1 - Translate quest
            - 2 - Certain Demise quest
            - 0 - To exit
            """))
    if response == 1:
        translate_quest()
    elif response == 2:
        certain_demise()

def menu_prompt():
    while lives > 0:
        response = int(input("""
        To select an option from the menu, enter the number:
    
        - 1 - Rename your character
        - 2 - Show player stats
        - 3 - Show items in inventory
        - 4 - Show the quests menu
        - 0 - To exit
        """))
        if response == 1:
            character = get_name()
            print('Your new name is: ', character)
        elif response == 2:
            player_stats()
        elif response == 3:
            inventory_items()
        elif response == 4:
            menu_quests()
        elif response == 0:
            helpful_tip()
            exit()
        else:
            print('Wrong input. Try again.')  # if the user enters anything unexpected, start over and ask

level(character_xp)

# --- User I/O --- #
# Keep playing game while lives are left



# Outside the loop which means no lives are left.
print(f'GAME OVER. {character} is no more.')

