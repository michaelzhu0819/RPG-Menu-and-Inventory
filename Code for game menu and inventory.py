# Python menu and inventory - text based adventure game
# Michael Zhu
# Oct 6th, 2021
# CS30
# Ms.Cotcher
""" This is the menu for a game where you are an adventurer trying to escape
a wasteland with a locked door, navigate through the biome with four
movements, encounter and defeat enemies, collect resources, and try to find
the key to the door. Now comes with two inventories, one for exploring and
one for combat, along with descriptions for potential characters and
locations in the main menu"""

""" These variables set up the catagories for actions and the coordinate
system, the nested dictionaries holding your two inventories, and the
dictionaries holding descriptions for character and location"""
x = 0
y = 0
general_action = ["explore", "combat", "characters", "locations"]
explore = ["forward", "backward", "left", "right", "inventory", "quit"]
combat = ["attack", "dodge", "defend", "inventory", "quit"]

# exploration inventory
exploring_bag = {
                 "woter bottle": {"description": "a common woter bottle",
                                  "stats": "+2 focus", "usage": "2"},
                 "first aid": {"description":
                               "a first aid kit capable of healing fatal" +
                               " wounds",
                               "stats":
                               "full heal, boost health to 8 and focus to 15",
                               "usage": "1"},
                 "monke bar": {"description": "a tasty monke bar", "stats":
                               "+4 health and +5 focus", "usage": "2"}
                }

# Combat inventory
combat_pouch = {
                "fist": {"description": "your fist",
                         "stats": "1 damage",
                         "cooldown": None},
                "pistol": {"description":
                           "a small firearm capable of piercing armor",
                           "stats": "5 damage",
                           "cooldown": "one round"},
                "knife": {"description":
                          "a dull knife that does more than your fist",
                          "stats": "2 damage",
                          "cooldown": None},
                "grenade": {"description":
                            "a high powered explosive with devastating powers",
                            "stats": "10 damage",
                            "cooldown": "1 use per fight"}
                }

# Potential characters and their descriptions
characters = {
              "beserker": "do high damge when health and/or focus is low",
              "healer": "heal themselves every 5 rounds",
              "mage": "have less cooldown on weapons and healing items",
              "tank": "have +100% health at the start of the game"
              }

# Potential locations and their descriptions
locations = {
             "loot point 1": "at (1, 0), contains a woter bottle",
             "loot point 2": "at (-2, 2), contains a first aid kit",
             "combat point 1": "at (-1, 0), need to defeat a 3 health enemy",
             "combat point 2": "at (2, -1), need to defeat a 7 health enemy",
             "boss spawn": "at either (4, 5) or (5, 4), need to defeat the" +
             " boss with higher damage and 20 health",
             "key point": "at (5, 5), contains the key that beats the game",
             "end game point": "at (0, 5), unlock it by obtaining and using" +
             " the key, which will then beat the game"
            }

""" The while loop that makes sure the general menu is running constantly until
quit is inputted, during this you can either select explore or combat"""
while True:
    print("\nyou can do the following catagory of actions:")
    for i in general_action:
        print (i)
    print("side note: you can type quit to quit anytime\n")
    cata_input = input("which one do you choose?\n")

    """ The section is what happens when you select explore, it constantly
    loops and ask for input until you type quit which will return to the
    general menu"""
    if cata_input.lower() == general_action[0]:
        while True:
            print("\nu can go either")
            for option in explore:
                print(option)
            direction_input = input("which one do you choose?\n")

            # The coordinate system
            if direction_input.lower() in explore:
                print("\n" + direction_input.lower() + "!\n")
                coord_change = direction_input.lower()
                if coord_change == explore[0]:
                    y += 1
                    print("your y value increased by one, " +
                          "your coord now is " + str(x)+" ," + str(y))
                elif coord_change == explore[1]:
                    y -= 1
                    print("your y value decreased by one, " +
                          "your coord now is " + str(x)+" ," + str(y))
                elif coord_change == explore[2]:
                    x -= 1
                    print("your x value decreased by one, " +
                          "your coord now is " + str(x) + " ," + str(y))
                elif coord_change == explore[3]:
                    x += 1
                    print("your x value increased by one, " +
                          "your coord now is " + str(x) + " ," + str(y))

                # Displays your exploration inventory
                elif direction_input.lower() == explore[4]:
                    for item in exploring_bag:
                        print(f"^{item}^:")
                        for thing in exploring_bag[item]:
                            print(f"{thing} - {exploring_bag[item][thing]}")
                        print("\n")
                elif direction_input.lower() == explore[5]:
                    print("going back to the main menu\n")
                    break
            else:
                print("invalid action!")

    # Select combat in main menu, constantly loops till quit is inputted
    elif cata_input.lower() == general_action[1]:
        while True:
            print("\nu can do either")
            for action_type in combat:
                print(action_type)
            combat_input = input("\nwhich one do you choose?\n")
            if combat_input.lower() in combat:
                print("\n" + combat_input.lower() + "!\n")

                """ Shows you all the accessories in the combat inventory and
                lets you choose one of them and use it"""
                if combat_input.lower() == combat[0]:
                    print("You have:\n")
                    for item in combat_pouch:
                        print(f"- {item}")
                    combat_input_2 = input("\nWhich one do you want to use?\n")
                    if combat_input_2.lower() in combat_pouch:
                        print(f"You used {combat_input_2.lower()}!")
                    elif combat_input_2.lower() == "quit":
                        print("returning to combat menu\n")
                        break
                    else:
                        print("invalid action!")

                # displays your combat inventory
                elif combat_input.lower() == combat[3]:
                    for item in combat_pouch:
                        print(f"^{item}^:")
                        for info in combat_pouch[item]:
                            print(f"{info}- {combat_pouch[item][info]}")
                        print("\n")

                # breaks the loop if inputted quit
                elif combat_input.lower() == combat[4]:
                    print("going back to the main menu")
                    break

            # accepts wrong inputs
            else:
                print("invalid action!")

    # prints descriptions of characters as statements if inputted characters
    elif cata_input.lower() == general_action[2]:
        print("\n")
        for item in characters:
            print(f"{item} can {characters[item]}")

    # prints descriptions of locations as statements if inputted location
    elif cata_input.lower() == general_action[3]:
        print("\n")
        for place in locations:
            print(f"{place} is {locations[place]}")

    # Breaks the loop when inputted quit and accepts wrong inputs
    elif cata_input.lower() == "quit":
        break
    else:
        print("invalid action!")
