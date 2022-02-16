#stops game from running
import sys

#inventory
inventory = ["Sword", "Shield"]
#number of items in inventory
invnum = 2
#possible locations
locations = ["Exit", "Puzzle", "Mystery room", "Empty room", "Intro"]
#asks player if they want to play game again

#makes inventory not appear as a list
def inven():
  for a in inventory:
      print(a)
#makes locatations not appear as a list
def lo():
  for b in locations:
    print (b)
#possible locations to go to from intro room
def travel_intro():
  #description of the sign which has the locations writen on it
  print ("\nThere is a sign with locations on it and how to get there.")
  lo()
  loc = input("\nWhere do you go ").lower()
  #doesn't allow invalid input
  while loc != "exit" and loc != "puzzle" and loc != "mystery room" and loc != "empty room":
    print ("\nThat location does not exist")
    loc = input("\nWhere do you go ").lower()

  while loc == "exit":
    #description of room
    print ("\nThe exit is just a gate.")
    #asks user if they are sure they want to go to room
    des = input("\nAre you sure you want to go there ").lower()
    #doesn't allow invalid input
    while des != "yes" and des != "no":
      print ("I don't understand")
      des = input("\nAre you sure you want to go there ").lower()
      #if user types yes but doesn't have item, it desn't allow the user to travel to room
    if des == "yes" and inventory[invnum-1] != "Key":
      print ("You do not meet the requirements to go to this room")
      loc = input("\nWhere do you go ").lower()
      #if user types yes and meets requirements, user travels to room
    if des == "yes" and inventory[invnum-1] == "Key":
      #removes intro location so that they cannot got back
      locations.remove("Intro")
      #imports exit room
      import exit
    if des == "no":
      loc = input("\nWhere do you go ").lower()

  while loc == "mystery room":
    #description of room
    print ("\nThe only thing in the room is a wooden chest")
    #asks user if they are sure they want to go to room
    des = input("\nAre you sure you want to go there ").lower()
    #doesn't allow invalid input
    while des != "yes" and des != "no":
      print ("I don't understand")
      des = input("\nAre you sure you want to go there ").lower()
      #if user types yes but doesn't have item, it desn't allow the user to travel to room
    if des == "yes" and invnum != 5:
      print ("You do not meet the requirements to go to this room")
      loc = input("\nWhere do you go ").lower()
      #if user types yes and meets requirements, user travels to room
    if des == "yes" and invnum == 5:
      locations.remove("Intro")
      #imports mystery
      import mystery
      mystery.mystery()
    #if user types no, user has to choose another location
    if des == "no":
      loc = input("\nWhere do you go ").lower()
  
  if loc == "puzzle":
    #description of room
    print ("\nThe puzzle room has a lot of torches on the wall. \nThere is a pedestal at the centre of the room.")
    #asks user if they are sure they want to go to room
    des = input("\nAre you sure you want to go there ").lower()
    #doesn't allow invalid input
    while des != "yes" and des != "no":
      print ("I don't understand")
      des = input("\nAre you sure you want to go there ").lower()
      #if user types yes, user travels to room
    if des == "yes":
      locations.remove("Intro")
      import puzzle
      puzzle.puzzle()
    #if user types no, user has to choose another location
    if des == "no":
      loc = input("\nWhere do you go ").lower()
  
  if loc == "empty room":
    #description of room
    print ("\nThis room is very empty")
    #asks user if they are sure they want to go to room
    des = input("\nAre you sure you want to go there ").lower()
    #doesn't allow invalid input
    while des != "yes" and des != "no":
      print ("I don't understand")
      des = input("\nAre you sure you want to go there ").lower()
    if des == "yes":
      locations.remove("Intro")
      import empty
      empty.empty()
      #if user types no, user has to choose another location
    if des == "no":
      loc = input("\nWhere do you go ").lower()

#same thing as above
def travel_puzzle():
  lo()
  loc = input("\nWhere do you go ").lower()
  while loc != "exit" and loc != "puzzle" and loc != "mystery room" and loc != "empty room":
    print ("\nThat location does not exist")
    loc = input("\nWhere do you go ").lower()

  while loc == "exit":
    print ("\nThe exit is just a gate.")
    des = input("\nAre you sure you want to go there ").lower()
    while des != "yes" and des != "no":
      print ("I don't understand")
      des = input("\nAre you sure you want to go there ").lower()
    if des == "yes" and inventory[invnum-1] != "Key":
      print ("You do not meet the requirements to go to this room")
      loc = input("\nWhere do you go ").lower()
    if des == "yes" and inventory[invnum1] == "Key":
      import exit
    if des == "no":
      loc = input("\nWhere do you go ").lower()

  while loc == "mystery room":
    print ("\nThe only thing in the room is a wooden chest")
    des = input("\nAre you sure you want to go there ").lower()
    while des != "yes" and des != "no":
      print ("I don't understand")
      des = input("\nAre you sure you want to go there ").lower()
    if des == "yes" and invnum != 5:
      print ("You do not meet the requirements to go to this room")
      loc = input("\nWhere do you go ").lower()
    if des == "yes" and invnum == 5:
      import mystery
      mystery.mystery()
    if des == "no":
      loc = input("\nWhere do you go ").lower()
  
  while loc == "puzzle":
    print ("You are already here")
    loc = input("\nWhere do you go ").lower()
  
  while loc == "empty room":
    print ("\nThis room is very empty")
    des = input("\nAre you sure you want to go there ").lower()
    while des != "yes" and des != "no":
      print ("I don't understand")
      des = input("\nAre you sure you want to go there ").lower()
    if des == "yes":
      locations.remove("Puzzle")
      import empty
      empty.empty()
    if des == "no":
      loc = input("\nWhere do you go ").lower()

