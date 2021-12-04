import copy

EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."
vectors = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

def pretty_print(layout):
	for line in layout:
		print(line)
	print("====================================")

def visible_occupied(layout, pos):
	for vector in vectors:
		x = pos[1]
		y = pos[0]
		while 0 <= y <= len(layout)-1 and 0 <= x <= len(layout[0])-1:
			if layout[y][x] != FLOOR and not (y == pos[0] and x == pos[1]):
				if layout[y][x] == OCCUPIED:
					return True
				else:
					break
			x += vector[0]
			y += vector[1]

	return False

def count_visible_occupied(layout, pos):
	count = 0
	for vector in vectors:
		x = pos[1]
		y = pos[0]

		while 0 <= y <= len(layout)-1 and 0 <= x <= len(layout[0])-1:
			if layout[y][x] != FLOOR and not (y == pos[0] and x == pos[1]):
				if layout[y][x] == OCCUPIED:
					count += 1
					if count == 5:
						return True
				break
			x += vector[0]
			y += vector[1]

	return False

current = []
new = []

with open("input.txt", "r") as f:
	for l in f.readlines():
		current += [[c for c in l.strip()]]

while True:
	new = copy.deepcopy(current)

	for i in range(len(current)):
		for j in range(len(current[i])):
			if current[i][j] == EMPTY and not visible_occupied(current, (i,j)):
				new[i][j] = OCCUPIED

			if current[i][j] == OCCUPIED and count_visible_occupied(current, (i,j)):
				new[i][j] = EMPTY

	# pretty_print(current)
	# pretty_print(new)
	# input()
	if new == current:
		break

	current = new

print([item for sub in current for item in sub].count(OCCUPIED))