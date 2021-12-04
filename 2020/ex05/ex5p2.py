lines = []
with open("input.txt", "r") as f:
	for line in f.readlines():
		lines += [int(line.translate(line.maketrans("FBLR", "0101")), 2)]

for i in range(sorted(lines)[-1]):
	if i not in lines and i-1 in lines and i+1 in lines:
		print(i)