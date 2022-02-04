from os import system
from time import sleep
from random import randint
# ---------------------------------------------------------------------- #
# All default Global Variables will be here

hp = 10 # The current hp of the player
armorLevel = 0 # How good the armor the player is currently wearing
name = ' ' # Players name
god = ' ' # Name of the players god
godOrGoddess = 'Parent' # Gender of the players parent and wether to refer to them as god or goddess nr k,jgbn
fatherOrMother = 'Parent'
inventoryFull = False
arrowhead = '\U000025CB'
xCord = 0
yCord = 0

# ---------------------------------------------------------------------- #
# All lists, dictionaries and other like things will be here

godList = ("Zeus", "Hades", "Poseidon", "Apollo", "Ares", "Hephaestus", "Hermes", "Dionysus", "Demeter", "Athena", "Artemis", "Aphrodite") #list of optional gods/goddesses
godFact = ("Zeus is the god of lightning and the Heavens", "Hades is the god of death", "Poseidon is the god of the sea", "Apollo is the god of archery and healing", "Ares is the god of war and fighting", "Hephaestus is the god of fire and frogeing", "Hermes is the god of speed amd messages", "Dionysus is the god of partying and wine", "Demeter is the goddess of farming and food", "Athena is the goddess of wisdom and tactics", "Artemis is the goddess of hunting and nature", "Aphrodite is the goddess of love and beuaty") #list of god/goddess facts corresponding to the list of the availible gods/goddesses

# This will be a list of the players current inventory
inventoryItems = ["Basic Shield", "Athena\'s Shield", "Basic Sword", "Basic Bow"]
inventorySlotQuantity = [1, 1, 1, 1, 1]
# This will be a dictionary corresponding an item name to its descriptioin
items = { 
  # item name : [item description line one , if there isn't enough room line 2 description]
  "Empty" : "You having nothing in this inventory slot. Pick something up!",
  "Basic Bow" : "It\'s a basic shield. + 1 to range attacks",
  "Basic Sword" : "It\'s a basic shield. + 1 to melee attacks.",
  "Basic Shield" : "It\'s a basic shield. + 1 to armor.",
  "Athena\'s Shield" : "A special shield only given to Athena\'s champion. +2 to armor."
}
y4 = ['E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_']
y3 = ['E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_']
y2 = ['E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_']
y1 = ['E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_']
y0 = ['E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_']

revealY4 = ['E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_']
revealY3 = ['E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_']
revealY2 = ['E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_']
revealY1 = ['E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_']
revealY0 = ['E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_', 'E_']

