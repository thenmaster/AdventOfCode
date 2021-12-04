vectors = {'N' : (0,1) , 'E' : (1,0), 'S' : (0,-1), 'W' : (-1,0)}
directions = "NESW"

orientation = 'E'
position = [0,0]

with open("input.txt","r") as f:
	for l in f.readlines():
		option = l[0]

		if option == "R":
			deg = int(l[1:])
			count = deg // 90

			option = (directions.index(orientation) + count) % len(directions)

			orientation = directions[option]
		elif option == "L":
			deg = int(l[1:])
			count = deg // 90

			option = (directions.index(orientation) - count) % len(directions)

			orientation = directions[option]
		else:
			if option == "F":
				vector = vectors[orientation]
			else:
				vector = vectors[option]

			steps = int(l[1:])

			position[0] += vector[0] * steps
			position[1] += vector[1] * steps

print(abs(position[0]) + abs(position[1]))
