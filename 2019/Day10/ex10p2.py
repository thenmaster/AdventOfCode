import math

layout = []
base = [0,1]

def calcangle(origin, point):
	vector = (point[0]-origin[0], point[1]-origin[1])
	angle = (math.degrees(math.atan2(vector[0], vector[1]))+180) % 360
	return angle	

def los(asteroid, asteroids):
	lines = set()
	for other in asteroids:
		if other != asteroid: # ignore the asteroid we are on
			vector = (other[1]-asteroid[1], other[0]-asteroid[0])
			common = abs(math.gcd(vector[1], vector[0]))
			lines.add((vector[1]//common,vector[0]//common))
	return lines

with open("input.txt") as f:
	layout = f.readlines()

layout = [line.strip() for line in layout]

asteroids = []
for i in range(len(layout)):
	for c in range(len(layout[i])):
		if layout[i][c] == "#":
			asteroids += [(c,i)]

best = (11,13) # from part 1

asteroids.remove(best)

def order(asteroid):
	return calcangle(best,asteroid)

asteroids.sort(key=order)

lines = los(best, asteroids)

print(lines)
print(asteroids)


print(asteroids.index((8,2)))