roomTypes = {
  #Name  bottom  middle  top
  'FW' : [' | ', '-+-', ' | '], # FW 'Four Way'
  #[ | ] Example top
  #[-+-] Example middle |
  #[ | ] Example bottom Y-
  'V~' : [' | ', ' | ', ' | '], # V~ 'Vertical' 
  'H~' : ['   ', '---', '   '], # H~ 'Horizantal'
  'NB' : ['   ', '-+-', ' | '], # NB 'Everything but the bottom'
  'NL' : [' | ', ' +-', ' | '], # NL 'Everything but the left'
  'NR' : [' | ', '-+ ', ' | '], # NR 'Everything but the right'
  'NU' : [' | ', '-+-', '   '], # NB 'Everything but the top'
  'UL' : ['   ', '-+ ', ' | '], # UL 'Goes up and then left'
  'UR' : ['   ', ' +-', ' | '], # UR 'Goes up and then right'
  'BL' : [' | ', '-+ ', '   '], # BL 'Goes from the left then down'
  'BR' : [' | ', ' +-', '   '], # BR 'Goes from the right then down'
  'DU' : ['   ', '   ', ' | '], # DU 'Dead end from the top'
  'DL' : ['   ', '-  ', '   '], # DL 'Dead end from the left'
  'DB' : [' | ', '   ', '   '], # DB 'Dead end from the bottom'
  'DR' : ['   ', '  -', '   '], # DR 'Dead end from the right'
  'E_' : ['   ', '   ', '   '], # E_ 'Empty'
  'PFW' : [' | ', f'-{arrowhead}-', ' | '], # FW 'Four Way' with the player token
  'PV~' : [' | ', f' {arrowhead} ', ' | '], # V~ 'Vertical' with the player token
  'PH~' : ['   ', f'-{arrowhead}-', '   '], # H~ 'Horizantal' with the player token
  'PNB' : ['   ', f'-{arrowhead}-', ' | '], # NB 'Everything but the bottom' with the player token
  'PNL' : [' | ', f' {arrowhead}-', ' | '], # NL 'Everything but the left' with the player token
  'PNR' : [' | ', f'-{arrowhead} ', ' | '], # NR 'Everything but the right' with the player token
  'PNU' : [' | ', f'-{arrowhead}-', '   '], # NB 'Everything but the top' with the player token
  'PUL' : ['   ', f'-{arrowhead} ', ' | '], # UL 'Goes up and then left' with the player token
  'PUR' : ['   ', f' {arrowhead}-', ' | '], # UR 'Goes up and then right' with the player token
  'PBL' : [' | ', f'-{arrowhead} ', '   '], # BL 'Goes from the left then down' with the player token
  'PBR' : [' | ', f' {arrowhead}-', '   '], # BR 'Goes from the right then down' with the player token
  'PDU' : ['   ', f' {arrowhead} ', ' | '], # DU 'Dead end from the top' with the player token
  'PDL' : ['   ', f'-{arrowhead} ', '   '], # DL 'Dead end from the left' with the player token
  'PDB' : [' | ', f' {arrowhead} ', '   '], # DB 'Dead end from the bottom' with the player token
  'PDR' : ['   ', f' {arrowhead}-', '   ']  # DR 'Dead end from the right' with the player token
}

# ---------------------------------------------------------------------- #
# All functions will be define here (unless it is a temporary function defined in a specific part of the game)

# This shows the default size of the screen that shows everything
def blankScreen(scale):
  print('_' * int(65 * scale))
  i = 1
  while i < (int(16 * scale)):
    print('|' + (' ' * int((65 * scale - 2))) + '|')
    i += 1
  print('|' + ('_' * int((65 * scale - 2))) + '|')

def splitSentencesUp(sentence, maxLength):
  newStrings = [""]
  sentenceWords = sentence.split(" ") # Splits any string I give it into a list with each list tiem being a word
  previousString = "" 
  count = 0 # Initializing count to 0 because you start with the 0th word in the list
  for i in sentenceWords: # Loops through each word in the list
    if len(i) + len(previousString) <= maxLength: # If that word plus whatever the previous stuff is less then the maxed allowed length then we can add that word to the new strings.
      newStrings.insert(count, f'{previousString}{i} ')
      previousString = newStrings[count]
      newStrings.pop()
    else: # if the word cant be added to the new strings because its too long then we add another list item which is that word.
      count += 1
      newStrings.insert(count, i)
      previousString = f"{i} "
  return newStrings
def splitParagraphUp(paragraph):
  newStrings = []
  lines = paragraph.split("~") # forces a new line
  for i in lines:
      newStrings.append(splitSentencesUp(i, 60))
  return newStrings

#This makes, displays and keeps track of the player health or HP. Based around the global variable hp
def healthbar():
  # health = '\U000026E8 \U0001F90D _ X '
  health =  ('X ' * (10-hp)) + ('\U00002764 ' * hp)
  return health

# This makes, displays and keep tracks of what aromor level the player has. Based around the global variable armorLevel
def armorbar():
  armor =  ('_ ' * (10-armorLevel)) + ('\U000026E8 ' * armorLevel) 
  return armor

