import globalv
def Tut():
  #tells player what to do
  print ("\nType inven to access your inventory  \n(Type skip to skip the tutorial)")
  userinput = input("").lower()
  #doesn't allow invalid input to be entered
  while userinput != "skip" and userinput != "inven" and userinput != "yes":
    print ("I don't understand that")
    userinput = input("").lower()
  #allows player to skip the tutorial
  if userinput == "skip":
    import main
  #teaches character the commands
  if userinput == "inven":
    #prints inventory
    globalv.inven()
    print ("\nNow type go in \nThis allows you to go into rooms")
    userinput = input("").lower()
    while userinput != "go in":
      print ("I don't understand that")
      userinput = input("").lower()
    if userinput == "go in":
      print ("\nGood job. \nNow type inven then sword to use it")
      userinput = input("").lower()
      #doesn't allow invalid input
      while userinput != "inven":
        print ("I don't understand that")
        userinput = input("").lower()
      if userinput == "inven":
        globalv.inven()
        userinput = input("").lower()
        #doesn't allow invalid input
      while userinput != "sword":
        print ("I don't know what that means")
        userinput = input("").lower()
      if userinput == "sword":
        #ascii art for starting sword
        globalv.sword()
        print ("Now type shield")
        userinput = input("").lower()
        #doesn't allow invalid input
        while userinput != "shield":
          print ("I don't understand what that means")
          userinput = input("").lower()
        if userinput == "shield":
          #ascii art for starting shield
          globalv.shield()
          #teaches character that items can only be used in certain events
          print ("\nYou have completed the tutorial. \nNote: You can only use items during certain events that require them. For example, you can \nonly use your sword and shield when attacked.")
Tut()