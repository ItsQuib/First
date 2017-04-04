from random import randint
from time import sleep
from util import clearScreen
import csv

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
