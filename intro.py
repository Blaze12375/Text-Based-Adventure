#imports global variables
import globalv
#chance function
def chance (pct):
  import random
  return random.randrange(100)<pct
#tells player how to win the game
print ("\nYour objective is to escape by finding a key which looks like this")
globalv.key()
userinput = input("\nWhat do you do ").lower()
def Intro(userinput):
  #doesn't allow invalid input
  while userinput != "inven" and userinput != "look around":
    print ("I don't understand what that means")
    userinput = input("\nWhat do you do ").lower()
  while userinput == "inven":
    #prints inventory
    globalv.inven()
    userinput = input("\nWhat do you do ").lower()
  #doesn't allow invalid input
  while userinput != "look around":
    print ("I don't understand what that means")
    userinput = input("\nWhat do you do ").lower()
  #tells player description
  if userinput == "look around":
    print ("\nYou seem to be in a hallway. At the end of the hallway you see an abandoned house.")
    #ascii art for building
    globalv.building()
    userinput = input("\nWhat do you do ").lower()
    #doesn't allow invalid input
    while userinput != "go in" and userinput != "inven":
      print ("\nI don't understand that")
      userinput = input("\nWhat do you do ").lower()
    if userinput == "inven":
      #prints inventory
      globalv.inven()
      userinput = input("\nWhat do you do ").lower()
    #doesn't allow invalid input
    while userinput != "go in":
      print ("I don't understand what that means")
      userinput = input("\nWhat do you do ").lower()
    if userinput == "go in":
      if chance(60):
        #battle starts when chance is 60
        print ("\nYou have run into an enemy. \nIt plans to attack with a Great sword.")
        userinput = input("\nWhat do you do ").lower()
        #tells player they can't run
        while userinput == "run":
          print ("\nYou can't. \nThis isn't pokemon.")
          userinput = input("\nWhat do you do ").lower()
          #doesn't allow invalid input
        while userinput != "inven":
          print ("\nI don't understand that")
          userinput = input("\nWhat do you do ").lower()
        if userinput == "inven":
          #prints inventory
          globalv.inven()
          userinput = input("\nWhat do you do ").lower()
        #doesn't allow invalid input
        while userinput != "sword" and userinput != "shield":
          print ("You do not have that item")
          userinput = input("\nWhat do you do ").lower()
        if userinput == "sword":
          if chance(30):
            #ascii art for sword
            globalv.sword()
            print ("\nYou win")
            #adds great sword to inventory
            globalv.inventory.append("Great sword")
            globalv.invnum += 1
            print ("\nYou got a Great sword")
            #ascii art for great sword
            globalv.great_sword()
            #allows player to chance locations
            globalv.travel_intro()
          else:
            #ascii art for sword
            globalv.sword()
            print ("\nYou lose")
            #ascii art for gameover screen
            globalv.goscrn()
        if userinput == "shield":
          if chance(30+40):
            #ascii art for shield
            globalv.shield()
            print ("\nYou win")
            #adds great sword to inventory
            globalv.inventory.append("Great sword")
            globalv.invnum += 1
            print ("\nYou got a Great sword")
            #ascii art for great sword
            globalv.great_sword()
            #allows player to travel
            globalv.travel_intro()
          else:
            #ascii art for shield
            globalv.shield()
            print ("\nYou lose")
            #gameover screen
            globalv.goscrn()
      else:
        #adds great sword to inventory
        globalv.inventory.append("Great sword")
        globalv.invnum += 1
        print ("\nYou found a Great sword")
        #ascii art for great sword
        globalv.great_sword()
        #allaws user to change locations
        globalv.travel_intro()
Intro(userinput)       