# This makes the basic screen with health name god and armor. Also includes any 3 lines of text you want to display.
def displayScreen1(displayText1, displayText2, displayText3):
  a = len(splitSentencesUp(displayText1, 64))
  print(a)
  system ('cls')
  print('_' * 65)
  print('|' + ' ' + f'Name: {name}' + ' '*(55 - len(name) - len(healthbar())) + f'{healthbar()} ' + '|')
  print('|' + ' ' + f'{godOrGoddess}: {god}' + ' '*(59 - len(godOrGoddess) - len(god) - len(armorbar())) + f'{armorbar()} ' + '|')
  i = 0
  while i < 5:
    print('|' + ' ' * 63 + '|')
    i += 1
  print('|' + f'{displayText1:^63}' + '|') # This is the upper middle part cant be more than 63 characters
  print('|' + f'{displayText2:^63}' + '|') # If you obnly display one line of texzt use this line
  print('|' + f'{displayText3:^63}' + '|')
  i = 0
  while i < 5:
    print('|' + ' ' * 63 + '|')
    i += 1
  print('|' + '_' * 63 + '|')

# This displays just text inside the viewing box. It is used for exposition and such. Always hit enter to move to the next part of the code.
def justText(text1, text2, text3):
  while True:
    displayScreen1(f'{text1}', f'{text2}', f'{text3}')
    next  = input('Answer: ').lower()
    if next == '':
      break
    else:
      displayScreen1('', '', 'Hold on a sec... you just need to hit enter')
      sleep(2)

def addToInventory(newItem):
  count = 0
  for i in inventoryItems:
    if count == 3:
      inventoryFull = True
      break
    elif i == "Empty":
      inventoryItems[count] = newItem
      break
    elif i == newItem:
      inventorySlotQuantity[count] += 1
      break
    else:
      count += 1

def displaySlotQuantity(slotNumber):
  if inventorySlotQuantity[slotNumber] == 1:
    return ''
  else:
    return f' {inventorySlotQuantity[slotNumber]}'

# This creates and displays an inventory slot based on the intem and that items disrciption
def displaySlotSide(slotNumber, upper):
  if upper == True:
    try:
      return f'{displaySlotQuantity(slotNumber)} {splitSentencesUp((inventoryItems[slotNumber]), 9)[0]}'
    except IndexError:
      return ''
  else:
    try:
      return f'{splitSentencesUp((inventoryItems[slotNumber]), 9)[1]}{splitSentencesUp((inventoryItems[slotNumber]), 9)[2]}'
    except IndexError:
      try:
        return f'{splitSentencesUp((inventoryItems[slotNumber]), 9)[1]}'
      except IndexError:
        return ''
def displayDescriptionSide(slotNumber, upper):
  if upper == True:
    try:
      return f'{splitSentencesUp((items[inventoryItems[slotNumber]]), 27)[0]}'
    except IndexError:
      return ''
  else:
    try:
      return f'{splitSentencesUp((items[inventoryItems[slotNumber]]), 27)[1]}{splitSentencesUp((items[inventoryItems[slotNumber]]), 27)[2]}'
    except IndexError:
      try:
        return f'{splitSentencesUp((items[inventoryItems[slotNumber]]), 27)[1]}'
      except IndexError:
        return ''

# ---------------------------------------------------------------------- #
def printSlot(slotNumber):
  print('| ' + f'Slot {slotNumber + 1}:{displaySlotSide(slotNumber, True)}' + (' ' * (11 - len(displaySlotSide(slotNumber, True)))) + f'| Description: {displayDescriptionSide(slotNumber, True)}' + (' ' * (28 - len(displayDescriptionSide(slotNumber, True)))) + ' |')

  print('| ' + f'{displaySlotSide(slotNumber, False)}' + (' ' * (18 - len(displaySlotSide(slotNumber, False)))) + '| ' + f'{displayDescriptionSide(slotNumber, False)}' + (' ' * (42 - len(displayDescriptionSide(slotNumber, False)))) + '|')

def displayInvintory():
  system('cls')
  print('_' * 65)
  print('|' + (' ' * 63) + '|')
  print('|' + (f'Invintory is now opened. Press X to go back to the story '.center(63, ' ')) + '|')
  print('|' + (f'to use an item type either the item name or the slot number.'.center(63, ' ')) + '|') 
  print('|' + ('-' * 19) + '' + ('-' * 43) + '|')
  printSlot(0)
  print('|' + ('-' * 19) + '+' + ('-' * 43) + '|')
  printSlot(1)
  print('|' + ('-' * 19) + '+' + ('-' * 43) + '|')
  printSlot(2)
  print('|' + ('-' * 19) + '+' + ('-' * 43) + '|')
  printSlot(3)
  print('|' + ('_' * 63) + '|')

