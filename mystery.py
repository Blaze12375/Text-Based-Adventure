#imports global variables
import globalv
#chance function
def chance (pct):
  import random
  return random.randrange(100)<pct

def mystery():
  userinput = input("\nWhat do you do ").lower()
  #doesn't allow invalid input
  while userinput != "inven" and userinput != "go in":
    print ("I don't understand what that means")
    userinput = input("\nWhat do you do ").lower()
  #prints inventory
  while userinput == "inven":
    globalv.inven()
    userinput = input("\nWhat do you do ").lower()
  #doesn't allow invalid input
  while userinput != "inven" and userinput != "go in":
    print ("I don't understand what that means")
    userinput = input("\nWhat do you do ").lower()

  if userinput == "go in":
    #removes unnecessary items from inventory
    globalv.inventory.remove("Sword")
    globalv.inventory.remove("Shield")
    globalv.invnum -= 2
    print ("\nAs you enter the room you realise that you're carrying around a bunch of useless items\nYou drop them")
    #adds second key piece to inventory
    globalv.inventory.append("Key piece2")
    print ("\nInside of the chest was the other piece of the key")
    #ascii art for second key piece
    globalv.seckey_piece()
    print ("You stick the two pieces of the key together")
    #adds key to inventory
    globalv.inventory.append("Key")
    #removes key pieces from inventory
    globalv.inventory.remove("Key piece")
    globalv.inventory.remove("Key piece2")
    #ascii art for key
    globalv.key()
    print ("\nThe miniboss appears infront of you\nIt is charging up for a powerful attack")
    userinput = input("What do you do ").lower()
    #doesn't allow invalid input
    while userinput != "inven":
      print ("I don't understand that")
      userinput = input("\nWhat do you do ").lower()
    #prints inventory
    if userinput == "inven":
      globalv.inven()
      userinput = input("What do you do ").lower()
      #doesn't allow invalid input
      while userinput != "great sword" and userinput != "shield2" and userinput != "key":
        print ("You don't have that item")
        userinput = input("What do you do ").lower()
      #if key is typed it insults the user
      while userinput == "key":
        print ("Are you stupid?")
        userinput = input("\nWhat do you do ").lower()
      if userinput == "great sword":
        if chance(20):
          #adds legendary sword to inventory
          globalv.inventory.append("Legendary sword")
          globalv.invnum += 1
          print ("You beat the miniboss and got its sword")
          #ascii art of legendary sword
          globalv.legendary_sword()
          #removes great sword from inventory
          globalv.inventory.remove("Great sword")
          globalv.invnum -= 1
          #imports exit
          import exit
        if chance != (20):
          print ("You lose")
          #ascii art of gameover screen
          globalv.goscrn() 
      if userinput == "shield2":
        if chance(80):
          #adds legendary sword to inventory
          globalv.inventory.append("Legendary sword")
          globalv.invnum += 1
          print ("You beat the miniboss and got its sword")
          #ascii art of legendary sword
          globalv.legendary_sword()
          #removes great sword from inventory
          globalv.inventory.remove("Great sword")
          globalv.invnum -= 1
          #imports the exit
          import exit
        if chance != (80):
          print ("You lose")
          #ascii art for gameover screeb
          globalv.goscrn() 