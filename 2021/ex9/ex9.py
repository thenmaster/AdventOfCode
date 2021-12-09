import sys

if len(sys.argv) < 2:
	print("Usage: python3 ex9.py <filename>")
	quit()

filename = sys.argv[1]

with open(filename) as file:
	maze = []
	for line in file:
		maze += [list(map(lambda x: int(x), " ".join(line.strip()).split(" ")))]

total = 0
low_points = []
for i in range(len(maze)):
	for j in range(len(maze[i])):
		values = []
		if i == 0:
			values += [maze[i+1][j]]
			if j != 0:
				values += [maze[i][j-1]]
			if j != len(maze[i])-1:
				values += [maze[i][j+1]]
		elif i == len(maze)-1:
			values += [maze[i-1][j]]
			if j != 0:
				values += [maze[i][j-1]]
			if j != len(maze[i])-1:
				values += [maze[i][j+1]]
		else:
			values += [maze[i+1][j]]
			values += [maze[i-1][j]]
			if j != 0:
				values += [maze[i][j-1]]
			if j != len(maze[i])-1:
				values += [maze[i][j+1]]

		if maze[i][j] < min(values):
			total+=maze[i][j] + 1
			low_points+= [(i,j)]

print("Part 1: " + str(total))

def get_adjacent(point):
	global maze
	values = []
	i=point[0]
	j=point[1]
	if i == 0:
		values += [(i+1,j)]
		if j != 0:
			values += [(i,j-1)]
		if j != len(maze[i])-1:
			values += [(i,j+1)]

	elif i == len(maze)-1:
		values += [(i-1,j)]
		if j != 0:
			values += [(i,j-1)]
		if j != len(maze[i])-1:
			values += [(i,j+1)]
	else:
		values += [(i+1,j)]
		values += [(i-1,j)]
		if j != 0:
			values += [(i,j-1)]
		if j != len(maze[i])-1:
			values += [(i,j+1)]

	return values

sizes = []
for point in low_points:
	to_visit = [point]
	visited = set()
	while to_visit:
		current = to_visit.pop(0)
		for adjacent in get_adjacent(current):
			if maze[adjacent[0]][adjacent[1]] != 9 and adjacent not in visited:
				visited.add(adjacent)
				to_visit += [adjacent]
	sizes += [len(visited)]

sizes = sorted(sizes, reverse=True)
print("Part 2: " + str(sizes[0]*sizes[1]*sizes[2]))