def displayJournal():
  system('cls')
  print('_' * 65)
  print('|' + (' ' * 63) + '|')
  print('|' + (' ' * 63) + '|')
  print('|' + (' ' * 63) + '|')
  print('|' + (' ' * 63) + '|')
  print('|' + (' ' * 63) + '|')
  print('|' + (' ' * 63) + '|')
  print('|' + (' ' * 63) + '|')
  print('|' + (' ' * 63) + '|')
  print('|' + (' ' * 63) + '|')
  print('|' + (' ' * 63) + '|')
  print('|' + (' ' * 63) + '|')
  print('|' + (' ' * 63) + '|')
  print('|' + (' ' * 63) + '|')
  print('|' + (' ' * 63) + '|')
  print('|' + (' ' * 63) + '|')
  print('|' + ('_' * 63) + '|')

def displayMiniMap():
  def displayLine(yline, subLine):
    previousWhatToReturn = ''
    for i in range(11):
      addToWhatToReturn = (roomTypes[f'{yline[i]}'][subLine])
      whatToReturn = f'{previousWhatToReturn}{addToWhatToReturn}'
      previousWhatToReturn = whatToReturn
    return whatToReturn
  system('cls')
  print('_' * 65)
  print('|' + ('IMPORTANT INFO:'.center(25)) + '|  ' + ('Mini Map:' + ' ' * 20) + 'Exit  |')
  print('|' + (' ' * 25) + '|  ' + f'{displayLine(revealY4, 2)}' + (' ' * 2) + '|')
  print('|' + ('  Follow the lines NOT   ') + '|  ' + f'{displayLine(revealY4, 1)}' + (' ' * 2) + '|')
  print('|' + ('the spaces'.center(25)) + '|  ' + f'{displayLine(revealY4, 0)}' + (' ' * 2) + '|')
  print('|' + (' '.center(25)) + '|  ' + f'{displayLine(revealY3, 2)}' + (' ' * 2) + '|')
  print('|' + (' \'|\' Is a vertical path.'.center(25)) + '|  ' + f'{displayLine(revealY3, 1)}' + (' ' * 2) + '|')
  print('|' + (' \'+\' Is a turn or split  ') + '|  ' + f'{displayLine(revealY3, 0)}' + (' ' * 2) + '|')
  print('|' + ('path.'.center(25)) + '|  ' + f'{displayLine(revealY2, 2)}' + (' ' * 2) + '|')
  print('|' + (' \'-\' Is a side path.'.center(25)) + '|  ' + f'{displayLine(revealY2, 1)}' + (' ' * 2) + '|')
  print('|' + (' ' * 25) + '|  ' + f'{displayLine(revealY2, 0)}' + (' ' * 2) + '|')
  print('|' + ('You start at the bottom'.center(25)) + '|  ' + f'{displayLine(revealY1, 2)}' + (' ' * 2) + '|')
  print('|' + ('left and end in the'.center(25)) + '|  ' + f'{displayLine(revealY1, 1)}' + (' ' * 2) + '|')
  print('|' + ('top right!'.center(25)) + '|  ' + f'{displayLine(revealY1, 0)}' + (' ' * 2) + '|')
  print('|' + (' ' * 25) + '|  ' + f'{displayLine(revealY0, 2)}' + (' ' * 2) + '|')
  print('|' + (' ' * 25) + '|  ' + f'{displayLine(revealY0, 1)}' + (' ' * 2) + '|')
  print('|' + (' ' * 25) + '|  ' + ' | <-Start' + (' ' * 25) + '|')
  print('|' + ('_' * 25) + '|' + ('_' * 37) + '|')

