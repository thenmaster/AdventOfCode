import sys

if len(sys.argv) < 2:
	print("Usage: python3 ex11.py <filename>")
	quit()

filename = sys.argv[1]

with open(filename) as file:
	lines = []
	for line in file:
		lines += [list(map(lambda x: int(x), " ".join(line.strip()).split(" ")))]

def get_adjacent(point):
	global lines
	i=point[0]
	j=point[1]
	points = [(i+1,j),(i,j+1),(i-1,j),(i,j-1),(i+1,j+1),(i+1,j-1),(i-1,j+1),(i-1,j-1)]
	points = list(filter(lambda x: 0<=x[0]<=len(lines)-1 and 0<=x[1]<=len(lines[0])-1, points))
	return points

# print("Start")
# for line in lines:
# 	print("".join(list(map(lambda x: str(x), line))))
# print("============================")

total = 0
for x in range(100):
	# Step 1 - increment

	for i in range(len(lines)):
		for j in range(len(lines[i])):
			lines[i][j] += 1

	# Step 2 & 3 - flash all bigger then 9 and set to 0
	flashed = []
	for i in range(len(lines)):
		for j in range(len(lines[i])):
			if lines[i][j] > 9:
				lines[i][j] = 0
				flashed.append((i,j))

				to_visit = [(i,j)]
				while to_visit:
					current = to_visit.pop(0)
					for adjacent in get_adjacent(current):
						if adjacent not in flashed:
							lines[adjacent[0]][adjacent[1]] += 1
							if lines[adjacent[0]][adjacent[1]] > 9:
								lines[adjacent[0]][adjacent[1]] = 0
								to_visit.append(adjacent)
								flashed.append(adjacent)


	# print("Step " + str(x+1))
	# for line in lines:
	# 	print("".join(list(map(lambda x: str(x), line))))
	# print("============================")

	total += len(flashed)

print("Part 1: " + str(total))

x = 100

while True:
	x+=1
	# Step 1 - increment

	for i in range(len(lines)):
		for j in range(len(lines[i])):
			lines[i][j] += 1

	# Step 2 & 3 - flash all bigger then 9 and set to 0
	flashed = []
	for i in range(len(lines)):
		for j in range(len(lines[i])):
			if lines[i][j] > 9:
				lines[i][j] = 0
				flashed.append((i,j))

				to_visit = [(i,j)]
				while to_visit:
					current = to_visit.pop(0)
					for adjacent in get_adjacent(current):
						if adjacent not in flashed:
							lines[adjacent[0]][adjacent[1]] += 1
							if lines[adjacent[0]][adjacent[1]] > 9:
								lines[adjacent[0]][adjacent[1]] = 0
								to_visit.append(adjacent)
								flashed.append(adjacent)


	# print("Step " + str(x))
	# for line in lines:
	# 	print("".join(list(map(lambda x: str(x), line))))
	# print("============================")

	values = set()
	for line in lines:
		values.update(line)

	if len(values) == 1:
		break

print("Part 2: " + str(x))