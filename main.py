import random

def get_choices():
  player_choice = input ("Enter your choice (rock, paper, scissor) = ")
  options = ["rock", "paper", "scissor"]
  computer_choice = random.choice(options)
  choices = {"player" : player_choice,"computer": computer_choice}

  return choices

def check_win(player, computer):
  print("You chose " + player + "/Computer chose " + computer)
  if player==computer:
    return "It's a tie!"
    
  
  
  

