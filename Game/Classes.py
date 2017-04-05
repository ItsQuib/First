#Used everywhere.
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
    def retxp(self):
        return self.level
    def updatehp(self, hp):
        self.hp = hp
    def fixhp(self):
        #If the player's HP becomes a decimal number, this will round it to the closest int.
        self.hp = int(self.hp)

#Used in Inventory.py
class itemClass(object):
    def __init__(self, itemid, name, desc, itemtype, att, defe, at):
        self.itemid = itemid
        self.name = name
        self.desc = desc
        self.itemtype = itemtype
        if(self.itemtype == "Armour"):
            self.defence = defe
            self.at = at
        if(self.itemtype == "Weapon"):
            self.att = att
    def info(self):
        print("Name: " + self.name)
        print("Description: " + self.desc)
        print("Type of item: " + self.itemtype)
        if(self.itemtype == "Armour"):
            print("Armour Type: " + self.at)
            print("Defence: " + str(self.defence) + "\n")
        elif(self.itemtype == "Weapon"):
            print("Attack: " + str(self.att) + "\n")
        else:
            print("")
    def retid(self):
        return self.itemid
    def rettype(self):
        return self.itemtype
    def retname(self):
        return self.name
    def retatt(self):
        return self.att
    def retat(self):
        return self.at
    def retdef(self):
        return self.defence

#Used in mobs.py
class enemy(object):
    def __init__(self, name, hp, att, defe, xpaw):
        self.name = name
        self.hp = hp
        self.att = att
        self.defence = defe
        self.xpaw = xpaw
    def info(self):
        print("--" + self.name + "--")
        print("Health: " + str(self.hp))
        print("Attack: " + str(self.att))
        print("Defence: " + str(self.defence) + "")
        print("XP Reward: " + str(self.xpaw) + "\n")
    def retatt(self):
        return self.att
    def retdef(self):
        return self.defence
    def retname(self):
        return self.name
    def rethp(self):
        return self.hp
    def retxpaw(self):
        return self.xpaw
