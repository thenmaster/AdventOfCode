stored = {}
def get_possible_paths(adapters, value):

	if value in stored:
		return stored[value]

	paths = 0

	start = adapters.index(value)

	possibles = []
	for i in range(start+1, len(adapters)):
		if adapters[i] - value <= 3: 
			possibles += [adapters[i]]

	for possible in possibles:
		new_paths = get_possible_paths(adapters, possible)
		paths += new_paths
	
	if not paths:
		paths += 1

	stored[value] = paths

	return paths



adapters = []

with open("input.txt", "r") as f:
	for line in f.readlines():
		adapters += [int(line)]

adapters += [max(adapters) + 3]

adapters += [0]

adapters.sort()

print(get_possible_paths(adapters, 0))