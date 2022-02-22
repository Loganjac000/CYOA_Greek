from os import system
from random import randint

from pip import main

icon = '\U000025CB'
xCord = 0
yCord = 0
mainpath = 0
# These are where we keep all the info about each tile. a tile is one room and all the infor about it
# the y_ is what y level the tile is on. It is a list with 11 list elements for each of the 11 x points on each y line. 4 y lines times 11 x points per line equals 44 total tiles
# Each of the x points is its own list. the first element on that list is the room typee,  the second element is whether it is one the main path or split path.
# The third element is what type of encounter it is. The fourth one is what specific encounter it is. 
y4 = [
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True}]
y3 = [
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True}]
y2 = [
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True}]
y1 = [
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True}]
y0 = [
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True},
  {'roomtype' : 'E_',
   'revealed' : 'E_',
   'isItMain' : True}]
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
  'DU' : ['   ', ' x ', ' | '], # DU 'Dead end from the top'
  'DL' : ['   ', '-x ', '   '], # DL 'Dead end from the left'
  'DB' : [' | ', ' x ', '   '], # DB 'Dead end from the bottom'
  'DR' : ['   ', ' x-', '   '], # DR 'Dead end from the right'
  'E_' : ['   ', '   ', '   '], # E_ 'Empty'
  'PFW' : [' | ', f'-{icon}-', ' | '], # FW 'Four Way' with the player token
  'PV~' : [' | ', f' {icon} ', ' | '], # V~ 'Vertical' with the player token
  'PH~' : ['   ', f'-{icon}-', '   '], # H~ 'Horizantal' with the player token
  'PNB' : ['   ', f'-{icon}-', ' | '], # NB 'Everything but the bottom' with the player token
  'PNL' : [' | ', f' {icon}-', ' | '], # NL 'Everything but the left' with the player token
  'PNR' : [' | ', f'-{icon} ', ' | '], # NR 'Everything but the right' with the player token
  'PNU' : [' | ', f'-{icon}-', '   '], # NB 'Everything but the top' with the player token
  'PUL' : ['   ', f'-{icon} ', ' | '], # UL 'Goes up and then left' with the player token
  'PUR' : ['   ', f' {icon}-', ' | '], # UR 'Goes up and then right' with the player token
  'PBL' : [' | ', f'-{icon} ', '   '], # BL 'Goes from the left then down' with the player token
  'PBR' : [' | ', f' {icon}-', '   '], # BR 'Goes from the right then down' with the player token
  'PDU' : ['   ', ' x ', f' {icon} '], # DU 'Dead end from the top' with the player token
  'PDL' : ['   ', f'{icon}x ', '   '], # DL 'Dead end from the left' with the player token
  'PDB' : [f' {icon} ', ' x ', '   '], # DB 'Dead end from the bottom' with the player token
  'PDR' : ['   ', f' x{icon}', '   ']  # DR 'Dead end from the right' with the player token
}

