import sys

class Line(object):
	"""docstring for Line"""
	def __init__(self):
		super(Line, self).__init__()
		self.content = []

	def add_value(self,value: int):
		self.content += [value]

	def get_length(self):
		return len(self.content)

	def get_value(self, i: int):
		return self.content[i]

	def mark_value(self,value: int):
		self.content = list(map(lambda x: 'X' if x == value else x, self.content))

	def is_full(self):
		return len(list(filter(lambda x: x != 'X', self.content))) == 0

	def get_sum(self):
		return sum(list(filter(lambda x: x != 'X', self.content)))

	def __str__(self):
		return str(self.content)

class Board(object):
	"""docstring for Board"""
	def __init__(self):
		super(Board, self).__init__()
		self.lines = []
		
	def add_line(self, line: Line):
		self.lines+=[line]

	def mark_value(self, value: int):
		for line in self.lines:
			line.mark_value(value)

	def is_winner(self):
		for line in self.lines:
			if line.is_full():
				return True
		for i in range(self.lines[0].get_length()): # check columns
			column = [x.get_value(i) for x in self.lines]
			if len(list(filter(lambda x: x != 'X', column)))==0:
				return True

	def get_sum_unmarked(self):
		total = 0
		for line in self.lines:
			total+=line.get_sum()
		return total

	def __str__(self):
		return "Board\n"+ "".join(map(lambda x: str(x)+"\n", self.lines))

Plays = list[int]

class Game(object):
	"""docstring for Game"""
	def __init__(self, plays: Plays):
		super(Game, self).__init__()
		self.plays = plays
		self.boards = []
	
	def add_board(self, board: Board):
		self.boards+=[board]


	def play(self):
		for play in self.plays:
			self.last_play = play
			for board in self.boards:
				board.mark_value(play)
				if board.is_winner():
					return board

	def play_until_last(self):
		for play in plays:
			self.last_play = play
			next_round=[]
			for board in self.boards:
				board.mark_value(play)
				if board.is_winner():
					if len(self.boards) == 1: #last board
						return board
					continue #if won and isn't last, don't include in next round
				next_round+=[board]
			self.boards=next_round

	def get_last_play(self):
		return self.last_play

	def __str__(self):
		return "Game Plays:" + str(self.plays) + "\n" +  "".join(map(lambda x: str(x)+"\n", self.boards))


if len(sys.argv) < 2:
	print("Usage: python3 ex4.py <filename>")
	quit()

filename = sys.argv[1]

#parse input
with open(filename) as file:
	plays = list(map(lambda x: int(x), file.readline().strip().split(",")))
	game = Game(plays)

	file.readline()

	board = Board()
	for line in file:
		if len(line.strip()) == 0:
			game.add_board(board)
			board = Board()
			continue
		game_line = Line()

		processed = list(filter(lambda x: x != "", line.strip().split(" ")))
		for value in list(map(lambda x: int(x), processed)):
			game_line.add_value(value)
		board.add_line(game_line)

winner = game.play()

print("Sum: " + str(winner.get_sum_unmarked()))
print("Last play: " + str(game.get_last_play()))
print("Part 1: " + str(winner.get_sum_unmarked()*game.get_last_play()))

print() #Just for spacing

#re-parse input because we wrote over it on the first run
with open(filename) as file:
	plays = list(map(lambda x: int(x), file.readline().strip().split(",")))
	game = Game(plays)

	file.readline()

	board = Board()
	for line in file:
		if len(line.strip()) == 0:
			game.add_board(board)
			board = Board()
			continue
		game_line = Line()

		processed = list(filter(lambda x: x != "", line.strip().split(" ")))
		for value in list(map(lambda x: int(x), processed)):
			game_line.add_value(value)
		board.add_line(game_line)

last_winner = game.play_until_last()

print("Sum: " + str(last_winner.get_sum_unmarked()))
print("Last play: " + str(game.get_last_play()))
print("Part 2: " + str(last_winner.get_sum_unmarked()*game.get_last_play()))