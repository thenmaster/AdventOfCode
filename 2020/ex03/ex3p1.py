hill = []

with open("input.txt", "r") as f:
	for line in f.readlines():
		hill += [line.strip()]

count = 0 

x = 0
y = 0

while y < len(hill):
	if hill[y][x] == "#":
		count+=1
	y+=1
	x+=3

	x = x % len(hill[0])

	print(x)
	print(y)
	print("========")

print("res: " + str(count))