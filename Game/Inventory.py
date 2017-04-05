import InventoryFileHandling
from time import sleep
from Classes import itemClass
from utils import clearScreen

#itemBackpack is to store all the items that the user owns (Is in their inventory)
itemBackpack = []
#equipednums is for storing all the ---
equipednums = []
#activeBackpack is for storing all the items that the user has equiped.
activeBackpack = {"Armour":{"Helmet":"None", "Chest":"None", "Legs":"None", "Shoes":"None"}, "Weapon":"None", "Charm":"None"}

#The two functions responsible for reading the items. They are stored in lists called "itemInventory" and "equipedItemInventory"
itemInventory, errorBool = InventoryFileHandling.ReadItems()
equipedItemInventory = InventoryFileHandling.ReadEquiped()
#If there is an error reading the items, the ReadItems function will return an empty list and a boolean value
#of True which is stored in errorbool, this checks if the bool was True. If so, it will tell the user.
if(errorBool == True):
    print("ERROR IN READING INVENTORY ITEMS")
#Otherwise, it will make a class object for the item and append it to the itemBackpack.
#Look at InventoryFileHandling to see how it reads the data and returns it.
else:
    for i in itemInventory:
        #The InventoryFileHandling file returns the data in a list. To visualise the list that's being returned,
        #it would look something like this, but with one for every item in the player's inventory:
        #[(ItemID, ItemName, ItemDesc, ItemType, Attack, Defence, ArmourType)]
        itemBackpack.append(itemClass(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
try:
    with open("equiped.txt", "r") as f:
        while True:
            try:
                line = f.readline().strip("\n")
                if(line != ""):
                    equipednums.append(line)
                else:
                    break
            except IndexError:
                break
except FileNotFoundError:
    with open("equiped.txt", "w") as f:
        rip = True
for i in equipednums:
    for a in itemBackpack:
        if(a.retid() == int(i)):
            if(a.rettype() == "Armour"):
                if(a.retat() == "Helmet"):
                    activeBackpack["Armour"]["Helmet"] = a
                if(a.retat() == "Chest"):
                    activeBackpack["Armour"]["Chest"] = a
                if(a.retat() == "Legs"):
                    activeBackpack["Armour"]["Legs"] = a
                if(a.retat() == "Shoes"):
                    activeBackpack["Armour"]["Shoes"] = a
            if(a.rettype() == "Weapon"):
                activeBackpack["Weapon"] = a

tempBackpack = {}

def SaveInventory():
    ids = []
    items = []
    for i in activeBackpack:
        if(i != "Armour"):
            if(activeBackpack[i] != "None"):
                ids.append(activeBackpack[i].retid())
        else:
            for a in activeBackpack[i]:
                if(activeBackpack[i][a] != "None"):
                    ids.append(activeBackpack[i][a].retid())
    for i in itemBackpack:
        items.append(i.retid())
    with open("inv.txt", "w") as f:
        for i in items: 
            f.write(str(i) + "\n")
    with open("equiped.txt", "w") as f:
        for i in ids:
            f.write(str(i) + "\n")

def equipMenu():
    print("Equiped Items:\n")
    for key in activeBackpack:
        print(key + ":")
        if(activeBackpack[key] != "None"):
            try:
                if(len(activeBackpack[key].keys()) == 4):
                    if(activeBackpack[key]["Helmet"] != "None"):
                        print("Helmet: " + activeBackpack[key]["Helmet"].retname())
                    else:
                        print("Helmet: " + activeBackpack[key]["Helmet"])
                    if(activeBackpack[key]["Chest"] != "None"):
                        print("Chest: " + activeBackpack[key]["Chest"].retname())
                    else:
                        print("Chest: " + activeBackpack[key]["Chest"])
                    if(activeBackpack[key]["Legs"] != "None"):
                        print("Legs: " + activeBackpack[key]["Legs"].retname())
                    else:
                        print("Legs: " + activeBackpack[key]["Legs"])
                    if(activeBackpack[key]["Shoes"] != "None"):
                        print("Shoes: " + activeBackpack[key]["Shoes"].retname() + "\n")
                    else:
                        print("Shoes: " + activeBackpack[key]["Shoes"] + "\n")
                else:
                    print(activeBackpack[key].retname() + "\n")
            except AttributeError:
                print(activeBackpack[key].retname() + "\n")
        else:
            print(activeBackpack[key] + "\n")
    while True:
        try:
            i1 = input("Do you want to equip anything?\n1. Yes\n2. No\n")
            if(i1 == "save"):
                i = 0
                SaveInventory()
            clearScreen()
            if(i1 == "1"):
                i = input("What do you want to equip?\n1. Armour\n2. Weapons\n3. Charms\n")#3. Food\n4. Charms\n")
                clearScreen()
            elif(i1 == "2"):
                i = 0
                break
            else:
                print("Please enter a valid number.")
                sleep(1)
            break
        except ValueError:
            print("Please enter a valid numebr.")
            break
        ###########################
        #Start of Armour Selection#
        ###########################
    if(i == "1"):
        tempBackpack.clear()
        bool1 = True
        while bool1 == True:
            a = None
            a = 1
            print("Equiped Armour:")
            if(activeBackpack["Armour"]["Helmet"] != "None"):
                print("Helmet: " + activeBackpack["Armour"]["Helmet"].retname())
            else:
                print("Helmet: " + activeBackpack["Armour"]["Helmet"])
            if(activeBackpack["Armour"]["Chest"] != "None"):
                print("Chest: " + activeBackpack["Armour"]["Chest"].retname())
            else:
                print("Chest: " + activeBackpack["Armour"]["Chest"])
            if(activeBackpack["Armour"]["Legs"] != "None"):
                print("Legs: " + activeBackpack["Armour"]["Legs"].retname())
            else:
                print("Legs: " + activeBackpack["Armour"]["Legs"])
            if(activeBackpack["Armour"]["Shoes"] != "None"):
                print("Shoes: " + activeBackpack["Armour"]["Shoes"].retname() + "\n")
            else:
                print("Shoes: " + activeBackpack["Armour"]["Shoes"] + "\n")
            for key in range(0, len(itemBackpack)):
                if(itemBackpack[key].rettype() == "Armour"):
                    tempBackpack[a] = itemBackpack[key]
                    print("Item --" + str(a) + "--")
                    itemBackpack[key].info()
                    a = a + 1
            cbool1 = True
            while cbool1 == True:
                try:
                    c = int(input("Type the item number of the item you wish to equip:\n"))
                except ValueError:
                    print("Not a valid item number. Please pick again")
                else:
                    if((int(c) >= a) or (int(c) <= 0)):
                        print("Not a valid item number. Please pick again.")
                    else:
                        cbool1 = False
            clearScreen()
            ifbool1 = True
            art = tempBackpack[int(c)].retat()
            while ifbool1 == True:
                b = input("You wish to equip " + tempBackpack[int(c)].retname() + "\n1.  Correct\n2. No, I want to go back\n")
                if(b == "1"):
                    ifbool1 = False
                    bool1 = False
                    activeBackpack["Armour"][art] = tempBackpack[int(c)]
                    print(tempBackpack[int(c)].retname() + " Equiped")
                if(b == "2"):
                    print("Returning to item equip menu...")
                    sleep(1)
                    clearScreen()
                    ifbool1 = False
    ###########################
    #Start Of Weapon Selection#
    ###########################
    if(i == "2"):
        tempBackpack.clear()
        bool1 = True
        while bool1 == True:
            a = None
            a = 1
            if(activeBackpack["Weapon"] != "None"):
                print("Equiped weapon: " + activeBackpack["Weapon"].retname() + "\n")
            else:
                print("Equiped weapon: " + activeBackpack["Weapon"] + "\n")
            for key in range(0, len(itemBackpack)):
                if(itemBackpack[key].rettype() == "Weapon"):
                    tempBackpack[a] = itemBackpack[key]
                    print("Item --" + str(a) + "--")
                    itemBackpack[key].info()
                    a = a + 1
            cbool1 = True
            while cbool1 == True:
                try:
                    c = int(input("Type the item number of the item you wish to equip:\n"))
                except ValueError:
                    print("Not a valid item number. Please pick again")
                else:
                    if((int(c) >= a) or (int(c) <= 0)):
                        print("Not a valid item number. Please pick again.")
                    else:
                        cbool1 = False
            clearScreen()
            ifbool1 = True
            while ifbool1 == True:
                b = input("You wish to equip " + tempBackpack[int(c)].retname() + "\n1.  Correct\n2. No, I want to go back\n")
                if(b == "1"):
                    ifbool1 = False
                    bool1 = False
                    activeBackpack["Weapon"] = tempBackpack[int(c)]
                    print(tempBackpack[int(c)].retname() + " Equiped")
                if(b == "2"):
                    print("Returning to item equip menu...")
                    sleep(1)
                    clearScreen()
                    ifbool1 = False
    ##########################
    #Start Of Charm Selection#
    ##########################
    if(i == "3"):
        tempBackpack.clear()
        bool1 = True
        while bool1 == True:
            a = None
            a = 1
            if(activeBackpack["Charm"] != "None"):
                print("Equiped Charm: " + activeBackpack["Charm"].retname() + "\n")
            else:
                print("Equiped Charm: " + activeBackpack["Charm"] + "\n")
                for key in range(0, len(itemBackpack)):
                    if(itemBackpack[key].rettype() == "Charm"):
                        tempBackpack[a] = itemBackpack[key]
                        print("Item --" + str(a) + "--")
                        itemBackpack[key].info()
                        a = a + 1
            cbool1 = True
            while cbool1 == True:
                try:
                    c = int(input("Type the item number of the item you wish to equip:\n"))
                except ValueError:
                    print("Not a valid item number. Please pick again")
                else:
                    if((int(c) >= a) or (int(c) <= 0)):
                        print("Not a valid item number. Please pick again.")
                    else:
                        cbool1 = False
            clearScreen()
            ifbool1 = True
            while ifbool1 == True:
                b = input("You wish to equip " + tempBackpack[int(c)].retname() + "\n1.  Correct\n2. No, I want to go back\n")
                if(b == "1"):
                    ifbool1 = False
                    bool1 = False
                    activeBackpack["Charm"] = tempBackpack[int(c)]
                    print(tempBackpack[int(c)].retname() + " Equiped")
                if(b == "2"):
                    print("Returning to item equip menu...")
                    sleep(1)
                    clearScreen()
                    ifbool1 = False

def showInventory():
    clearScreen()
    for key in itemBackpack:

        print(key.rettype() + ":")
        if(key != "None"):
            print(key.retname() + "\n")
        else:
            print(key + "\n")
    i = input("Press Enter To Continue\n")
    clearScreen()

def returnItems():
    return allItems
