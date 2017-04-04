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
