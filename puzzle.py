#imorts global variables
import globalv
#chance function
def chance (pct):
  import random
  return random.randrange(100)<pct
  
def puzzle():
  #ascii art of pedestal
  globalv.pedestal()
  userinput = input("\nWhat do you do ").lower()
  #doesn't allow invalid input
  while userinput != "inven" and userinput != "go in":
    print ("I don't understand that")
    userinput = input("\nWhat do you do ").lower()
    
  while userinput == "inven":
    #prints inventory
    globalv.inven()
    userinput = input("\nWhat do you do ").lower()
  #doesn't allow invalid input
  while userinput != "go in":
    print ("I don't understand that")
    userinput = input("\nWhat do you do ").lower()
  if userinput == "go in":
    print ("On the pedestal there is rubik's cube")
    if chance(70):
      #ascii art of rubick's cube
      globalv.cube()
      #adds key piece to inventory
      globalv.inventory.append("Key piece")
      globalv.invnum += 1
      print ("\nYou solved the rubik's cube and got a piece of the key as a reward")
      #ascii art of key piece
      globalv.key_piece()
      #allows player to travel to any available room
      globalv.travel_puzzle()
    if chance != (70):
      #ascii art of rubick's cube
      globalv.cube()
      print ("\nYou didn't solve the cube so you were blown up")
      #ascii art of gameover screen
      globalv.goscrn() 