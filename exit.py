#imports global variables
import globalv
def exit():
  #description of room
  print ("\nThere is an indestructible padlock on it which requires a key to open.")
  #ASCII art for a padlock
  globalv.lock()
  #asks the user for input
  userinput = input("\nWhat do you do ").lower()
  #if user enters invalid input, the program asks them for the correct input
  while userinput != "inven":
    print ("\nI don't understand that")
    userinput = input("\nWhat do you do ").lower()
  #prints inventory when inven is typed
  if userinput == "inven":
    globalv.inven()
    userinput = input("\nWhat do you do ").lower()
    #doesn't allow invalid input
    while userinput != "key":
      print ("You can't use this item for this event")
      userinput = input("\nWhat do you do ").lower()
    #starts boss fight when key is typed
    if userinput == "key":
      globalv.inventory.remove("Key")
      globalv.invnum -= 1
      import boss
      boss.boss()
exit()