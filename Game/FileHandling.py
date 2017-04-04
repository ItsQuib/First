from random import randint
from time import sleep
import csv
def clearScreen():
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

class player(object):
  def __init__(self, name, hp, att, defe, level):
    self.name = name
    self.hp = hp
    self.att = att
    self.defence = defe
    self.level = level
  def info(self):
    print("Name: " + self.name)
    print("Health: " + str(self.hp))
    print("Attack: " + str(self.att))
    print("Defence: " + str(self.defence))
    print("Level: " + str(self.level) + "\n")
  def retatt(self):
    return self.att
  def retdef(self):
    return self.defence
  def retname(self):
    return self.name
  def rethp(self):
    return self.hp
  def levelup(self, level):
      self.level = self.level + level
#      num = 1 + (self.level / 1000)
#      self.hp = self.hp * num
#      self.att = self.att * num
#      self.defence = self.defence * num
  def retxp(self):
    return self.level
  def updatehp(self, hp):
    self.hp = hp
  def fixhp(self):
    self.hp = int(self.hp)


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




def ReadOptions():
    ml = []
    optl = {}
    try:
        with open("options.txt", "r") as a:
            optl['opt1'] = a.readline()[9:].strip()
            optl['ng'] = a.readline()[10:].strip()
            optl['cordx'] = int(a.readline()[16:].strip())
            optl['cordy'] = int(a.readline()[16:].strip())
      #      print(opt1)
      #      print(ng)
      #      print(cordx)
      #      print(cordy)
            if(optl['opt1'] == "0"):
                with open("map.csv", "r", newline="") as f:
                    if(1 == 1):
                        reader = csv.reader(f)
                        for row, i in zip(reader, range(0,100)):
                            ml.append([])
                            for thing, z in zip(row, range(0,100)):
                                if(thing != ""):
                                    ml[i].append([])
                                    ml[i][z].append(thing[2])
                                    ml[i][z].append(int(thing[6]))
                                else:
                                    break
            return ml, optl
            if(optl['opt1'] == "1"):
                optl['cordx'] = randint(0,8)
                optl['cordy'] = randint(0,8)
                optl['ng'] = 0
                optl['opt1'] = 0
                for i in range(0, 9):
                    ml.append([])
                    for o in range(0, 9):
                        r = None
                        r = randint(1,6)
                        ml[i].append([])
                        ml[i][o].append("q")
                        ml[i][o].append(r)
                ml[optl['cordy']][optl['cordx']][0] = "x"

                with open("options.txt", "w") as aa:
                    f.write("New Map: 0\n")
                    f.write("New Game: 0\n")
                    f.write("Starting Cord X: " + optl['cordx'] + "\n")
                    f.write("STarting Cord Y: " + optl['cordy'] + "\n")
                with open("map.csv", "w", newline="") as f:
                    if(1 == 1):
                        writer = csv.writer(f)
                        for row, i in zip(ml, range(0,len(ml))):
                            writer.writerow(ml[i])
                return ml, optl
    except FileNotFoundError:
        optl['cordx'] = randint(0,8)
        optl['cordy'] = randint(0,8)
        optl['ng'] = 0
        optl['opt1'] = 0
        for i in range(0, 9):
            ml.append([])
            for o in range(0, 9):
                r = None
                r = randint(1,6)
                ml[i].append([])
                ml[i][o].append("q")
                ml[i][o].append(r)
        ml[optl['cordy']][optl['cordx']][0] = "x"

        with open("options.txt", "w") as f:
            f.write("New Map: 0\n")
            f.write("New Game: 0\n")
            f.write("Starting Cord X: " + str(optl['cordx']) + "\n")
            f.write("STarting Cord Y: " + str(optl['cordy']) + "\n")
        with open("map.csv", "w", newline="") as f:
            if(1 == 1):
                writer = csv.writer(f)
                for row, i in zip(ml, range(0,len(ml))):
                    writer.writerow(ml[i])
        return ml, optl

#############
#Player File#
#############
def ReadPlayer():
    pll = {}
    try:
        with open("player.txt", "r") as a:
            pll['player1'] = a.readline()[11:].strip()
            pll['playername'] = a.readline()[12:].strip()
            pll['playerhp'] = a.readline()[10:].strip()
            pll['playerlevel'] = a.readline()[14:].strip()
     #      print(playerhp)
     #      print(playerlevel)
            if(pll['player1'] == "1"):
                user2 = player(pll['playername'], int(pll['playerhp']), 10, 10, int(pll['playerlevel']))
            if(pll['player1'] == "2"):
                user2 = player(pll['playername'], int(pll['playerhp']), 5, 10, int(pll['playerlevel']))
            if(pll['player1'] == "3"):
                user2 = player(pll['playername'], int(pll['playerhp']), 5, 5, int(pll['playerlevel']))
            return pll, user2
    except FileNotFoundError:
        pll, user2 = Tutorial()
        return pll, user2
################
#Inventory File#
################
#with open("inventory.csv", "r") as f:
#    r = csv.reader(f)

def updatePlayer(player, name, hp, xp):
  with open("player.txt", "w") as f:
    f.write("Player ID: " + str(player) + "\n")
    f.write("Playername: " + str(name) + "\n")
    f.write("Player HP: " + str(hp) + "\n")
    f.write("Player Level: " + str(xp) + "\n")

def updateMap(ml):
  with open("map.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for row, i in zip(ml, range(0,len(ml))):
      writer.writerow(ml[i])

m, opt = ReadOptions()
