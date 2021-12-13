import sys

if len(sys.argv) < 2:
	print("Usage: python3 ex13.py <filename>")
	quit()

filename = sys.argv[1]

with open(filename) as file:
	dots = set()
	folds = []
	for line in file:
		stripped = line.strip()
		if "," in line:
			pair = stripped.split(",")
			dots.add((int(pair[0]), int(pair[1])))
		elif "=" in line:
			fold = stripped.split(" ")[2].split("=")
			folds.append((fold[0], int(fold[1])))


first_fold = folds[0]

new_dots = set(dots)
for dot in dots:
	if first_fold[0] == "y":
		if dot[1] > first_fold[1]:
			new_dot = (dot[0], first_fold[1] - (dot[1] - first_fold[1]))
			new_dots.remove(dot)
			new_dots.add(new_dot)
	else:
		if dot[0] > first_fold[1]:
			new_dot = (first_fold[1] - (dot[0] - first_fold[1]), dot[1])
			new_dots.remove(dot)
			new_dots.add(new_dot)

print("Part 1: " + str(len(new_dots)))

dots = set(new_dots)
for fold in folds[1:]:
	new_dots = set(dots) 
	for dot in dots:
		if fold[0] == "y":
			if dot[1] > fold[1]:
				new_dot = (dot[0], fold[1] - (dot[1] - fold[1]))
				new_dots.remove(dot)
				new_dots.add(new_dot)
		else:
			if dot[0] > fold[1]:
				new_dot = (fold[1] - (dot[0] - fold[1]), dot[1])
				new_dots.remove(dot)
				new_dots.add(new_dot)
	dots = new_dots

print("Part 2:")
# Very dirty hack :(
layout = []
for i in range(40):
	line = []
	for j in range(40):
		if (i,j) in dots:
			line.append("#")
		else:
			line.append(".")
	layout.append(line)

for line in layout[::-1]:
	print("".join(line))