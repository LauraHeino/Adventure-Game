import time
import random
import items


def print_pause(msg):
    print(msg)
    time.sleep(1.5)


def generate_item(monster, creature, weapon, tool, id):
    if id == 'm':
        return random.choice(monster)
    elif id == 'c':
        return random.choice(creature)
    elif id == 'w':
        return random.choice(weapon)
    elif id == 't':
        return random.choice(tool)


def intro(monster, tool):
    print_pause("You find yourself standing in an open field "
                "of tall grass and not a soul nearby. \n"
                f"There's been word of an evil {random.choice(monster)} "
                "lurking nearby who has "
                "been terrifying the villagers.")
    print_pause("You see a small cozy-looking house,"
                " and next to it a cave whose entrance "
                "is covered with spiderwebs.")
    print_pause(f"You are only armed with an old {tool_x}.")
    accessories.append(tool_x)
    print_pause("")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to take a peek into the cave.")
    if get_choice() == '1':
        house(items.creature, items.weapon)
    else:
        cave(items.monster)


def valid_input(prompt, a, b, prompt2):
    while True:
        choice = input(prompt).lower()
        if choice == a:
            return choice
        elif choice == b:
            return choice
        else:
            print_pause(prompt2)
            time.sleep(1)


def get_choice():
    choice = valid_input("What would you like to do?\n",
                         '1', '2', 'Please enter 1 or 2')
    if choice == '1':
        return '1'
    else:
        return '2'


def house(creature, weapon):
    if 'amulet' in accessories:
        print_pause("You head back to the invaded house carrying your amulet.")
        print_pause("You do have a weapon, but wonder about the amulet...")
        print_pause("")
        print_pause("Enter 1 to fight the house occupant.")
        print_pause("Enter 2 to flee to the fields.")
        if get_choice() == '1':
            fight(items.weapon)
        else:
            field()
    elif 'sabertooth cat' in accessories or 'troll' in accessories:
        print_pause("You enter the house again with your new companion.")
        print_pause("Your companion proves to be of great help, "
                    "and you manage to evict the enemy together.")
        print_pause("It is a shared victory!")
        print_pause("")
        play_again()
    elif 'wizard' in accessories or 'dragon' in accessories:
        print_pause("You enter the house again with your new companion.")
        print_pause("Sadly your new friend goes rogue "
                    "and burns the house down.")
        print_pause("It is a tie.")
        print_pause("")
        play_again()
    else:
        print_pause("You knock on the door cautiously.")
        print_pause("The door opens slowly, and you are greeted "
                    f"by a {creature_x} who is not happy to see you.")
        print_pause("In the corner of the room you "
                    f"see a {weapon_x}, which you manage to grab.")
        accessories.append(weapon_x)
        print_pause("")
        print_pause("Enter 1 to fight the hostile creature.")
        print_pause("Enter 2 to back out and check the cave instead.")
        if get_choice() == '1':
            fight(items.weapon)
        else:
            cave(items.monster)
            print_pause("")


def cave(monster):
    print_pause("You slowly peek inside the cave after "
                "clearing the spider colony out of your way.")
    print_pause("The cave is dark, but you spy "
                "a mysterious looking amulet.")
    print_pause("")
    print_pause("Enter 1 to pick up the potentially dangerous item.")
    print_pause("Enter 2 to ignore the amulet.")
    if get_choice() == '1':
        accessories.append("amulet")
        print_pause("")
        print_pause("You pocket the amulet and continue into the cave.")
    else:
        print_pause("You leave the amulet and continue into the cave.")
        print_pause("")
    print_pause("You hear rustling and see something that "
                f"looks like a {monster_x}. You are horrified.")
    print_pause("However, the creature looks amicable "
                "and tells you their house has been invaded.")
    if 'Mace of Molag Bal' in accessories or 'magic wand' in accessories:
        print_pause("They can see you are in possession of a "
                    "powerful weapon and wish you good luck.")
    else:
        print_pause("They see you lack the sufficient means to "
                    "defend yourself, and offer to join forces with you.")
        accessories.append(monster_x)
    print_pause("")
    print_pause("Enter 1 to go explore the house.")
    print_pause("Enter 2 to fight the creature anyway.")
    if get_choice() == '1':
        house(items.creature, items.weapon)
    else:
        fight(items.weapon)


def fight(weapon):
    print_pause("You draw your weapon.")
    if 'amulet' in accessories:
        chance()
        play_again()
    elif ('Mace of Molag Bal' in accessories or 'sabertooth cat' in
          accessories or 'wizard' in accessories or
          'magic wand' in accessories):
        print_pause("Your extraordinary resources are "
                    "enough to defeat the opponent.")
        print_pause("You win!")
        play_again()
    else:
        print_pause("Sadly you were not able to "
                    "fend for yourself in this fight.")
        print_pause("You are defeated.")
        play_again()


def field():
    print_pause("You decide you don't have what it takes "
                "to come out of this in one piece.")
    print_pause("Therefore you make an escape back to "
                "the field unscathed but untriumphant.")
    play_again()


def chance():
    outcome = random.choice(["win", "lose"])
    if outcome == "win":
        print_pause("Congratulations! You have miraculously "
                    "emerged from this uneven battle!")
    else:
        print_pause("Unfortunately luck seems to have abandoned "
                    "you and you have lost.")


def play_again():
    print_pause("")
    accessories.clear()
    choice = valid_input("Would you like to play again? Enter y/n\n",
                         "y", "n", "Please enter y or n:").lower()
    if choice == "y":
        play_game()
    else:
        print_pause("Thank you for playing!")


def play_game():
    intro(items.monster, items.tool)


accessories = []
tool_x = generate_item(items.monster,
                       items.creature,
                       items.weapon,
                       items.tool, 't')
creature_x = generate_item(items.monster,
                           items.creature,
                           items.weapon,
                           items.tool, 'c')
weapon_x = generate_item(items.monster,
                         items.creature,
                         items.weapon,
                         items.tool, 'w')
monster_x = generate_item(items.monster,
                          items.creature,
                          items.weapon,
                          items.tool, 'm')

play_game()
