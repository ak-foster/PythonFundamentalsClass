# Desc - Computer game
# Dev - ak-foster
# change log

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
xp = 0

# Create inventory that is empty
inventory = ()


# -- game functionality -- #

# Ask user new character name
def get_name():
    # Name the player, ask user
    change_name = input('Please name your character: ')
    return change_name


def level():
    level = xp / 50
    return level


# Print out the player stats
def player_stats():
    print('=' * 30)
    print('Game Status')
    print('Welcome, ', character, title, 'your on', world)
    print('Level: \t', level())
    print('Vitality: \t', lives, 'lives and', health, 'health')
    print('=' * 30)


def inventory_items():
    print(f'You have {len(inventory)} items in your inventory.  They are:')
    for items in inventory:
        print(items)


# -- plot progression or player advancement -- #

# Quest 1 - Player dies every time
def certain_demise():
    global health
    global lives # it's bad practice to use global, when we learn more we'll fix this TODO: fix global
    while health > 0:
        print("Oh no, your character is hurt!")
        health = health - 20
        # users cannot take action, trolling until health is zero
        print("Do something quick! Their health is: ", health)
    print(character, "has perished.")
    lives -= 1  # player looses a life
    health = 100  # new life replenishes health
    print(f'You have {health} health {lives} lives remaining.')  # using an f string to print player stats


def helpful_tip():
    print('A stranger tells you the pass phrase at the bridge is "blue sky". Say it to the guard.')


# --- User I/O --- #
# Keep playing game while lives are left
while lives > 0:
    response = int(input("""
    To select an option from the menu, enter the number:

    - 1 - Rename your character
    - 2 - Show player stats
    - 3 - Show items in inventory
    - 4 - Deadly quest
    - 5 - Translate quest
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
        certain_demise()
    elif response == 5:
        words = 'Zkalet meh jonpass'
        print(f'The gatekeeper says {words}')
        # Use words to make a string that says 'let me PASS' by using only slicing and string methods we've covered
        print('')
        answer = words[3:9] + words[10] + words[-4:].upper()
        # If successful, notify user and award with new items for inventory
        if answer == 'let me PASS':
            print('Congrats you win!')
            loot = ('gold', 'armor')
            inventory += loot
    elif response == 0:
        helpful_tip()
        exit()
    else:
        print('Wrong input. Try again.')  # if the user enters anything unexpected, start over and ask for input


# Outside the loop which means no lives are left.
print(f'GAME OVER. {character} is no more.')

