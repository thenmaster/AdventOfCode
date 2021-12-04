lines = []
with open("input.txt", "r") as f:
	for line in f.readlines():
		lines += [int(line.translate(line.maketrans("FBLR", "0101")), 2)]

print(sorted(lines)[-1:])		