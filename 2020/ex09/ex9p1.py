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

		if not valid(values[len(values)-PREAMBLE:len(values)], value):
			print(value)
			break

		values += [value]