def displayMiniMap():
  def displayLine(yline, subLine):
    previousWhatToReturn = ''
    for i in range(11):
      addToWhatToReturn = (roomTypes[f'{yline[i]["revealed"]}'][subLine])
      whatToReturn = f'{previousWhatToReturn}{addToWhatToReturn}'
      previousWhatToReturn = whatToReturn
    return whatToReturn
  system('cls')
  print('_' * 65)
  print('|' + ('IMPORTANT INFO:'.center(25)) + '|  ' + ('Mini Map:' + ' ' * 20) + 'Exit  |')
  print('|' + (' ' * 25)                                   + '|  ' + f'{displayLine(y4, 2)}' + (' ' * 2) + '|')
  print('|' + ('Follow the line until'.center(25))         + '|  ' + f'{displayLine(y4, 1)}' + (' ' * 2) + '|')
  print('|' + ('you reach the exit!'.center(25))           + '|  ' + f'{displayLine(y4, 0)}' + (' ' * 2) + '|')
  print('|' + (' '.center(25))                             + '|  ' + f'{displayLine(y3, 2)}' + (' ' * 2) + '|')
  print('|' + ('\'|\' Is a vertical path. '.center(25))    + '|  ' + f'{displayLine(y3, 1)}' + (' ' * 2) + '|')
  print('|' + (' \'-\' Is a side path.     ')              + '|  ' + f'{displayLine(y3, 0)}' + (' ' * 2) + '|')
  print('|' + (' \'+\' Is a turn or split  '.center(25))   + '|  ' + f'{displayLine(y2, 2)}' + (' ' * 2) + '|')
  print('|' + ('path'.center(25))                          + '|  ' + f'{displayLine(y2, 1)}' + (' ' * 2) + '|')
  print('|' + (' ' * 25)                                   + '|  ' + f'{displayLine(y2, 0)}' + (' ' * 2) + '|')
  print('|' + ('\'x\' repersents any dead'.center(25))     + '|  ' + f'{displayLine(y1, 2)}' + (' ' * 2) + '|')
  print('|' + ('ends you\'ve encountered.'.center(25))     + '|  ' + f'{displayLine(y1, 1)}' + (' ' * 2) + '|')
  print('|' + (' ' * 25)                                   + '|  ' + f'{displayLine(y1, 0)}' + (' ' * 2) + '|')
  print('|' + (f'The \'{icon}\' is where your'.center(25)) + '|  ' + f'{displayLine(y0, 2)}' + (' ' * 2) + '|')
  print('|' + ('character currently is.'.center(25))       + '|  ' + f'{displayLine(y0, 1)}' + (' ' * 2) + '|')
  print('|' + (''.center(25)) + '|  ' + ' | <-Start' + (' ' * 25) + '|')
  print('|' + ('_' * 25) + '|' + ('_' * 37) + '|')

def displayMiniMapForTesting():
  def displayLine(yline, subLine):
    previousWhatToReturn = ''
    for i in range(11):
      addToWhatToReturn = (roomTypes[f'{yline[i]["roomtype"]}'][subLine])
      whatToReturn = f'{previousWhatToReturn}{addToWhatToReturn}'
      previousWhatToReturn = whatToReturn
    return whatToReturn
  system('cls')
  print('_' * 65)
  print('|' + ('IMPORTANT INFO:'.center(25)) + '|  ' + ('Mini Map:' + ' ' * 20) + 'Exit  |')
  print('|' + (' ' * 25) + '|  ' + f'{displayLine(y4, 2)}' + (' ' * 2) + '|')
  print('|' + ('Follow the line until'.center(25)) + '|  ' + f'{displayLine(y4, 1)}' + (' ' * 2) + '|')
  print('|' + ('you reach the exit!'.center(25)) + '|  ' + f'{displayLine(y4, 0)}' + (' ' * 2) + '|')
  print('|' + (' '.center(25)) + '|  ' + f'{displayLine(y3, 2)}' + (' ' * 2) + '|')
  print('|' + ('\'|\' Is a vertical path. '.center(25)) + '|  ' + f'{displayLine(y3, 1)}' + (' ' * 2) + '|')
  print('|' + (' \'-\' Is a side path.     ') + '|  ' + f'{displayLine(y3, 0)}' + (' ' * 2) + '|')
  print('|' + (' \'+\' Is a turn or split  '.center(25)) + '|  ' + f'{displayLine(y2, 2)}' + (' ' * 2) + '|')
  print('|' + ('path'.center(25)) + '|  ' + f'{displayLine(y2, 1)}' + (' ' * 2) + '|')
  print('|' + (' ' * 25) + '|  ' + f'{displayLine(y2, 0)}' + (' ' * 2) + '|')
  print('|' + ('\'x\' repersents any dead'.center(25)) + '|  ' + f'{displayLine(y1, 2)}' + (' ' * 2) + '|')
  print('|' + ('ends you\'ve encountered.'.center(25)) + '|  ' + f'{displayLine(y1, 1)}' + (' ' * 2) + '|')
  print('|' + (' ' * 25) + '|  ' + f'{displayLine(y1, 0)}' + (' ' * 2) + '|')
  print('|' + ('The \'\U000025CB\' is where your'.center(25)) + '|  ' + f'{displayLine(y0, 2)}' + (' ' * 2) + '|')
  print('|' + ('character currently is.'.center(25)) + '|  ' + f'{displayLine(y0, 1)}' + (' ' * 2) + '|')
  print('|' + (''.center(25)) + '|  ' + ' | <-Start' + (' ' * 25) + '|')
  print('|' + ('_' * 25) + '|' + ('_' * 37) + '|')
