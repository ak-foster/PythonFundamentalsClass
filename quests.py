# Description: Contains all quests for game, meant to be imported by class_game.py

# -- plot progression or player advancement -- #


# Given a question, return yes or no answer from user
def ask_yn(question):
    answer = input(f'{question} (yes or no): ').strip()
    return answer.lower()  # TODO: enforce yes or no responses, don't return any user string


# Quest - Player dies every time, unless they have a carrot in inventory
def certain_demise(p1):
    print(f"A killer bunny attacks {p1.name}!")   # using an f string is an easy way to print variables
    if 'carrot' not in p1.inventory:
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
        p1.inventory.remove('carrot')


# Quest - Player translates words and receives loot if successful
def translate_quest(p1):
    loot = ['gold', 'water']
    words = 'Zkalet meh jonpass.'
    print(f'The guard says, "{words}"')
    # Use words to make a string that says 'let me PASS' by using only slicing and string methods we've covered
    answer = words[3:9] + words[10] + words[-5:-1].upper()
    user_yn = ask_yn('The guard is speaking another language.  Would you like to respond in that language?')
    # If successful, notify user and award with new items for inventory
    if answer == 'let me PASS' and user_yn == 'yes':
        if 'note' in p1.inventory:  # if the character has completed helpful_tip quest, they have a note
            print(f'{p1.name} says, "It is a nice blue sky day...wont you {answer}?" The guard nods and moves aside.')
            print(f'While walking past, the guard hands {p1.name} a backpack.')
            loot += ['crossbow', 'medical kit']  # bonus loot for having the note, adds to loot normally awarded
        else:
            print(f'{p1.name} says, "Please {answer} and walks past the guard."')
        p1.inventory += loot
        print('Quest complete. Check your inventory for new loot!')
    else:
        print(f'{p1.name} says nothing and attempts to walk past the guard.  The guard pushes {p1.name} off the bridge.')
        p1.lives -= 1
        print(f'{p1.name} has perished.  {p1.lives} lives remain.')


# Quest - Player fights boss and receives a carrot and a note if successful
def boss_fight(p1, monster):
    print(f'{p1.name} encounters {monster.name} and prepares to battle.')
    user_yn = ask_yn('Would you like to fight?')
    if user_yn == 'yes':
        print(f'An epic battle ensues. {p1.name} misses with his first strike, {monster.name} strikes for 50 damage.')
        p1.health -= 50
        print(f'{monster.name} lunges to strike again, but {p1.name} parries and attacks, delivering a death blow.')
        monster.die(monster)
        p1.inventory += ['carrot']
        print(f'{p1.name} wins the battle, but lost health in the process.  {p1.name} slowly walks away, limping.')
        helpful_tip(p1)
    else:
        print(f'{p1.name} runs away and lives to fight another day.')


# Quest - Player receives a note containing helpful tip
def helpful_tip(p1):
    print('A stranger hands you a note that reads-- secret pass phrase at the bridge '
          'is "blue sky". Say it to the guard to earn extra loot.')
    loot = ['note']
    if 'note' not in p1.inventory:
        p1.inventory += loot