#same thing as above
def travel_empty():
  print ("\nThere is a sign with locations on it and how to get there.")
  lo()
  loc = input("\nWhere do you go ").lower()
  while loc != "exit" and loc != "puzzle" and loc != "mystery room" and loc != "empty room":
    print ("\nThat location does not exist")
    loc = input("\nWhere do you go ").lower()

  while loc == "exit":
    print ("\nThe exit is just a gate.")
    des = input("\nAre you sure you want to go there ").lower()
    while des != "yes" and des != "no":
      print ("I don't understand")
      des = input("\nAre you sure you want to go there ").lower()
    if des == "yes" and inventory[invnum-1] != "Key":
      print ("You do not meet the requirements to go to this room")
      loc = input("\nWhere do you go ").lower()
    if des == "yes" and inventory[invnum-1] == "Key":
      locations.remove("Empty room")
      import exit
    if des == "no":
      loc = input("\nWhere do you go ").lower()

  while loc == "mystery room":
    print ("\nThe only thing in the room is a wooden chest")
    des = input("\nAre you sure you want to go there ").lower()
    while des != "yes" and des != "no":
      print ("I don't understand")
      des = input("\nAre you sure you want to go there ").lower()
    if des == "yes" and invnum != 5:
      print ("You do not meet the requirements to go to this room")
      loc = input("\nWhere do you go ").lower()
    if des == "yes" and invnum == 5:
      locations.remove("Empty room")
      import mystery
      mystery.mystery()
    if des == "no":
      loc = input("\nWhere do you go ").lower()
  
  while loc == "puzzle":
    print ("\nThe puzzle room has a lot of torches on the wall. \nThere is a pedestal at the centre of the room.")
    des = input("\nAre you sure you want to go there ").lower()
    while des != "yes" and des != "no":
      print ("I don't understand")
      des = input("\nAre you sure you want to go there ").lower()
    if des == "yes":
      locations.remove("Empty room")
      import puzzle
      puzzle.puzzle()
    if des == "no":
      loc = input("\nWhere do you go ").lower()
  
  while loc == "empty room":
    print ("\nYou are already here")
    loc = input("\nWhere do you go ").lower()
#ascii art of gameover screen
def goscrn():
  print ("  __________         ___         _        _    _________    ")
  print (" |  ______  |       / _ \       | \      / |  |  _______|   ")
  print (" | |      |_|      / / \ \      |  \    /  |  | |_______    ")
  print (" | |    ____      / /___\ \     |   \  /   |  |  _______|   ")
  print (" | |   |___ |    /   ___   \    | |\ \/ /| |  | |           ")
  print (" | |______| |   /  /     \  \   | | \__/ | |  | |_______    ")
  print (" |__________|  /__/       \__\  |_|      |_|  |_________|   ")
  print ("                                                            ")
  print ("  __________   __         __   _________    __________      ")
  print (" |  ______  |  \ \       / /  |  _______|  |  ______  |     ")
  print (" | |      | |   \ \     / /   | |_______   | |______| |     ")
  print (" | |      | |    \ \   / /    |  _______|  |  ________|     ")
  print (" | |      | |     \ \_/ /     | |          | |   \ \        ")
  print (" | |______| |      \   /      | |_______   | |    \ \       ")
  print (" |__________|       \_/       |_________|  |_|     \_\      ")
  #stops game from running
  sys.exit()
  
#3ascii art for you win screen
def ywscrn():
  print (" __       __   __________    __      __       ")
  print (" \ \     / /  |  ______  |  |  |    |  |      ")
  print ("  \ \   / /   | |      | |  |  |    |  |      ")
  print ("   \ \ / /    | |      | |  |  |    |  |      ")
  print ("    \   /     | |      | |  |  |    |  |      ")
  print ("     | |      | |______| |  |  |____|  |      ")
  print ("     |_|      |__________|  |__________|      ")
  print ("                                              ")
  print (" __          __          __   __    __    __  ")
  print (" \ \        /  \        / /  |  |  |  \  |  | ")
  print ("  \ \      / /\ \      / /   |  |  |   \ |  | ")
  print ("   \ \    / /  \ \    / /    |  |  |    \|  | ")
  print ("    \ \  / /    \ \  / /     |  |  |  |\    | ")
  print ("     \ \/ /      \ \/ /      |  |  |  | \   | ")
  print ("      \__/        \__/       |__|  |__|  \__| ")\