# ---------------------------------------------------------------------- #
  
def yaxis(yLevel): #This turns any y level in y'that level' so I can acess that list easier
  if yLevel == 0:
    return y0
  elif yLevel == 1:
    return y1
  elif yLevel == 2:
    return y2
  elif yLevel == 3:
    return y3
  elif yLevel == 4:
    return y4

def createMaze(): # Generates a Random Maze. Solveable and no empty spaces. All interconnected. 
  path = [[0, 0]] # This is where the coordinates of all the tiles added go

  def createMainPath(): # This creates the main or intended path. It is the path you have to follow and go through to get to the exit
    y = 0 # Think of the maze as a grid with each coordinate being a room 
    x = 0 # You start at (0,0) or the bottom left
    previous = '' # There is no previous room because we have yet to create anything
    randomNumber = randint(0,1) # Chooses 1 or 0 randomly
    if randomNumber == 0: #From the start you can only go up or to the right since there is nothing down or to the left
      (yaxis(y))[x] = 'BR' 
      x += 1
      previous = 'x+1' # Chooses to go right and makes previous x+1 as in 1 to the right
    elif randomNumber == 1:
      (yaxis(y))[x] = 'V~'
      y += 1
      previous = 'y+1' # Chooses to go up and makes previous x+y as in 1 up

    while True:
      if (yaxis(y))[x] != 'E_': # If the tile the Ai wants is not empty then it deletes all the tiles that appear after the tile it wants to got. Then the Ai starts over at that point
        (yaxis(path[-1][1]))[path[-1][0]] = 'E_'
        while True:
          if path[-2][0] != x or path[-2][1] != y: # If this tile is not the tile that the Ai wants to start over at then it deletes that tile and then remove it from the path
            (yaxis(path[-2][1]))[path[-2][0]] = 'E_'
            path.pop()
          else: # If this runs then taht means the Ai reached the tile it wants to start over from. 
            if path[-2][1] + 1 == path[-1][1]:
              y += 1
              previous = 'y+1'
            elif path[-2][1] - 1 == path[-1][1]:
              y -= 1
              previous = 'y-1'
            elif path[-2][0] + 1 == path[-1][0]:
              x += 1
              previous = 'x+1'
            elif path[-2][0] - 1 == path[-1][0]: # Finds out what direction the tile leads into by seeing what direction the tile after is placed. If the tile after is 1 up in the y direction that means this tile is leading up
              x -= 1 
              previous = 'x-1'
            path.pop() # Deletes that reference tile it used to find the direction
            break

      if previous == 'x+1': # If the previous tile leads in from the left then there are only certian things the next tile can be.
        randomNumber = randint(1,7)
        if randomNumber >= 1 and randomNumber <= 4 and x != 10: # The likelyhood that it goes right is 4 times as likely since there is a lot of ground to cover going right
          (yaxis(y))[x] = 'H~'
          path.append([x, y])
          x += 1
          previous = 'x+1'
        elif randomNumber >= 5 and randomNumber <=6 and y != 4: # The likelyhood that it goes up is twice as likely since you want it to go up more than it goes down
          (yaxis(y))[x] = 'UL'
          path.append([x, y])
          y += 1
          previous = 'y+1'
        elif randomNumber == 7 and y != 0: # It is not very likely to go down
          (yaxis(y))[x] = 'BL'
          path.append([x, y]) # Afterwards adds the coordinates of the tile to the path list
          y -= 1
          previous = 'y-1'

      elif previous == 'x-1': # Same thing as before but when it is being lead in from the right
        randomNumber = randint(1,5)
        if randomNumber >= 1 and randomNumber <=2 and x != 0:
          (yaxis(y))[x] = 'H~'
          path.append([x, y])
          x -= 1
          previous = 'x-1'
        elif randomNumber >= 3 and randomNumber <=4 and y != 4:
          (yaxis(y))[x] = 'UR'
          path.append([x, y])
          y += 1
          previous = 'y+1'
        elif randomNumber == 5 and y != 0:
          (yaxis(y))[x] = 'BR'
          path.append([x, y])
          y -= 1
          previous = 'y-1'

      elif previous == 'y+1': # Same thing as before but when it is being lead in from the top
        randomNumber = randint(1,8)
        if randomNumber >= 1 and randomNumber <=2 and x != 0:
          (yaxis(y))[x] = 'BL'
          path.append([x, y])
          x -= 1
          previous = 'x-1'
        elif randomNumber >= 3 and randomNumber <=4 and y != 4:
          (yaxis(y))[x] = 'V~'
          path.append([x, y])
          y += 1
          previous = 'y+1'
        elif randomNumber >= 5 and randomNumber <=8 and x != 10:
          (yaxis(y))[x] = 'BR'
          path.append([x, y])
          x += 1
          previous = 'x+1'

      elif previous == 'y-1': # Same thing as before but when it is being lead in from the top
        randomNumber = randint(1,7)
        if randomNumber >= 1 and randomNumber <=2 and x != 0:
          (yaxis(y))[x] = 'UL'
          path.append([x, y])
          x -= 1
          previous = 'x-1'
        elif randomNumber == 3 and y != 0:
          (yaxis(y))[x] = 'V~'
          path.append([x, y])
          y -= 1
          previous = 'y-1'
        elif randomNumber >= 4 and randomNumber <=7 and x != 10:
          (yaxis(y))[x] = 'UR'
          path.append([x, y])
          x += 1
          previous = 'x+1'

      if y == 4 and x == 10: # Once you get to the coordinates (10, 4) then it ends the loop of adding tile since the Ai reached the exit. 
        if previous == 'y+1': # It needs to know if the previous tile leads in from the botttom or from the left
          (yaxis(4))[10] = 'V~'
        elif previous == 'x+1':
          (yaxis(4))[10] = 'UL'
        break
  createMainPath()

  def createSplitPaths(): # This runs after the Ai creates the main pathway. The porpuse of this function is to create a bunch of false paths until it is no longer abe to do so.
    while len(path) != 0: # If there is no longer any paths left then the loop ends since it cant create any more falce paths
      randomNumber = randint(0, (len(path) - 1)) # The Ai chooses a random tile that is on the path
      y = path[randomNumber][1] # It finds the y value of that random tile
      x = path[randomNumber][0] # It also finds the x value
      avialableSurroundings = [] # This is where it store all the tiles that are available to branch of into AKA the nearby tiles that are empty

      try:
        if (yaxis(y))[x + 1] == 'E_': # sees if the tile to the right of the randomly chosen tile is empty
          avialableSurroundings.append([x + 1, y])
      except:
        pass
      try:
        if x - 1 < 0: # sees if the tile to the left of the randomly chosen tile is empty. it wont do this if x is negative
          pass
        elif (yaxis(y))[x - 1] == 'E_':
          avialableSurroundings.append([x - 1, y])
      except:
        pass
      try:
        if (yaxis(y - 1))[x] == 'E_': # sees if the tile below the randomly chosen tile is empty
          avialableSurroundings.append([x, y - 1])
      except:
        pass
      try:
        if (yaxis(y + 1))[x] == 'E_': # sees if the tile above the randomly chosen tile is empty
          avialableSurroundings.append([x, y + 1])
      except:
        pass

      if len(avialableSurroundings) > 0: # If there is something available in the soroundings then...
        randomNumber2 = randint(0, (len(avialableSurroundings) - 1)) # Then it chooses a random free space
        changeDict = {
          # Previous tile -> what it can turn into [if add right, if add up, if add left, if add down] if you cant add a part since it already has it change it to "cant"
          'V~' : ['NL', 'Cant', 'NR', 'Cant'], # Example: You cant add an up or botttom part to vertical section 
          'H~' : ['Cant', 'NB', 'Cant', 'NU'],
          'NR' : ['FW', 'Cant', 'Cant', 'Cant'],
          'NU' : ['Cant', 'FW', 'Cant', 'Cant'],
          'NL' : ['Cant', 'Cant', 'FW', 'Cant'],
          'NB' : ['Cant', 'Cant', 'Cant', 'FW'],
          'BR' : ['Cant', 'NL', 'NU', 'Cant'],
          'BL' : ['NU', 'NR', 'Cant', 'Cant'],
          'UR' : ['Cant', 'Cant', 'NB', 'NL'],
          'UL' : ['NB', 'Cant', 'Cant', 'NR'],
          'DR' : ['Cant', 'UR', 'H~', 'BR'],
          'DU' : ['UR', 'Cant', 'UL', 'V~'],
          'DL' : ['H~', 'UL', 'Cant', 'BL'],
          'DB' : ['BR', 'V~', 'BL', 'Cant']
        }
        if path[randomNumber][1] + 1 == avialableSurroundings[randomNumber2][1]: # Sees what direction the new tile is and changes the tile leading into the new tile so it looks like it is leading in to the new tile
          (yaxis(y))[x] = changeDict[(yaxis(y))[x]][1]
          (yaxis(y + 1))[x] = 'DB' # Makes the tile that is being lead into
        elif path[randomNumber][1] - 1 == avialableSurroundings[randomNumber2][1]:
          (yaxis(y))[x] = changeDict[(yaxis(y))[x]][3]
          (yaxis(y - 1))[x] = 'DU'
        elif path[randomNumber][0] + 1 == avialableSurroundings[randomNumber2][0]:
          (yaxis(y))[x] = changeDict[(yaxis(y))[x]][0]
          (yaxis(y))[x + 1] = 'DL'
        elif path[randomNumber][0] - 1 == avialableSurroundings[randomNumber2][0]:
          (yaxis(y))[x] = changeDict[(yaxis(y))[x]][2]
          (yaxis(y))[x - 1] = 'DR'
        path.append(avialableSurroundings[randomNumber2]) # Adds new tile to the list of paths since it can be then added to later
      elif len(avialableSurroundings) == 0: # If there is no empty spots in the surroundings then remove that option from the path list so it doesn't accidently get chosen again since its non to not lead anywhere
        path.remove(path[randomNumber])
  createSplitPaths()    



