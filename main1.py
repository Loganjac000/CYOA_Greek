from os import system
from time import sleep
from random import randint
import maze_info
import all_rooms
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
maze_info.createMaze()
# ---------------------------------------------------------------------- #
# This is the testing zone
while True:
  maze_info.revealPath()

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