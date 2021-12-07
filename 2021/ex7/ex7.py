import sys

if len(sys.argv) < 2:
	print("Usage: python3 ex7.py <filename>")
	quit()

filename = sys.argv[1]

with open(filename) as file:
	inputs = list(map(lambda x: int(x), file.readline().strip().split(",")))

totals = {}
for i in range(1, max(inputs)+1):
	total_fuel = 0
	for position in inputs:
		total_fuel += abs(position-i)
	totals[i] = total_fuel

print("Part 1: " + str(min(totals.values())))

real_totals = {}
for i in range(1, max(inputs)+1):
	total_fuel = 0
	for position in inputs:
		total_fuel += sum([x for x in range(1,abs(position-i)+1)])
	real_totals[i] = total_fuel

print("Part 2: " + str(min(real_totals.values())))