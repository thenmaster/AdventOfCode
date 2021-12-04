
rules = {}

with open("input.txt", "r") as f:
	line = f.readline()
	while line != "\n":
		content = line.split(": ")
		intervals = content[1].split(" or ")
		ranges = []
		for interval in intervals:
			limits = interval.split("-")
			ranges += range(int(limits[0]), int(limits[1]) +1 )
		
		rules[content[0]] = ranges

		line = f.readline()

	for _ in range(4):
		f.readline()

	count = 0
	for ticket in f.readlines():
		numbers = ticket.split(",")

		for number in numbers:
			exists = False
			for rule in rules:
				if int(number) in rules[rule]:
					exists = True
					break

			if not exists:
				count += int(number)
	print(count)