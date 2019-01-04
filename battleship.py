from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)

# this creates the board
def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# this prints the winning result
# print ship_row
# print ship_col

# This is what happens in each turn
for turn in range(4):
  # get the user guesses
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))
  # winning condition
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sunk my battleship!"
    break
  # if you are not a winner, proceed
  else:
  	# condition if someone guesses something not between 0 and 4 on the board
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print "Oops, that's not even in the ocean."
    # condition if its a repeat guess
    elif(board[guess_row][guess_col] == "X"):
      print "You guessed that one already."
    # condition if its a true miss
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
      # Print (turn + 1) here!
      if turn == 3:
        print "Game Over"
    # print the board every turn
    print_board(board)

    

