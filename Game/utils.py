def Tutorial():
    pll = {}
    print("Starting New Game....")
    sleep(1)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWelcome to my game! To start off, please select a player")
    print("---------- Player Option 1 ----------")
    print("Attack: 10")
    print("HP: 100")
    print("Defence: 10")
    print("\n")
    print("---------- Player Option 2 ----------")
    print("Attack: 5")
    print("HP: 150")
    print("Defence: 10")
    print("\n")
    print("---------- Player Option 3 ----------")
    print("Attack: 5")
    print("HP: 250")
    print("Defence: 5")
    while True:
        try:
            i = int(input("Please pick a number (1-3):\n"))
        except ValueError:
            print("Please Enter a number. (1-3)")
        if(i == 1):
            name = input("Please Enter Your Name:\n")
            user1 = player(name, 100, 10, 10, 1)
            with open("player.txt", "w") as aa:
                f.write("Player ID: 1\n")
                f.write("Playername: " + name + "\n")
                f.write("Player HP: 100\n")
                f.write("Player Level: 1\n")
            pll['player1'] = 1
            pll['playername'] = name
            pll['playerhp'] = 100
            pll['playerlevel'] = 1
            return pll, user1
            break
            clearScreen()
        elif(i == 2):
            name = input("Please Enter Your Name:\n")
            user1 = player(name, 150, 5, 10, 1)
            with open("player.txt", "w") as aa:
                f.write("Player ID: 1\n")
                f.write("Playername: " + name + "\n")
                f.write("Player HP: 150\n")
                f.write("Player Level: 1\n")
            pll['player1'] = 2
            pll['playername'] = name
            pll['playerhp'] = 150
            pll['playerlevel'] = 1
            return pll, user1
            break
            clearScreen()
        elif(i == 3):
            name = input("Please Enter Your Name:\n")
            user1 = player(name, 250, 5, 5, 1)
            with open("player.txt", "w") as f:
                f.write("Player ID: 1\n")
                f.write("Playername: " + name + "\n")
                f.write("Player HP: 250\n")
                f.write("Player Level: 1\n")
            pll['player1'] = 3
            pll['playername'] = name
            pll['playerhp'] = 250
            pll['playerlevel'] = 1
            return pll, user1
            break
            clearScreen()
        else:
            print("Please Enter a number. (1-3)")
    print("I'll go through the basics of the game before you start.")
    print("This game is text based. Any questions you are asked will be answered")
    print('with 1, 2, 3 etc. The map is a 9 x 9 grid. Every room is different, with different')
    print('mobs and loot. Press Enter to go to the menu.')
    i = input('')
    print("\nMenu: \nThis will show your inventory.\n1. Show Inventory\nThis will let you equip items from your inventory. These can make you stronger\n2. Equip Menu\nThis will show your map, here you can go from room to room to fight monsters.\n3. Go to map\n4. Battle (alpha)\n5. Coming Soon...\n")
