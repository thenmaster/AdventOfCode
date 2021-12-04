possibilities = {}
def removeAll(index, rules, rule):
	# print("removing " + rule + " from " + str(index))

	possibilities[index].remove(rule)

	if len(rules) == 1:
		# print("Field " + str(index) + " has only 1 possibility")
		unique = rules[0]
		for p in possibilities:
			if unique in possibilities[p] and p != index:
				# print("R: " + str(possibilities[p]))
				removeAll(p, possibilities[p], unique)
	# print("======")


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

	f.readline()

	my_ticket = f.readline().split(",")
	# print(my_ticket)

	for _ in range(2):
		f.readline()

	for i in range(len(my_ticket)):
		possibilities[i] = list(rules.keys())


	valid_tickets = []
	for ticket in f.readlines():
		numbers = ticket.split(",")

		valid = True
		for number in numbers:
			exists = False

			for rule in rules:
				if int(number) in rules[rule]:
					exists = True
					break

			if not exists:
				valid = False
				break

		if valid:
			valid_tickets += [ticket]
	
	for ticket in valid_tickets:
		numbers = ticket.split(",")

		for i in range(len(numbers)):
			for rule in possibilities[i]:
				if int(numbers[i]) not in rules[rule]:
					removeAll(i, possibilities[i], rule)
						# possibilities[i].remove(rule)
						# if len(possibilities[i]) == 1:
						# 	unique = possibilities[i][0]
						# 	for p in possibilities:
						# 		if unique in possibilities[p] and p != i:
						# 			possibilities[p].remove(unique)


		# print(possibilities)

	print(possibilities)
	res = 1
	for p in possibilities:
		if "departure" in possibilities[p][0]:
			print("Found " + possibilities[p][0] + " for " + str(p))
			res *= int(my_ticket[p])

	print(res)
