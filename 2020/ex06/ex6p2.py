count = 0

with open("input.txt", "r") as f:
	answers = {}
	people = 0
	for line in f.readlines():
		if line != "\n":
			people += 1
			for c in line.strip():
				if c not in answers:
					answers[c] = 1
				else:
					answers[c] += 1
		else:
			for answer in answers:
				if answers[answer] == people:
					count+=1

			answers.clear()
			people = 0

	if len(answers) != 0: #no new line at end of file
		for answer in answers:
			if answers[answer] == people:
				count+=1

print(count)