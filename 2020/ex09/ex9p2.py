import copy

PREAMBLE = 25

def valid(values, value):
	for i in range(len(values)):
		for j in range(i, len(values)):
			if values[i] + values[j] == value:
				return True

	return False


values = []

with open("input.txt", "r") as f:
	for _ in range(PREAMBLE):
		values += [int(f.readline())]

	for line in f.readlines():
		value = int(line)

		end = False
		if not valid(values[len(values)-PREAMBLE:len(values)], value):
			print(value)
			for i in range(len(values)):
				for j in range(i, len(values)):
					if sum(values[i:j]) == value:
						c = copy.deepcopy(values[i:j])
						c.sort()
						print(c[0] + c[-1])
						end = True
						break
			if end:
				break
		values += [value]