def revealPath():
  global yCord
  global xCord
  def coordinate(y):
    if y == 0:
      return revealY0
    elif y == 1:
      return revealY1
    elif y == 2:
      return revealY2
    elif y == 3:
      return revealY3
    elif y == 4:
      return revealY4
  up = ''
  down = ''
  left = ''
  right = ''
  tile = f'{yaxis(yCord)[xCord]}'
  if tile == 'DU' or tile == 'NL' or tile == 'NR' or tile == 'NB' or tile == 'FW' or tile == 'V~' or tile == 'UL' or tile == 'UR':
    up = ' up [U]'
  if tile == 'DB' or tile == 'NL' or tile == 'NR' or tile == 'NU' or tile == 'FW' or tile == 'V~' or tile == 'BL' or tile == 'BR':
    down = ' down [D]'
  if tile == 'DL' or tile == 'NU' or tile == 'NR' or tile == 'NB' or tile == 'FW' or tile == 'H~' or tile == 'UL' or tile == 'BL':
    left = ' left [L]'
  if tile == 'DR' or tile == 'NL' or tile == 'NU' or tile == 'NB' or tile == 'FW' or tile == 'H~' or tile == 'UR' or tile == 'BR': 
    right = ' right [R]'
  coordinate(yCord)[xCord] = f'P{tile}'
  displayMiniMap()
  move = input(f'Would you like to go{up}{down}{left} or{right}? ')
  if move == 'U':
    coordinate(yCord)[xCord] = tile
    yCord += 1
    coordinate(yCord)[xCord] = f'P{tile}'
  elif move == 'D':
    coordinate(yCord)[xCord] = tile
    yCord -= 1
    coordinate(yCord)[xCord] = f'P{tile}'
  elif move == 'R':
    coordinate(yCord)[xCord] = tile
    xCord += 1
    coordinate(yCord)[xCord] = f'P{tile}'
  elif move == 'L':
    coordinate(yCord)[xCord] = tile
    xCord -= 1
    coordinate(yCord)[xCord] = f'P{tile}'

  displayMiniMap()
  