# ---------------------------------------------------------------------- #
def loopThroughMaze(search, look):
  count = 0
  for x in y4:
    if y4[x][search] == look:
      count += 1
  for x in y3:
    if y4[x][search] == look:
      count += 1
  for x in y2:
    if y4[x][search] == look:
      count += 1
  for x in y1:
    if y4[x][search] == look:
      count += 1
  for x in y0:
    if y4[x][search] == look:
      count += 1
  return count
  
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
      (yaxis(y))[x]['roomtype'] = 'BR' # the [0] is because we store the room type on the 1st list element of the x point. 
      x += 1
      previous = 'x+1' # Chooses to go right and makes previous x+1 as in 1 to the right
    elif randomNumber == 1:
      (yaxis(y))[x]['roomtype'] = 'V~'
      y += 1
      previous = 'y+1' # Chooses to go up and makes previous x+y as in 1 up

    while True:
      if (yaxis(y))[x]['roomtype'] != 'E_': # If the tile the Ai wants is not empty then it deletes all the tiles that appear after the tile it wants to got. Then the Ai starts over at that point
        (yaxis(path[-1][1]))[path[-1][0]]['roomtype'] = 'E_'
        while True:
          if path[-2][0] != x or path[-2][1] != y: # If this tile is not the tile that the Ai wants to start over at then it deletes that tile and then remove it from the path
            (yaxis(path[-2][1]))[path[-2][0]]['roomtype'] = 'E_'
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
          (yaxis(y))[x]['roomtype'] = 'H~'
          path.append([x, y])
          x += 1
          previous = 'x+1'
        elif randomNumber >= 5 and randomNumber <=6 and y != 4: # The likelyhood that it goes up is twice as likely since you want it to go up more than it goes down
          (yaxis(y))[x]['roomtype'] = 'UL'
          path.append([x, y])
          y += 1
          previous = 'y+1'
        elif randomNumber == 7 and y != 0: # It is not very likely to go down
          (yaxis(y))[x]['roomtype'] = 'BL'
          path.append([x, y]) # Afterwards adds the coordinates of the tile to the path list
          y -= 1
          previous = 'y-1'

      elif previous == 'x-1': # Same thing as before but when it is being lead in from the right
        randomNumber = randint(1,5)
        if randomNumber >= 1 and randomNumber <=2 and x != 0:
          (yaxis(y))[x]['roomtype'] = 'H~'
          path.append([x, y])
          x -= 1
          previous = 'x-1'
        elif randomNumber >= 3 and randomNumber <=4 and y != 4:
          (yaxis(y))[x]['roomtype'] = 'UR'
          path.append([x, y])
          y += 1
          previous = 'y+1'
        elif randomNumber == 5 and y != 0:
          (yaxis(y))[x]['roomtype'] = 'BR'
          path.append([x, y])
          y -= 1
          previous = 'y-1'

      elif previous == 'y+1': # Same thing as before but when it is being lead in from the top
        randomNumber = randint(1,8)
        if randomNumber >= 1 and randomNumber <=2 and x != 0:
          (yaxis(y))[x]['roomtype'] = 'BL'
          path.append([x, y])
          x -= 1
          previous = 'x-1'
        elif randomNumber >= 3 and randomNumber <=4 and y != 4:
          (yaxis(y))[x]['roomtype'] = 'V~'
          path.append([x, y])
          y += 1
          previous = 'y+1'
        elif randomNumber >= 5 and randomNumber <=8 and x != 10:
          (yaxis(y))[x]['roomtype'] = 'BR'
          path.append([x, y])
          x += 1
          previous = 'x+1'

      elif previous == 'y-1': # Same thing as before but when it is being lead in from the top
        randomNumber = randint(1,7)
        if randomNumber >= 1 and randomNumber <=2 and x != 0:
          (yaxis(y))[x]['roomtype'] = 'UL'
          path.append([x, y])
          x -= 1
          previous = 'x-1'
        elif randomNumber == 3 and y != 0:
          (yaxis(y))[x]['roomtype'] = 'V~'
          path.append([x, y])
          y -= 1
          previous = 'y-1'
        elif randomNumber >= 4 and randomNumber <=7 and x != 10:
          (yaxis(y))[x]['roomtype'] = 'UR'
          path.append([x, y])
          x += 1
          previous = 'x+1'

      if y == 4 and x == 10: # Once you get to the coordinates (10, 4) then it ends the loop of adding tile since the Ai reached the exit. 
        if previous == 'y+1': # It needs to know if the previous tile leads in from the botttom or from the left
          (yaxis(4))[10]['roomtype'] = 'V~'
        elif previous == 'x+1':
          (yaxis(4))[10]['roomtype'] = 'UL'
        break
  createMainPath()
  global mainpath
  mainpath = path.copy()
  def createSplitPaths(): # This runs after the Ai creates the main pathway. The porpuse of this function is to create a bunch of false paths until it is no longer abe to do so.
    while len(path) != 0: # If there is no longer any paths left then the loop ends since it cant create any more falce paths
      randomNumber = randint(0, (len(path) - 1)) # The Ai chooses a random tile that is on the path
      y = path[randomNumber][1] # It finds the y value of that random tile
      x = path[randomNumber][0] # It also finds the x value
      avialableSurroundings = [] # This is where it store all the tiles that are available to branch of into AKA the nearby tiles that are empty

      try:
        if (yaxis(y))[x + 1]['roomtype'] == 'E_': # sees if the tile to the right of the randomly chosen tile is empty
          avialableSurroundings.append([x + 1, y])
      except:
        pass
      try:
        if x - 1 < 0: # sees if the tile to the left of the randomly chosen tile is empty. it wont do this if x is negative
          pass
        elif (yaxis(y))[x - 1]['roomtype'] == 'E_':
          avialableSurroundings.append([x - 1, y])
      except:
        pass
      try:
        if (yaxis(y - 1))[x]['roomtype'] == 'E_': # sees if the tile below the randomly chosen tile is empty
          avialableSurroundings.append([x, y - 1])
      except:
        pass
      try:
        if (yaxis(y + 1))[x]['roomtype'] == 'E_': # sees if the tile above the randomly chosen tile is empty
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
          (yaxis(y))[x]['roomtype'] = changeDict[(yaxis(y))[x]['roomtype']][1]
          (yaxis(y + 1))[x]['roomtype'] = 'DB' # Makes the tile that is being lead into
          (yaxis(y + 1))[x]['isItMain'] =  False # Makes note that this is a split path
        elif path[randomNumber][1] - 1 == avialableSurroundings[randomNumber2][1]:
          (yaxis(y))[x]['roomtype'] = changeDict[(yaxis(y))[x]['roomtype']][3]
          (yaxis(y - 1))[x]['roomtype'] = 'DU'
          (yaxis(y - 1))[x]['isItMain'] = False
        elif path[randomNumber][0] + 1 == avialableSurroundings[randomNumber2][0]:
          (yaxis(y))[x]['roomtype'] = changeDict[(yaxis(y))[x]['roomtype']][0]
          (yaxis(y))[x + 1]['roomtype'] = 'DL'
          (yaxis(y))[x + 1]['isItMain'] = False
        elif path[randomNumber][0] - 1 == avialableSurroundings[randomNumber2][0]:
          (yaxis(y))[x]['roomtype'] = changeDict[(yaxis(y))[x]['roomtype']][2]
          (yaxis(y))[x - 1]['roomtype'] = 'DR'
          (yaxis(y))[x - 1]['isItMain'] = False
        path.append(avialableSurroundings[randomNumber2]) # Adds new tile to the list of paths since it can be then added to later
      elif len(avialableSurroundings) == 0: # If there is no empty spots in the surroundings then remove that option from the path list so it doesn't accidently get chosen again since its non to not lead anywhere
        path.remove(path[randomNumber])
  createSplitPaths()
  test()

