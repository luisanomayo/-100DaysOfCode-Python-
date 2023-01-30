print("""
               ,     \    /      ,
              / \    )\__/(     / \
             /   \  (_\  /_)   /   \
____________/_____\__\@  @/___/_____\___________
|                    |\../|                    |
|                     \VV/                     |
|                 TREASURE HUNT                |
|                                              |
|______________________________________________|
        |    /\ /      \\       \ /\    |
        |  /   V        ))       V   \  |
        |/     `       //        '     \|
        
        """)



print ("Your mission is to find the treasure.\n\n")



choice_1 = input("You're setting off on your quest.\nWhere do you go? left or right?").lower()
result = "you fell into the dragon's pit. GAME OVER!\n"
if choice_1 != "left":
  print(result)
else:
  print ("\nYou're still on the quest")
  choice_2 = input("You've come to a lake. Do you go swim or wait for rescue?").lower()
  if choice_2 != "swim":
    result = "\nthe dragon found you idly by the lakeside and burned you. GAME OVER!"
    print (result)
  else:
    print ("\nGood! You're still on the quest. \nYou've swam to the other side of the lake.")
    choice_3 = input("\nThere is a castle with three doors.\nWhich door do you go through? The Red door, The Yellow door or the Blue door?\nEnter only the colour of the door: ").lower()
    if choice_3 != "yellow":
      result = "\nYou picked the wrong door and ran into a dragon. GAME OVER!"
      print (result)
    else:
      result = "\nYou've found the treasure. You completed the game. HURRAY!!!"
      print (result)
      print ("""
      
               __________
              /\____;;___\
             | /         /
             `. ())oo() .
              |\(%()*^^()^\
             %| |-%-------|
            % \ | %  ))   |
            %  \|%________|
            
      """)


