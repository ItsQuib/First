from random import randint
from time import sleep
from util import clearScreen
import sqlite3
import csv

def newMap(optionList):
    mapList = []
    for i in range(0, 9):
        mapList.append([])
        for o in range(0, 9):
            r = None
            r = randint(1,6)
            mapList[i].append([])
            mapList[i][o].append("q")
            mapList[i][o].append(r)
    mapList[optionList['coordinateY']][optionList['coordinateX']][0] = "x"
    return mapList


#A lot of this function repeats itself with writing to files.
def ReadOptions():
    #Two lists I am using to store data.
    mapList = []
    optionList = {}
    #Try statement to open the options file. Here so if the file isn't there I can
    #take care of that in the except statement.
    try:
        with open("options.txt", "r") as a:
            #This reads the first four lines, and puts them in the dictionary.
            optionList['newMap'] = a.readline()[9:].strip()
            optionList['newGame'] = a.readline()[10:].strip()
            optionList['coordinateX'] = int(a.readline()[24:].strip())
            optionList['coordinateY'] = int(a.readline()[24:].strip())
            #This block handles reading the map from the file (As the user does not want to generate a new map.)
            if(optionList['newMap'] == "0"):
                with open("map.csv", "r", newline="") as f:
                    reader = csv.reader(f)
                    for row, i in zip(reader, range(0,100)):
                        mapList.append([])
                        for thing, z in zip(row, range(0,100)):
                            if(thing != ""):
                                mapList[i].append([])
                                mapList[i][z].append(thing[2])
                                mapList[i][z].append(int(thing[6]))
                            else:
                                break
                return mapList, optionList
            #This block handles creating a map (Uses the above newMap function.) when the user wants to generate a new map.
            if(optionList['newMap'] == "1"):
                optionList['coordinateX'] = randint(0,8)
                optionList['coordinateY'] = randint(0,8)
                optionList['newMap'] = 0
                mapList = newMap(optionList)
                with open("options.txt", "w") as aa:
                    f.write("New Map: 0\n")
                    f.write("New Game: " + str(optionList["newGame"]) + "\n")
                    f.write("Starting Coordinate X: " + optionList['coordinateX'] + "\n")
                    f.write("Starting Coordinate Y: " + optionList['coordinateY'] + "\n")
                with open("map.csv", "w", newline="") as f:
                    writer = csv.writer(f)
                    for row, i in zip(mapList, range(0,len(mapList))):
                        writer.writerow(mapList[i])
                return mapList, optionList
    #Does the same as if the user wants a new map made. This is called if
    #the code looks for the file but it isn't there.
    except FileNotFoundError:
        optionList['coordinateX'] = randint(0,8)
        optionList['coordinateY'] = randint(0,8)
        optionList['newGame'] = 0
        optionList['newMap'] = 0
        mapList = newMap(optionList)
        with open("options.txt", "w") as f:
            f.write("New Map: 0\n")
            f.write("New Game: 0\n")
            f.write("Starting Coordinate X: " + str(optionList['coordinateX']) + "\n")
            f.write("Starting Coordinate Y: " + str(optionList['coordinateY']) + "\n")
        with open("map.csv", "w", newline="") as f:
            writer = csv.writer(f)
            for row, i in zip(mapList, range(0,len(mapList))):
                writer.writerow(mapList[i])
        return mapList, optionList

#############
#Player File#
#############
def ReadPlayer():
    playerList = {}
    try:
        with open("player.txt", "r") as a:
            playerList['playerType'] = a.readline()[11:].strip()
            playerList['playerName'] = a.readline()[12:].strip()
            playerList['playerHp'] = a.readline()[10:].strip()
            playerList['playerLevel'] = a.readline()[14:].strip()
            if(playerList['playerType'] == "1"):
                playerClass = player(playerList['playerName'], int(playerList['playerHp']), 10, 10, int(playerList['playerLevel']))
            if(playerList['playerType'] == "2"):
                playerClass = player(playerList['playerName'], int(playerList['playerHp']), 5, 10, int(playerList['playerLevel']))
            if(playerList['playerType'] == "3"):
                playerClass = player(playerList['playerName'], int(playerList['playerHp']), 5, 5, int(playerList['playerLevel']))
            return playerList, playerClass
    except FileNotFoundError:
        playerList, playerClass = Tutorial()
        return playerList, playerClass

################
#Inventory File#
################
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
