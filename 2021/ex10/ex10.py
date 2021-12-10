import sys

if len(sys.argv) < 2:
	print("Usage: python3 ex10.py <filename>")
	quit()

filename = sys.argv[1]

with open(filename) as file:
	lines = []
	for line in file:
		lines += [line.strip()]

corrupt_score_map = {')':3, ']':57, '}':1197, '>':25137}
close_map = {'(':')', '[':']', '{':'}', '<':'>'}

total = 0
corrupted = []
for line in lines:
	stack = []
	for char in line:
		if char in close_map.keys():
			stack.append(char)
		else:
			open_char = stack.pop()
			if char != close_map[open_char]:
				total += corrupt_score_map[char]
				corrupted.append(line)
				break

print("Part 1: " + str(total))

for c in corrupted:
	lines.remove(c)

missing_score_map = {')':1, ']':2, '}':3, '>':4}

scores=[]
for line in lines:
	stack = []
	for char in line:
		if char in close_map.keys():
			stack.append(char)
		else:
			open_char = stack.pop()
	stack = stack[::-1]
	missing_chars = list(map(lambda x: close_map[x], stack))
	score = 0
	for char in missing_chars:
		score = (score * 5) + missing_score_map[char]
	scores.append(score)

scores = sorted(scores)
print("Part 2: " + str(scores[int(len(scores) / 2)]))