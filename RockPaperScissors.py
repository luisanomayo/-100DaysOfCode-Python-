import random 

#game intro
print ("Rock Paper Scissors\n")


#game art/symbols
rock = "O"
paper = "[]"
scissors = "✄"

print (" " + rock + "    "+ paper + "     " + scissors + "\n")

#store all the play options in a list for random picks for the computer
game_options = ["rock","paper","scissors"]
game_art = [rock,paper,scissors]

limit = len(game_options) - 1

#set the plays
player_move = input("Welcome Player. Rock, Paper, or Scissors?:").lower()
index = game_options.index (player_move)

computer_play = game_options[random.randint(0, limit)]
comp_index = game_options.index(computer_play)

#show the player choices
print (game_art[index] + "  vs. " + game_art[comp_index])


#the game rules
if player_move == "rock" and computer_play == "scissors":
  print ("Rock beats Scissors. You Win!")
  
elif player_move == "scissors" and computer_play == "paper":
  print ("Scissors beats Paper. you Win!")
  
  
elif player_move =="paper" and computer_play == "rock":
  print ("Paper beats Rock. You Win!")

elif player_move == computer_play:
  print ("It's draw! Restart the game.")

else:
  print (f"{computer_play.upper()} beats {player_move.upper()}. You Lose! Try Again")
  
  
  

  

