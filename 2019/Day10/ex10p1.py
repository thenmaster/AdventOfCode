import math

layout = []

def los(asteroid, asteroids):
	lines = set()
	for other in asteroids:
		if other != asteroid: # ignore the asteroid we are on
			vector = (other[1]-asteroid[1], other[0]-asteroid[0])
			common = abs(math.gcd(vector[1], vector[0]))
			lines.add((vector[1]//common,vector[0]//common))
	return len(lines)		

with open("input.txt") as f:
	layout = f.readlines()

layout = [line.strip() for line in layout]

asteroids = []
for i in range(len(layout)):
	for c in range(len(layout[i])):
		if layout[i][c] == "#":
			asteroids += [(c,i)]

chosen = None
best = 0
for asteroid in asteroids:
	count = los(asteroid, asteroids)
	if count > best:
		chosen = asteroid
		best = count
print(chosen)
print(best)