# ---------------------------------------------------------------------- #
# This is the testing zone
createMaze()
while True:
  revealPath()
input('')

# ---------------------------------------------------------------------- #
# This is the actual game with all the storlines and options


justText('', 'Welcome to Jacob Logan\'s game!', 'Press enter to continue.')
justText('About the game: It\'s a choose your own adventure (CYOA).', 'Whenever there\'s a screen with just text and no question hit', 'Hit enter to continue.')
justText('There you! Your\'re getting the hang of it!', 'The game is based around Greek Myths. Your health and armor', 'appear in the top right and your name and parent in the left.')

#finds out what the player wants to be called and makes sure that what they want to becalled is capitilzed and between 0-25 charectors.
displayScreen1('', 'So... what do you want to be called?', 'Type your answer below!')
while True:
  nameTemp = input('Answer: ').title()
  if len(nameTemp) > 30:
    displayScreen1('Your name is too long. Try a different one.', 'What do you want to be called?', '')
  elif len(nameTemp) == 0:
    displayScreen1('You need a name.', 'What do you want to be called?', 'Type your answer below!')
  else:
    displayScreen1('', f'Are you happy with the name: {nameTemp}? ', 'Yes or No')
    while True:
      satisfied = input('Answer: ').lower()
      if satisfied == 'yes':
        name = nameTemp
        break
      elif satisfied == 'no':
        displayScreen1(f'Okay you don\'t want to be called {nameTemp}', 'What do you want to be called?', '')
        break
      else:
        displayScreen1('It is a yes or no question.', f'Are you happy with the name: {nameTemp}? ', 'Yes or No')
    if satisfied == 'yes':
      break

