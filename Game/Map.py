def clear(int1):
    int1 = int(int1)
    text = "\n\n\n\n\n\n"
    while int1 != 23:
        text = text + "\n"
        int1 = int1 + 1
    print(text)
def changeroom(direc, cordx, cordy, ml, roomcomp):
  if(direc == "up"):
    if(cordy == 0):
      print("Cannot go up any further")
      return None
    else:
      if(ml[(cordy - 1)][cordx][0] == "o"):
        ml[cordy][cordx][0] = "o"
        cordy = cordy - 1
        ml[cordy][cordx][0] = "x"
        return True
      else:
        if(roomcomp == False):
          print("You must defeat everyone in this room before you move!")
        if(roomcomp == True):
          ml[cordy][cordx][0] = "o"
          cordy = cordy - 1
          ml[cordy][cordx][0] = "x"

  if(direc == "down"):
    if(cordy == 8):
      print("Cannot go down any further")
      return None
    else:
      if(ml[(cordy + 1)][cordx][0] == "o"):
        ml[cordy][cordx][0] = "o"
        cordy = cordy + 1
        ml[cordy][cordx][0] = "x"
        return True
      else:
        if(roomcomp == False):
          print("You must defeat everyone in this room before you move!")
        if(roomcomp == True):
          ml[cordy][cordx][0] = "o"
          cordy = cordy + 1
          ml[cordy][cordx][0] = "x"

  if(direc == "left"):
    if(cordx == 0):
      print("Cannot go left any further")
      return None
    else:
      if(ml[cordy][(cordx - 1)][0] == "o"):
        ml[cordy][cordx][0] = "o"
        cordx = cordx - 1
        ml[cordy][cordx][0] = "x"
        return True
      else:
        if(roomcomp == False):
          print("You must defeat everyone in this room before you move!")
        if(roomcomp == True):
          ml[cordy][cordx][0] = "o"
          cordx = cordx - 1
          ml[cordy][cordx][0] = "x"

    
  if(direc == "right"):
    if(cordx == 8):
      print("Cannot go right any further")
      return None
    else:
      if(ml[cordy][(cordx + 1)][0] == "o"):
        ml[cordy][cordx][0] = "o"
        cordx = cordx + 1
        ml[cordy][cordx][0] = "x"
        return True
      else:
        if(roomcomp == False):
          print("You must defeat everyone in this room before you move!")
        if(roomcomp == True):
          ml[cordy][cordx][0] = "o"
          cordx = cordx + 1
          ml[cordy][cordx][0] = "x"

def showmap(roomcomp,cordx,cordy, ml, roomcomp):
    abool = True
    while abool == True:
      text = ""
      for ab in ml:
        for bb in ab:
            if(bb[0] == "q"):
                text = text + " " + chr(9632)
            else:
                text = text + " " + bb[0]
        text = text + "\n"
      print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
      print(text)
      clear(4)
      i = input("1. Up\n2. Down\n3. Left\n4. Right\n")
      if(i == "1"):
        changeroom("up")
      elif(i == "2"):
        changeroom("down")
      elif(i == "3"):
        changeroom("left")
      elif(i == "4"):
        changeroom("right")

