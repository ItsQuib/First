import glob
import sqlite3
from random import randint
from time import sleep
def clearScreen():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
path = "H:\Year 12 (Again)\Game\Items\Random\*.txt"
itemid = 0
with sqlite3.connect("items.db") as db:
    c = db.cursor()
    try:
        c.execute("""
            CREATE TABLE Items(
            ItemID integer,
            ItemName string,
            ItemDesc string,
            ItemType string,
            Attack integer,
            Defence integer,
            ArmourType string,
            Primary Key(ItemID));""")
    except sqlite3.OperationalError:
        randomassvariable = True
    c.execute("""SELECT * FROM Items""")
    d = c.fetchall()
    for i in d:
#        print(i)
        itemid += 1
#        print(itemid)
files = glob.glob(path)
adjectives = []
nouns = []
for f in files:
    with open(f, "r") as file:
        line = file.readline().strip()
        if(line == "---Adjectives---"):
            for line in file:
                adjectives.append(line.strip())
        if(line == "---Nouns---"):
            for line in file:
                nouns.append(line.strip())

def RandomItem():
    item = ""
    r1 = randint(0, (len(adjectives) - 1))
    r2 = randint(0, (len(nouns) - 1))
    if(adjectives[r1][0] in ["A", "E", "I", "O", "U"]):
        item = item + "An "
    else:
        item = item + "A "
    item = item + adjectives[r1] + " "
    item = item + nouns[r2]
    print(item)

#for i in range(0, 100):
#    RandomItem()

def AddItem():
    global itemid
    name = str(input("Name: "))
    desc = str(input("Description: "))
    itemtype = str(input("ItemType (Weapon, Armour): "))
    attack = int(input("Attack (0 If Armour): "))
    defe = int(input("Defence (0 If Weapon): "))
    armourtype = str(input("ArmourType (Helmet, Chest, Legs, Boots, (None if Weapon)): "))
    with sqlite3.connect("items.db") as db:
        c = db.cursor()
        c.execute("""INSERT INTO Items (ItemID, ItemName, ItemDesc, ItemType, Attack, Defence, ArmourType)
VALUES ('""" + str(itemid) + """','""" + name + """','""" + desc + """','""" + itemtype + """','""" + str(attack) + """','""" + str(defe) + """','""" + armourtype + """');""")
        db.commit()
    print("Item Added")
    itemid += 1
    sleep(0.5)
    clearScreen()

def ReadAllItems():
    with sqlite3.connect("items.db") as db:
        c = db.cursor()
        c.execute("""SELECT * FROM Items""")
        d = c.fetchall()
        return d

def ReadItems():
    items = []
    activeitemchars = []
    activeitems = []
    with sqlite3.connect("items.db") as db:
        c = db.cursor()
        c.execute("""SELECT * FROM Items""")
        d = c.fetchall()
        items.append(d)
    try:
        with open("inv.txt", "r") as f:
            while True:
                line = f.readline().strip("\n")
                if(line != ""):
                    try:
                        activeitemchars.append(line)
                    except IndexError:
        #                print("END OF ACTIVE FILE")
                        break
                else:
                    break
    except FileNotFoundError:
        with open("inv.txt", "w") as f:
            rip = True
    try:
        for i in activeitemchars:
            activeitems.append(items[0][int(i)])
        return activeitems, False
    except IndexError:
        print("ERROR: Invalid ItemID in Inventory File.")
        return activeitems, True

def ReadEquiped():
    items = []
    equipeditems = []
    with sqlite3.connect("items.db") as db:
        c = db.cursor()
        c.execute("""SELECT * FROM Items""")
        d = c.fetchall()
        items.append(d)
    try:
        with open("equiped.txt", "r") as f:
            while True:
                line = f.readline().strip("\n")
                if(line != ""):
                    try:
                        equipeditems.append(items[0][int(line)])
                    except IndexError:
                        break
                else:
                    break
    except FileNotFoundError:
        rip = True
    return equipeditems

ReadEquiped()

def SaveItems(inv, equiped):
    ids = []
    for i in equiped:
        if(i == "Armour"):
            for a in i:
                ids.append(i[a])
        else:
            ids.append(equiped[i])


#ReadItems()
#AddItem()
#ReadItems()
with sqlite3.connect("items.db") as db:
    c = db.cursor()
#    c.execute("""DELETE FROM Items WHERE ItemID = 8""")
#    c.execute("""SELECT * FROM Items""")
#    d = c.fetchall()
#    print(d)

#for i in ReadAllItems():
#    print(i)



#for i in range(0, 10):
#    AddItem()
