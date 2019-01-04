print("""In this project, we'll build Rock-Paper-Scissors!""")

from random import randint 

option = ["ROCK", "PAPER", "SCISSORS"]

message = {
  "tie" : "Yawn it's a tie!",
  "won" : "Yay you won!",
  "lost" : "Aww you lost!"
}

# User: Rock, Computer: Scissors
# User: Paper, Computer: Rock
# User: Scissors, Computer: Paper

def decide_winner(user_choice, computer_choice):
  print("You selected: %s" % user_choice)
  print("Computer selected: %s" % computer_choice)
  if user_choice == computer_choice:
    print(message["tie"])
  elif user_choice == option[0] and computer_choice == option[2]:
    print(message["won"])
  elif user_choice == option[1] and computer_choice == option[0]:
  	print(message["won"])
  elif user_choice == option[2] and computer_choice == option[1]:
  	print(message["won"])
  else:
  	print(message["lost"])

def play_RPS():
  user_choice = raw_input("Enter Rock, Paper, or Scissors: ")
  user_choice = user_choice.upper()
  computer_choice = option[randint(0,2)]
  decide_winner(user_choice, computer_choice)

play_RPS()