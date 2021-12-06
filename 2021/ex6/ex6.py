import sys

class Fish(object):
	"""docstring for Fish"""
	def __init__(self, start:int, current:int):
		super(Fish, self).__init__()
		self.start = start
		self.current = current

	def get_start(self):
		return self.start

	def get_current(self):
		return self.current

	def pass_time(self):
		self.current-=1

	def should_spawn(self):
		return self.current == 0

	def reset_current(self):
		self.current = self.start

	def __str__(self):
		return "Fish start=" + str(self.start) + " current=" + str(self.current)

	def __repr__(self):
		return "Fish start=" + str(self.start) + " current=" + str(self.current)

if len(sys.argv) < 2:
	print("Usage: python3 ex6.py <filename>")
	quit()

filename = sys.argv[1]

with open(filename) as file:
	inputs = list(map(lambda x: int(x), file.readline().strip().split(",")))

school = []
for times in inputs:
	school += [Fish(6,times)]

for _ in range(80):
	new_school = []
	for fish in school:
		if fish.get_current() == 0:
			new_school += [Fish(fish.get_start(),fish.get_start()+2)]
			fish.reset_current()		
		else:
			fish.pass_time()
		new_school+= [fish]
	school=new_school

print("Part 1: " + str(len(school)))

with open(filename) as file:
	inputs = list(map(lambda x: int(x), file.readline().strip().split(",")))

counters = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

for times in inputs:
	counters[times]+=1

total = len(inputs)
for _ in range(256):
	temp = counters[0]

	for i in range(1,9):
		counters[i-1] = counters[i]

	counters[8] = temp
	counters[6] += temp
	total += temp

print("Part 2: " + str(total))