def revealPath():
  global yCord
  global xCord
  movementOptions = []
  tile = f'{yaxis(yCord)[xCord]["roomtype"]}'
  if tile == 'DU' or tile == 'NL' or tile == 'NR' or tile == 'NB' or tile == 'FW' or tile == 'V~' or tile == 'UL' or tile == 'UR':
    movementOptions.append(' up [U]')
  if tile == 'DB' or tile == 'NL' or tile == 'NR' or tile == 'NU' or tile == 'FW' or tile == 'V~' or tile == 'BL' or tile == 'BR':
    movementOptions.append(' down [D]')
  if tile == 'DL' or tile == 'NU' or tile == 'NR' or tile == 'NB' or tile == 'FW' or tile == 'H~' or tile == 'UL' or tile == 'BL':
    movementOptions.append(' left [L]')
  if tile == 'DR' or tile == 'NL' or tile == 'NU' or tile == 'NB' or tile == 'FW' or tile == 'H~' or tile == 'UR' or tile == 'BR': 
    movementOptions.append(' right [R]')
  yaxis(yCord)[xCord]['revealed'] = f'P{tile}'
# --- Once you figure out what options the player can move continue on to find where they want to move --- #
  while True:
    displayMiniMap()
    if len(movementOptions) == 1:
      move = input(f'Oh no a dead end! You can only go{movementOptions[0]}. Please enter whats in the []. ').capitalize()
    elif len(movementOptions) == 2:
      move = input(f'Would you like to go{movementOptions[0]} or{movementOptions[1]}? ').capitalize()
    elif len(movementOptions) == 3:
      move = input(f'Would you like to go{movementOptions[0]},{movementOptions[1]} or{movementOptions[2]}? ').capitalize()
    elif len(movementOptions) == 4:
      move = input(f'Would you like to go{movementOptions[0]},{movementOptions[1]},{movementOptions[2]} or{movementOptions[3]}? ').capitalize()
