from random import randint
def ReadMobs():
    ml = []
    md = {}
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

    with open("Mobs.txt", "r") as f:
        for line in f:
            ml.append(line.strip())
    for entry in ml:
        with open(entry + ".txt", "r") as f:
            filename = entry
            name = f.readline()[6:].strip()
            hp = f.readline()[4:].strip()
            att = f.readline()[8:].strip()
            defe = f.readline()[9:].strip()
            xpaw = f.readline()[4:].strip()
            md[filename] = enemy(name, hp, att, defe, xpaw)
    return md

def RandomMob():
    l = []
    with open("Mobs.txt", "r") as f:
        for line in f:
            l.append(line.strip())
    r = randint(0, (len(l) - 1))
    return l[r]






