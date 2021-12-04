count = 0

with open("input.txt", "r") as f:
	answers = set()
	for line in f.readlines():
		if line != "\n":
			for c in line.strip():
				answers.add(c)
		else:
			count += len(answers)
			answers.clear()

	if len(answers) != 0: #no new line at end of file
		count += len(answers)

print(count)