from random import randint
board = []
for x in range(5):
	board.append(["O"] * 5)
def print_board(board):
	for row in board:
		print " ".join(row)
def random_row(board):
	return randint(0, len(board[0]) - 1)
def no_input(guess_row,guess_col):
	(not guess_row) or (not guess_col)
def random_col(board):
	return randint(0, len(board[0]) - 1)
def hit(guess_row,row,guess_col,col):
	return (guess_row == row) and (guess_col == col)
def already(y):
	return y == 'X'
def outside(guess_row,guess_col):
	return (guess_row > 4 or guess_row < 0) or (guess_col > 4 or guess_col < 0)
ship_row = random_row(board)
ship_col = random_col(board)
print "Let's play Battleship!"
print_board(board)
for turn in range(4):
	print "You get four turns. This is Turn " + str(turn + 1) +"."
	raw_guess_row = raw_input("Guess a row, 1-5: ")
	raw_guess_col = raw_input("Guess a column, 1-5: ")
	while not raw_guess_row or not raw_guess_col:
		raw_guess_row = raw_input("I need a row and column, dumbo. Guess a row, 1-5: ")
		raw_guess_col = raw_input("And now a column, 1-5: ")
	guess_col = int(raw_guess_col)-1
	guess_row = int(raw_guess_row)-1
	if outside(guess_row,guess_col):
		print "That's not in the ocean, dumbo."
		print_board(board)
	elif already(board[guess_row][guess_col]):
		print "You already guessed there..."
		print_board(board)
	elif hit(guess_row,ship_row,guess_col,ship_col):
		print "You sunk my battleship! You monster. Thousands died."
		board[guess_row][guess_col] = '*'
		print_board(board)
		break
	else:
		print "You missed my battleship. Try again (if you can)."
		board[guess_row][guess_col] = 'X'
		print_board(board)
if turn == 3:
	print "You had four goes. It's game over for you, loser."
