
def travel_slope(right,down , hill):
	count = 0 

	x = 0
	y = 0

	while y < len(hill):
		if hill[y][x] == "#":
			count+=1
		y+=down
		x+=right

		x = x % len(hill[0])

	return count


hill = []
paths = [(1, 1), (3, 1), (5, 1), (7, 1), (1,2)]

with open("input.txt", "r") as f:
	for line in f.readlines():
		hill += [line.strip()]

total = 1
for path in paths:
	count = travel_slope(path[0], path[1], hill)
	print("res: " + str(count))
	total *= count

print(total)
