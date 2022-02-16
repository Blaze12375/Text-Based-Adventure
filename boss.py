#imports global variables
import globalv
#stops game
import sys

#chance function
def chance (pct):
  import random
  return random.randrange(100)<pct

def boss():
  #sets the boss' lives to 2
  bosslives = 2
  print ("\nYou approach the boss\nThe boss is blocking the path to the exit\nThe boss is preparing to attack\nUnlike the other enemies the boss has two lives")
  userinput = input("\nWhat do you do ").lower()
  #doesn't allow inavlid input
  while userinput != "inven":
    print ("I don't understand that")
    userinput = input("\nWhat do you do ").lower()
  #prints inventory
  if userinput == "inven":
    globalv.inven()
    userinput = input("\nWhat do you do ").lower()
    #doesn't allow inavlid input
    while userinput != "legendary sword" and userinput != "shield2":
      print ("I don't understand that")
      userinput = input("\nWhat do you do ").lower()
    
    if userinput == "legendary sword":
      if chance(20):
        #ascii art for legendary sword
        globalv.legendary_sword()
        bosslives -= 1
        print ("The boss is too tired to do anything")
        userinput = input("\nWhat do you do ").lower()
        #doesn't allow inavlid input
        while userinput != "inven":
          print ("I don't understand that")
          userinput = input("\nWhat do you do ").lower()
        #prints inventory
        if userinput == "inven":
          globalv.inven()
          userinput = input("\nWhat do you do ").lower()
          while userinput != "legendary sword" and userinput != "shield2":
            print ("I don't understand that")
            userinput = input("\nWhat do you do ").lower()

          if userinput == "legendary sword":
            if chance(80):
              #ascii art of legendary sword
              globalv.legendary_sword()
              print ("The boss is now defending")
              userinput = input("\nWhat do you do ").lower()
        
          if userinput == "shield2":
            if chance(20):
              #ascii art for second shield
              globalv.secshield()
              print ("The boss is now defending")
              userinput = input("\nWhat do you do ").lower()
              #doesn't allow inavlid input
              while userinput != "legendary sword" and userinput != "shield2":
                print ("I don't understand that")
                userinput = input("\nWhat do you do ").lower()

              if userinput == "legendary sword":
                if chance(20):
                  #ascii art for legendary sword
                  globalv.legendary_sword()
                  #ascii art for you win screen
                  globalv.ywscrn()
                  #stops game
                  sys.exit()

                if chance != (20):
                  #ascii art for legendary sword
                  globalv.legendary_sword()
                  print ("You lose")
                  #ascii art for gameover screen
                  globalv.goscrn()

              if userinput == "shield2":
                if chance(80):
                  #ascii art for second shield
                  globalv.secshield()
                  #ascii art for you win screen
                  globalv.ywscrn()
                  #stops game
                  sys.exit()
              
                if chance != (80):
                  #ascii art for second shield
                  globalv.secshield()
                  print ("You lose")
                  #ascii art for gameover screen
                  globalv.goscrn()

            if chance != (20):
              #ascii art for second shield
              globalv.secshield()
              print ("You lose")
              #ascii art for gameover screen
              globalv.goscrn()

      if chance != (20):
        #ascii art for legendary sword
        globalv.legendary_sword()
        print ("You lose")
        #ascii art for gameover screen
        globalv.goscrn()
        

    if userinput == "shield2":
      if chance(80):
        #ascii art for second shield
        globalv.secshield()
        bosslives -= 1
        print ("The boss is too tired to do anything")
        userinput = input("\nWhat do you do ").lower()
        #doesn't allow invalid input
        while userinput != "inven":
          print ("I don't understand that")
          userinput = input("\nWhat do you do ").lower()

        if userinput == "inven":
          #prints inventory
          globalv.inven()
          userinput = input("\nWhat do you do ").lower()
          #doesn't allow invalid input
          while userinput != "legendary sword" and userinput != "shield2":
            print ("I don't understand that")
            userinput = input("\nWhat do you do ").lower()

          if userinput == "legendary sword":
            if chance(80):
              #ascii art for legendary sword
              globalv.legendary_sword()
              print ("You win")
              #ascii art for you win screen
              globalv.ywscrn()
              #stops game
              sys.exit()

            if chance != (80):
              #ascii art for legendary sword
              globalv.legendary_sword()
              print ("You lose")
              #ascii art for gameover screen
              globalv.goscrn()
        
          if userinput == "shield2":
            if chance(20):
              #ascii art for second shield
              globalv.secshield()
              print ("You win")
              #ascii art you win screen
              globalv.ywscrn()
              #stops game
              sys.exit()

            if chance != (20):
              #ascii second shield
              globalv.secshield()
              print ("You lose")
              #ascii art for gameover
              globalv.goscrn()