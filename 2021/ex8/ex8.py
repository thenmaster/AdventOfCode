import sys
import itertools

class Entry(object):
	"""docstring for Entry"""
	def __init__(self, patterns, output):
		super(Entry, self).__init__()
		self.patterns = patterns
		self.output = output

	def get_patterns(self):
		return self.patterns

	def get_output(self):
		return self.output

	def __str__(self):
		return """Entry:
	Patterns: """ + str(self.patterns) + """
	Output: """ + str(self.output)

	def __repr__(self):
		return """Entry:
Patterns: """ + str(self.patterns) + """
Output: """ + str(self.output) + "\n"

def get_pattern_to_digit_map(patterns):
	m = {}
	for pattern in patterns:
		if len(pattern) == 2:
			m['1'] = pattern
			continue
		if len(pattern) == 3:
			m['7'] = pattern
			continue
		if len(pattern) == 4:
			m['4'] = pattern
			continue
		if len(pattern) == 7:
			m['8'] = pattern
			continue

	for pattern in patterns:
		if m['1'][0] in pattern and m['1'][1] in pattern and len(pattern) == 5:
			m['3'] = pattern
			break

	for pattern in patterns:
		if not (m['1'][0] in pattern and m['1'][1] in pattern) and len(pattern) == 6:
			m['6'] = pattern
			break

	for pattern in patterns:
		if len(pattern) == 5 and len(set(m['6']) - set(pattern)) == 1:
			m['5'] = pattern
			break

	for pattern in patterns:
		if len(pattern) == 5 and pattern not in m.values():
			m['2'] = pattern
			break

	for pattern in patterns:
		if len(pattern) == 6 and len(set(pattern) - set(m['4']+m['7'])) == 1:
			m['9'] = pattern
			break

	for pattern in patterns:
		if len(pattern) == 6 and pattern not in m.values():
			m['0'] = pattern
			break

	return m


if len(sys.argv) < 2:
	print("Usage: python3 ex8.py <filename>")
	quit()

filename = sys.argv[1]

with open(filename) as file:
	inputs = []
	for line in file:
		content = line.strip().split(" | ")
		inputs += [Entry(content[0].split(" "), content[1].split(" "))]

count = 0
for entry in inputs:
	output = entry.get_output()
	for digit in output:
		if len(digit) == 2: # 1
			count += 1
		if len(digit) == 3: # 7
			count += 1
		if len(digit) == 4: # 4
			count += 1
		if len(digit) == 7: # 8
			count += 1

print("Part 1: " + str(count))

total = 0
for entry in inputs:
	mapper = get_pattern_to_digit_map(entry.get_patterns())
	value = ''
	output = entry.get_output()
	for digit in output:
		for key, item in mapper.items():
			if len(item) != len(digit):
				continue
			if digit in list(map(lambda x: "".join(x), itertools.permutations(item))):
				value += key
	total += int(value)

print("Part 2: " + str(total))