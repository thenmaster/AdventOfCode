import sys

if len(sys.argv) < 2:
	print("Usage: python3 ex2.py <filename>")
	quit()

filename = sys.argv[1]
commands = []

with open(filename) as file:
	for line in file:
		commands += [line.strip().split(" ")]

#print(commands)
horizontal = 0
depth = 0

for command in commands:
	if command[0] == 'forward':
		horizontal+=int(command[1])
	elif command[0] == 'up':
		depth-=int(command[1])
	elif command[0] == 'down':
		depth+=int(command[1])
	else:
		raise ValueError("Unknown direction:" + command[0])

print(horizontal)
print(depth)
print("Part 1: " + str(horizontal*depth))

horizontal = 0
depth = 0
aim = 0

for command in commands:
	if command[0] == 'forward':
		horizontal+=int(command[1])
		depth+=aim*int(command[1])
	elif command[0] == 'up':
		aim-=int(command[1])
	elif command[0] == 'down':
		aim+=int(command[1])
	else:
		raise ValueError("Unknown direction:" + command[0])

print(horizontal)
print(depth)
print(aim)
print("Part 2: " + str(horizontal*depth))