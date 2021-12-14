import sys
import collections

if len(sys.argv) < 2:
	print("Usage: python3 ex14.py <filename>")
	quit()

filename = sys.argv[1]

with open(filename) as file:
	chain = file.readline().strip()
	file.readline()

	templates = {}
	for line in file:
		pair = line.strip().split(" -> ")
		templates[pair[0]] = pair[1]

for _ in range(10):
	new_chain = ''
	for i in range(1,len(chain)):
		pair = chain[i-1] + chain[i]
		if pair in templates:
			new_chain += pair[0] + templates[pair]
		else:
			new_chain += pair[0]
	new_chain += chain[-1]		
	chain = new_chain

frequency = collections.Counter(chain)

dif = max(frequency.values()) - min(frequency.values())

print("Part 1: " + str(dif))

with open(filename) as file:
	chain = file.readline().strip()
	file.readline()

	templates = {}
	for line in file:
		pair = line.strip().split(" -> ")
		templates[pair[0]] = pair[1]

for _ in range(40):
	new_chain = ''
	for i in range(1,len(chain)):
		pair = chain[i-1] + chain[i]
		if pair in templates:
			new_chain += pair[0] + templates[pair]
		else:
			new_chain += pair[0]
	new_chain += chain[-1]		
	chain = new_chain

frequency = collections.Counter(chain)

dif = max(frequency.values()) - min(frequency.values())

print("Part 2: " + str(dif))