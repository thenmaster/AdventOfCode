import sys

with open("input.txt", "r") as f:
	time = int(f.readline())
	buses = f.readline().split(",")

selected = 0
departure = sys.maxsize
for b in buses:
	if b != "x":
		period = int(b)
		multiple = 0
		while multiple < time:
			multiple += period

		if multiple < departure and multiple >= time:
			departure = multiple
			selected = period

print(departure)
print(selected)
print((departure - time) * selected)