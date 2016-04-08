from random import randint									#pull the functionality for random numbers	
board = []											#the original blank board as a list
for x in range(5):										#create 5 x 5 Os for the proper board
	board.append(["O"] * 5)
def print_board(board):										#print it pretty, without []s or ,s
	for row in board:
		print " ".join(row)
def random_row(board):										#use the randint fn to create a battleship location
	return randint(0, len(board[0]) - 1)
def random_col(board):
	return randint(0, len(board[0]) - 1)
def hit(guess_row,row,guess_col,col):								#define sinking a ship
	return (guess_row == row) and (guess_col == col)
def already(y):											#define hitting the same place twice
	return y == 'X'
def outside(guess_row,guess_col):								#define hitting outside the board
	return (guess_row > 4 or guess_row < 0) or (guess_col > 4 or guess_col < 0)
ship_row = random_row(board)									#defining the ship's coords
ship_col = random_col(board)
print "Let's play Battleship!"
print_board(board)										#print the board for the player
for turn in range(4):										#four turns. Each turn goes like this:
	print "You get four turns. This is Turn " + str(turn + 1) +"."				#corrects the Python index style and tells the player how many turns are left
	raw_guess_row = raw_input("Guess a row, 1-5: ")						#coords as a string
	raw_guess_col = raw_input("Guess a column, 1-5: ")
	while not raw_guess_row or not raw_guess_col:						#checks if the coords are blank
		raw_guess_row = raw_input("I need a row and column, dumbo. Guess a row, 1-5: ")	#tells the player to
		raw_guess_col = raw_input("And now a column, 1-5: ")				#\re-enter their coords
	guess_col = int(raw_guess_col)-1							#changes the coords to ints
	guess_row = int(raw_guess_row)-1							#-1 aligns the guesses with the Python index style
	if outside(guess_row,guess_col):							#if outside print this (see ln.16)
		print "That's not in the ocean, dumbo."
		print_board(board)
	elif already(board[guess_row][guess_col]):						#if already print this (see ln.14)
		print "You already guessed there..."						#note how 'board' not cited in def
		print_board(board)
	elif hit(guess_row,ship_row,guess_col,ship_col):					#if hit print this (see ln.12)
		print "You sunk my battleship! You monster. Thousands died."
		board[guess_row][guess_col] = '*'						#changes the hit coord to a *
		print_board(board)
		break										#break is so if you win, game over
	else:
		print "You missed my battleship. Try again (if you can)."			#it's hard to define 'missed',
		board[guess_row][guess_col] = 'X'						#so it's the 'else' function.
		print_board(board)
if turn == 3:											#note Python index
	print "You had four goes. It's game over for you, loser."
