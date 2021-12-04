intervals = {}
prod = 1

with open("input.txt", "r") as f:
	f.readline()
	timetable = f.readline().split(",")
	for i in range(len(timetable)):
		if timetable[i] != "x":
			prod *= int(timetable[i])
			intervals[int(timetable[i])] = i

print(intervals)

result = 0
for bus in intervals:
	p = prod // bus
	result += -intervals[bus] * pow(p, -1, bus) * p

print(result % prod)