while True: # This is the section of the game where the player decides what god or goddess they want for a parent
  displayScreen1('Pick one of the gods/goddesses below to learn more about them', 'Zeus, Hades, Poseidon, Apollo, Ares, Hephaestus, Hermes,', ' Dionysus, Demeter, Athena, Artemis, & Aphrodite')
  godNumber = 0 # This goes with the list of gods/goddesses go up to the god/goddess list
  godResponse = ''
  godResponse = input('Answer: ').capitalize()
  for x in godList: # Goes through the list of available gods and finds which one the player picked and what number that god is on the list
    if x == godResponse:
      break
    else: 
      godNumber += 1
  try:
    displayScreen1('', f'You chose {godList[godNumber]}! That is a great choice!', '')
  except:
    displayScreen1('', 'Hold on a sec.. you need to pick an available god/goddess', '') # If I there is an error for whatever reason then say something went wrong and cicle back up to ask what god again.
    sleep(2)
  else:
    if godNumber < 8: # This identifies what gender to call the god/goddess 
      godOrGoddessTemp = 'God'
      fatherOrMotherTemp = 'Father'
    else:
      godOrGoddessTemp = 'Goddess'
      fatherOrMotherTemp = 'Mother'
    displayScreen1(f'You chose {godList[godNumber]}! That is a great choice!', f'{godFact[godNumber]}', f'Would you like to choose {godList[godNumber]} to be your {fatherOrMotherTemp}? Yes or no')
    while True:
      godWant = input('Answer: ').lower() # Verify that this is the god/goddess the player wants
      if godWant == 'yes':
        break
      elif godWant == 'no':
        break
      else:
        displayScreen1('It is a yes or no question.', f'Would you like to choose {godList[godNumber]} to be your parent', 'Yes or No')
    if godWant == 'yes': # Makes what we wer temporarly calling the god/goddess what we will permenatly call them
        god = godResponse
        godOrGoddess = godOrGoddessTemp
        fatherOrMother = fatherOrMotherTemp
        break
    else:
        continue

# ---------------------------------------------------------------------- #

#If you made it to this screen that most likely means stuff is working so far
displayScreen1('If you\'re at this screen then you\'re at the end of the game.', 'So far...', 'Things must be working nicely! :)')