import sys

if len(sys.argv) < 2:
	print("Usage: python3 ex1.py <filename>")
	quit()

filename = sys.argv[1]
sonar = []

with open(filename) as file:
	for line in file:
		sonar += [int(line.strip())]

print(sonar)

counter = 0

for i in range(1,len(sonar)):
	if sonar[i] > sonar[i-1]:
		counter+=1

print("Part 1: " + str(counter))

slide_counter = 0

for i in range(3,len(sonar)):
	previous_window = i - 1
	sum_previous = sonar[previous_window]+sonar[previous_window-1]+sonar[previous_window-2]
	sum_current = sonar[i] + sonar[i-1] + sonar[i-2]
	if sum_current > sum_previous:
		slide_counter+=1

print("Part 2: " + str(slide_counter))