#ascii art for starting sword
def sword():
  print ("       ________________ ")
  print (" [====|________________\ ")
#ascii art for great sword
def great_sword():
  print ("          ((                               ")
  print ("          ||____________________________   ")
  print (" /|-------||\___________________________\  ")
  print (" \|-------||/___________________________/  ")
  print ("          ||                               ")
  print ("          ((                               ")
#ascii art for legendary sword
def legendary_sword():
  print ("               ___                               ")
  print ("              / __\      ___                     ")
  print ("    _        / /________/  /_  ________________  ")
  print ("   / |       |H|             \/           _____\ ")
  print ("  |  |OXOXOXO|O|-------------------------|_____  ")
  print ("   \_|       |H|_________   _/\________________/ ")
  print ("             \ \___      \__\                    ")
  print ("              \___/                              ")
#ascii art for starting sword 
def shield():
  print ("    _________________   ")
  print ("   /   ||||| |||||   \  ")
  print ("  |    |\ /| |\ /|    | ")
  print ("  |    | | | | | |    | ")
  print ("  |    |/ \| |/ \|    | ")
  print ("  |____||||| |||||____| ")
  print ("  |________   ________| ")
  print ("  |     |\/| |\/|     | ")
  print ("  |     |||| ||||     | ")
  print ("  |     |/\| |/\|     | ")
  print ("   \     \|| ||/     /  ")
  print ("    \      | |      /   ")
  print ("     \_____|_|_____/    ")
#ascii art for second shield
def secshield():
  print ("   _____________     ")
  print ("  /\ \       / /\    ")
  print (" |  \ \_____/ /  |   ")
  print (" |   \  ___  /   |   ")
  print (" |   | |   | |   |   ")
  print (" |   | |   | |   |   ")
  print (" |   | |___| |   |   ")
  print ("  \  / _____ \  /    ")
  print ("   \/ /     \ \/     ")
  print ("    \/       \/      ")
  print ("     \       /       ")
  print ("      \     /        ")
  print ("       \___/         ")

#ascii art for padlock
def lock():
  print  ("    ___________    ")
  print  ("  /  _________  \  ")
  print  (" /  /         \  \ ")
  print  ("|  |           |  |")
  print  ("|__|___________|__|")
  print  ("|                 |")
  print  ("|        _        |")
  print  ("|       | |       |")
  print  ("|      |   |      |")
  print  ("|       |_|       |")
  print  ("|_________________|")
#ascii art for building
def building():
  print ('    __      _     ')
  print ('   /  \    / \    ')
  print ('  /    \  /   \   ')
  print (' /      \/     \  ')
  print ('/________\______\ ')
  print ('|               | ')
  print ('|       ___     | ')
  print ('|      |   |    | ')
  print ('|      |  0|    | ')
  print ('|______|___|____| ')
#ascii art for first piece of the key
def key_piece():
  print ("  __________  ")
  print (" /  ______  \ ")
  print ("|  /      \  |")
  print ("|  \______/  |")
  print (" \___    ___/ ")
  print ("     |  |     ")
  print ("     |  |     ")
#ascii art for the second piece of the key
def seckey_piece():
  print (" |  |__  ")
  print (" |   __| ")
  print (" |  |__  ")
  print (" |   __| ")
  print (" |__|    ")
#ascii art for the key
def key():
  print ("  __________  ")
  print (" /  ______  \ ")
  print ("|  /      \  |")
  print ("|  \______/  |")
  print (" \___    ___/ ")
  print ("     |  |     ")
  print ("     |  |     ")
  print ("     |  |__   ")
  print ("     |   __|  ")
  print ("     |  |__   ")
  print ("     |   __|  ")
  print ("     |__|     ")
#ascii art of rubick's cube
def cube():
  print ("   _ _ _     ")
  print ("  /_/_/_/\   ")
  print (" /_/_/_/\/\  ")
  print ("/_/_/_/\/\/\ ")
  print ("\_\_\_\/\/\/ ")
  print (" \_\_\_\/\/  ")
  print ("  \_\_\_\/   ")
#ascii art of pedestal
def pedestal():
  print ("     ____________                                ")
  print ("    /           /|                               ")
  print ("   /           / |                               ")
  print ("  /           /  |                               ")
  print (" /___________/   |                               ")
  print (" |           |   |                               ")
  print (" |           |   |                               ")
  print (" |           |   |                               ")
  print (" |           |   |                               ")
  print (" |           |   | <--------This is the pedestal ")
  print (" |           |   |                               ")
  print (" |           |   |                               ")
  print (" |           |   |                               ")
  print (" |           |   |                               ")
  print (" |           |  /                                ")
  print (" |           | /                                 ")
  print (" |___________|/                                  ")