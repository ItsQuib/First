def clearScreen():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
from random import randint
from time import sleep
def battle(p, en):
    print("You engage in battle with:")
    enstuckhp = int(en.rethp())
    pstuckhp = int(p.rethp())
    en.info()
    attacker = 0
    patt = int(p.retatt())
    pdef = int(p.retdef())
    pname = p.retname()
    php = int(p.rethp())
    enatt = int(en.retatt())
    endef = int(en.retdef())
    enname = en.retname()
    enhp = int(en.rethp())
    pcrit = False
    encrit = False
    sleep(2)
    while True:
        enperc = 0
        pperc = 0
        enstr = ""
        pstr = ""
        att = None
        r = None
        if(attacker == 0):
            att = patt
            r = randint(1, 10)
            if(r == 1):
                att = att * 10
                pcrit = True
            elif(r <= 2):
                att = att * 5
            elif(r <= 5):
                att = att * 2
            enhp = enhp - att
        if(attacker == 1):
            att = enatt
            r = randint(1, 10)
            if(r == 1):
                att = att * 10
                pcrit = True
            elif(r <= 2):
                att = att * 5
            elif(r <= 5):
                att = att * 2
            php = php - att
        if(attacker == 1):
            attacker = 0
        elif(attacker == 0):
            attacker = 1
        if(php <= 0):
            if(encrit == True):
                print("CRITICAL HIT!!!")
                encrit = False
            print("----" + "Your HP" + "----")
            print("0")
            if(pcrit == True):
                print("CRITICAL HIT!!!")
                pcrit = False
            print("----" + "Enemy HP" + "----")
            print(enhp)
            print("You have died!")
            print("Enemies Health: " + str(enhp))
            break
        if(enhp <= 0):
            if(encrit == True):
                print("CRITICAL HIT!!!")
                encrit = False
            print("----" + "Your HP" + "----")
            print(php)
            if(pcrit == True):
                print("CRITICAL HIT!!!")
                pcrit = False
            print("----" + "Enemy HP" + "----")
            print("0")
            print(enname + " has died!")
            print("Your Health: " + str(php))
            break
        clearScreen()
        if(encrit == True):
            print("CRITICAL HIT!!!")
            encrit = False
        print("----" + "Your HP" + "----")
        print(php)
        if(pcrit == True):
            print("CRITICAL HIT!!!")
            pcrit = False
        print("----" + "Enemy HP" + "----")
        print(enhp)
        sleep(0.75)
    print("You have gained " + str(en.retxpaw()) + " XP :D")
    print("Your Loot:")
    r1 = randint(1, 10)
    r2 = randint(1, 1000)
    r3 = randint(1, 5)
    print(r1)
    print(r2)
    print(r3)
    if(r1 == 1):
        print("5 Items")
    elif(r1 < 3):
        print("3 Items")
    else:
        print("2 Items")
    i = input("Press Enter To Continue...\n")
    p.levelup(int(en.retxpaw()))
    p.updatehp(php)
    p.fixhp()
    clearScreen()
