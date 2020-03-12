# Крестики-нолики

import random

def drawBoard(board):
	# Эта функция выводит на экран игровое поле, клетки которого будут заполняться.

	# "board" - это список из 10 строк, для прорисовки игрового поля (индекс 0 игнорируестя).
	print(board[7] + '|' + board[8] + '|' + board[9])
	print('-+-+-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-+-+-')
	print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
	# Разрешение игроку ввести букву, которую он выбирает.
	# Возвращает список, в котором буква игрока - первый элемент, а буква компьютер - второй.
	letter = ''
	while not (letter == 'X' or letter == 'O'):
		print('Вы выбираете X или O?')
		letter = input().upper()

	# Певрым элементом списка является буква игрока, вторым - буква компьютера.
	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']

def whoGoesFirst():
	# Случайнный выбор игрока, который ходит первым.
	if random.randit(0, 1) == 0:
		return 'Компьютер'
	else:
		return 'Человек'

def makeMove(board, letter, move):
	board[move] = letter

def isWinner(bo, le):
	# Учитывая заполнение игрового поля и буквы игрока, эта функция возвращает True, если игрок выиграл.
	# Мы используем "bo" вместо "board" и "le" вместо "letter", поэтому нам не нужно много печатать.
	return ((bo[7] == le and bo[8] == le and bo[9] == le) or # через верх
	(bo[4] == le and bo[5] == le and bo[6] == le) or # через центр
	(bo[1] == le and bo[2] == le and bo[3] == le) or # через низ 
	(bo[7] == le and bo[4] == le and bo[1] == le) or # вниз по левой стороне
	(bo[8] == le and bo[5] == le and bo[2] == le) or # вниз по центру
	(bo[9] == le and bo[6] == le and bo[3] == le) or # вниз по правой стороне
	(bo[7] == le and bo[5] == le and bo[3] == le) or # по диагонали
	(bo[9] == le and bo[5] == le and bo[1] == le)) # по диагонали 

def getBoardCopy(board):
	# Создает копию игрового поля и возвращает его.
	boardCopy = []
	for i in board:
		boardCopy.append(i)
	return boardCopy

def isSpaceFree(board,move):
	# Возвращает True, сли сделан ход в свободную клетку.
	return board[move] == ' '

def getPlayerMove(board):
	# Разрешение игроку сделать ход.
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
		print('Ваш следующий ход? (1-9)')
		move = input()
	return int(move)

def chooseRandomMoveFromList (board, movesList):
	#
	#
	possibleMoves = []:
	for i in movesList:
		if isSpaceFree (board, i):
			possibleMoves.append(i)

	if len(possibleMoves) != 0:
		return random.choice(possibleMoves)
	else:
		return None 

def getComouterMove (board, computerLetter):
	#
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

