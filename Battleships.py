# Import modules
from random import randint
from time import sleep

# Setting up board as a list
board = []

# Generating a board of 5x5 "O"s
for x in range(5):
  board.append(["O"] * 5)

# Making a nice print function for the board
def print_board(board):
  for row in board:
    print (" ".join(row))
    # .join removes python punctuation and separates Os with a space

# functions to create a random initial position
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

# Set incitial ships sunk
ships_sunk = 0

# place ships on board
ship1_row = random_row(board)
ship1_col = random_col(board)
ship2_row = random_row(board)
ship2_col = random_col(board)

# make sure ships aren't at the same place
if ship1_row == ship2_row and ship1_col == ship2_col:
  ship2_row = random_row(board)
  ship2_col = random_col(board)

# welcome to the game
print ("Hullo folks!")
print ("Two ships (1x1) are hidden in a 5x5 grid.")
print ("You have ten guesses to find them.")
print ("Missed shots will show as X on the board.")
print ("Sunk ships will show as S")

# While loop for many turns
play_again="y"
while play_again=="y":

  # Print ship positions to console for debugging
  cheat = input("Do you want to know where the ships are? (y/n):")
  if cheat == "y":
    sleep(1)
    print ("Ship 1 is at row %d column %d." % (ship1_row+1, ship1_col+1))
    print ("Ship 2 is at row %d column %d." % (ship2_row+1, ship2_col+1))
    print()

  # Loop for each turn. Print the board and ask for the user's guess.
  for turn in range(10):
    sleep(1)
    print ("Turn %d/10" % (turn + 1))
    print_board(board)
    # Player input
    guess_row = int(input("Guess Row (1-5): "))-1
    guess_col = int(input("Guess Col (1-5): "))-1
  
    # If player hits a ship:
    if (guess_row == ship1_row and guess_col == ship1_col and board[guess_row][guess_col]=="O")\
    or (guess_row == ship2_row and guess_col == ship2_col and board[guess_row][guess_col]=="O"):
      sleep(1)
      print()
      print ("Kaboooom! Direct hit!")
      # Update the board with "S" for sunk ship
      board[guess_row][guess_col] = "S"
      ships_sunk = ships_sunk + 1
      # Message regarding remaining number of ships, and end of game cases
      if ships_sunk == 1:
        print ("Got one! One more to go....")
      if turn == 9:
        print ("... but you're out of turns! Game Over")
        print ("Ship 1 was at row %d column %d." % (ship1_row+1, ship1_col+1))
        print ("Ship 2 was at row %d column %d." % (ship2_row+1, ship2_col+1))
      else:  
        print()
      if ships_sunk == 2:
        print ("And that's the other! The ocean is now safe.")
        print_board(board)
        break
  
    # If player misses
    else:
      # Guess out of range
      if guess_row >= 5 or guess_row < 0 or guess_col >= 5 or guess_col <0:
        sleep(1)
        print ("You spanner, that's not even on the board.")
        print ()
      # User enters a position already guessed
      elif(board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "S"):
        sleep(1)
        print ("You guessed that one already.")
        print()
      # Player misses
      else:
        sleep(1)
        print()
        print ("Splash! Missed.")
        print()
        board[guess_row][guess_col] = "X"

# End of game
      if turn==9:
        if ships_sunk == 0:
          print ("Bad luck, you didn't hit a thing!")
        if ships_sunk == 1:
          print ("Not bad, you got one of them!")
        print ("Ship 1 was at row %d column %d." % (ship1_row+1, ship1_col+1))
        print ("Ship 2 was at row %d column %d." % (ship2_row+1, ship2_col+1))
        print ("Game Over")
  print()
  print ("Do you want to play again?")
  play_again = input("(y/n)")