#imports global variables
import globalv
#chance function
def chance (pct):
  import random
  return random.randrange(100)<pct

def empty():
  userinput = input("\nWhat do you do ").lower()
  #doesn't allow invalid input
  while userinput != "inven" and userinput != "go in":
    print ("I don't understand that")
    userinput = input("\nWhat do you do ").lower()
#prints inventory
  while userinput == "inven":
    globalv.inven()
    userinput = input("\nWhat do you do ").lower()
#doesn't allow invalid input
  while userinput != "go in":
    print ("I don't understand that")
    userinput = input("\nWhat do you do ").lower()

  if userinput == "go in":
    if chance(49):
      print ("\nAn enemy materializes infront of you. \nIt plans to defend with a Shield")
      userinput = input("\nWhat do you do ").lower()
      #doesn't allow invalid input
      while userinput != "inven":
        print ("\nI don't understand that")
        userinput = input("\nWhat do you do ").lower()
      #prints inventory
      if userinput == "inven":
        globalv.inven()
        userinput = input("\nWhat do you do ").lower()
      #doesn't allow invalid input
      while userinput != "sword" and userinput != "shield" and userinput != "great sword" and userinput != "inven":
        print ("You do not have that item")
        userinput = input("\nWhat do you do ").lower()

      if userinput == "sword":
        if chance(30-20):
          globalv.sword()
          print ("\nYou win")
          #adds shield2 to inventory
          globalv.inventory.append("Shield2")
          globalv.invnum += 1
          print ("\nYou got another shield that's better than your current one")
          #ascii art of second shield
          globalv.secshield()
          #allows user to travel to different rooms
          globalv.travel_empty()
        if chance != (10):
          globalv.sword()
          print ("\nYou lose")
          #ascii art of gameover screen
          globalv.goscrn()
      if userinput == "shield":
        if chance(30+30):
          globalv.shield()
          print ("\nYou win")
          #adds shield2 to inventory
          globalv.inventory.append("Shield2")
          globalv.invnum += 1
          print ("\nYou got another shield that's better than your current one")
          #ascii art of second shield
          globalv.secshield()
          #allows user to travel to different rooms
          globalv.travel_empty()
        if chance != (60):
          globalv.shield()
          print ("\nYou lose")
          #ascii art of gameover screen
          globalv.goscrn()
      if userinput == "great sword":
        if chance(60-20):
          globalv.great_sword()
          print ("\nYou win")
          #adds shield2 to inventory
          globalv.inventory.append("Shield2")
          globalv.invnum += 1
          print ("\nYou got another shield that's better than your current one")
          #ascii art of second shield
          globalv.secshield()
          #allows user to travel to different rooms
          globalv.travel_empty()
        if chance != (40):
          globalv.great_sword()
          print ("\nYou lose")
          #ascii art of gameover screen
          globalv.goscrn()
    else:
      #adds shield2 to inventory
      globalv.inventory.append("Shield2")
      globalv.invnum += 1
      print ("You find another shield which is better than your current one")
      #ascii art of second shield
      globalv.secshield()
      #allows user to travel to different rooms
      globalv.travel_empty()