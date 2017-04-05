from random import randint
#This reads all the mobs, makes a class object for them and puts them in a dictionary
#The dictionary is then returned.
def ReadMobs():
    mobList = []
    mobDictionary = {}
    with open("Mobs.txt", "r") as f:
        for line in f:
            mobList.append(line.strip())
    for entry in mobList:
        with open("mobs/" + entry + ".txt", "r") as f:
            filename = entry
            name = f.readline()[6:].strip()
            hp = f.readline()[4:].strip()
            att = f.readline()[8:].strip()
            defence = f.readline()[9:].strip()
            xpAward = f.readline()[4:].strip()
            mobDictionary[filename] = enemy(name, hp, att, defence, xpAward)
    return mobDictionary

#A function to find a random mob and return the mob's class object.
def RandomMob():
    mobList = []
    with open("Mobs.txt", "r") as f:
        for line in f:
            mobList.append(line.strip())
    randomNo = randint(0, (len(mobList) - 1))
    return mobList[randomNo]






