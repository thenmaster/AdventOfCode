import sys
import copy

if len(sys.argv) < 2:
	print("Usage: python3 ex3.py <filename>")
	quit()

filename = sys.argv[1]
values = []

with open(filename) as file:
	for line in file:
		values += [line.strip()]

#print(values)


size = len(values[0])
gamma = ''
epsilon = ''
for i in range(size):
	counts = {'0': 0, '1': 0}
	for value in values:	
		counts[value[i]]+=1
	if counts['0'] > counts['1']:
		gamma+='0'
		epsilon+='1'
	else:
		gamma+='1'
		epsilon+='0'

# print(gamma)
# print(epsilon)

print("Part 1: " + str(int(gamma,2) * int(epsilon,2)))

oxygen_values=copy.deepcopy(values)
cotwo_values=copy.deepcopy(values)

for i in range(size):
	counts = {'0': 0, '1': 0}
	new_values = []
	for value in oxygen_values:	
		counts[value[i]]+=1
	if counts['0'] > counts['1']:
		for value in oxygen_values:
			if value[i] == '0':
				new_values += [value]
	else:
		for value in oxygen_values:
			if value[i] == '1':
				new_values += [value]

	oxygen_values = new_values
	if len(oxygen_values) == 1:
		break

for i in range(size):
	counts = {'0': 0, '1': 0}
	new_values = []
	for value in cotwo_values:	
		counts[value[i]]+=1
	if counts['0'] <= counts['1']:
		for value in cotwo_values:
			if value[i] == '0':
				new_values += [value]
	else:
		for value in cotwo_values:
			if value[i] == '1':
				new_values += [value]

	cotwo_values = new_values
	if len(cotwo_values) == 1:
		break

print(oxygen_values)
print(cotwo_values)

print("Part 2: " + str(int(oxygen_values[0],2) * int(cotwo_values[0],2)))