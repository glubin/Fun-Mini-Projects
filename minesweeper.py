import random
import sys

cols = int(raw_input("Columns: "))
rows = int(raw_input("Rows: "))
prob_of_bomb = float(raw_input("Decimal Probability of Bomb: "))

board = [[0 for x in xrange(rows+2)] for x in xrange(cols+2)]
num_board = board = [[0 for x in xrange(rows+2)] for x in xrange(cols+2)]


for i in range(len(board)):
	for j in range(len(board[i])):
		r = random.random()
		bomb = r < prob_of_bomb
		if bomb == True:
			board[i][j] = "*"
		else:
			board[i][j] = "."
		if i == 0 or j == 0 or j == rows+1 or i == cols+1:
			board[i][j] = "-"

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in board]))

