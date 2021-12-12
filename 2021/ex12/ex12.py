import sys

if len(sys.argv) < 2:
	print("Usage: python3 ex12.py <filename>")
	quit()

filename = sys.argv[1]

with open(filename) as file:
	maze_paths = {}
	for line in file:
		parsed = line.strip().split("-")

		if parsed[0] in maze_paths:
			maze_paths[parsed[0]].append(parsed[1])
		else:
			maze_paths[parsed[0]] = [parsed[1]]

		if parsed[1] in maze_paths:
			maze_paths[parsed[1]].append(parsed[0])
		else:
			maze_paths[parsed[1]] = [parsed[0]]

def traverse_maze(start, visited, base):
	if start == 'end':
		return [base]

	paths = []
	for path in maze_paths[start]:
		if path.islower() and path not in visited:
			visited.add(path)
			paths += traverse_maze(path, visited, base+[path])
			visited.remove(path)
		elif path not in visited:
			paths += traverse_maze(path, visited, base+[path])

	return paths

start_set = set()
start_set.add('start')

result = traverse_maze('start', start_set, ['start'])

print("Part 1: " + str(len(result)))

def traverse_maze_2(start, visited, base, can_double):
	if start == 'end':
		return [base]

	paths = []
	for path in maze_paths[start]:
		path_two = path + "2"
		if path.islower() and path not in visited:
			visited.add(path)
			paths += traverse_maze_2(path, visited, base+[path], can_double)
			visited.remove(path)
		elif path.islower() and path not in ("start", "end") and path_two not in visited and can_double:
			visited.add(path_two)
			paths += traverse_maze_2(path, visited, base+[path], False)
			visited.remove(path_two)
		elif path not in visited:
			paths += traverse_maze_2(path, visited, base+[path], can_double)

	return paths

start_set = set()
start_set.add('start')

result = traverse_maze_2('start', start_set, ['start'], True)

print("Part 2: " + str(len(result)))