# --- once you ask for the move continue move the player token accordingly --- #
    if move == 'U' and (' up [U]' in movementOptions):
      yaxis(yCord)[xCord]['revealed'] = tile
      if xCord == 10 and yCord == 4:
        print('You Win!!')
        break
      yCord += 1
      yaxis(yCord)[xCord]['revealed'] = f'P{tile}'
      displayMiniMap()
      break
    elif move == 'D' and (' down [D]' in movementOptions):
      yaxis(yCord)[xCord]['revealed'] = tile
      if xCord == 0 and yCord == 0:
        print('You decide you dont want to deal with this whole maze thing and leave forever. How boring.')
        break
      yCord -= 1
      yaxis(yCord)[xCord]['revealed'] = f'P{tile}'
      break
    elif move == 'R' and (' right [R]' in movementOptions):
      yaxis(yCord)[xCord]['revealed'] = tile
      xCord += 1
      yaxis(yCord)[xCord]['revealed'] = f'P{tile}'
      displayMiniMap()
      break
    elif move == 'L' and (' left [L]' in movementOptions):
      yaxis(yCord)[xCord]['revealed'] = tile
      xCord -= 1
      yaxis(yCord)[xCord]['revealed'] = f'P{tile}'
      displayMiniMap()
      break
# --- End of reveal path function --- #

mazeInfo = {}
def findInfo(tile):
  x = (int(tile[0]))
  y = (int(tile[1]))
  return yaxis(y)[x]
def test():
  displayMiniMapForTesting()
  print(mainpath)
  numberOfSplitPaths = 0
  for x in mainpath:
    mainPathRoom = yaxis(x[1])[x[0]]['roomtype']
    if 'N' in mainPathRoom:
      numberOfSplitPaths += 1
      print(mainPathRoom)
    elif mainPathRoom == 'FW':
      numberOfSplitPaths += 2
      print(mainPathRoom)
  mazeInfo['numberofSplitPaths'] = numberOfSplitPaths
  print(len(mainpath))
  print(mazeInfo['numberofSplitPaths'])
  while True:
    tile = input('Type tile coordinate as in x,y: ').split(',')
    print(findInfo(tile))
    b = input('Break? ')
    if b == 'y':
      break