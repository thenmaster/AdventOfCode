vectors = {'N' : (0,1) , 'E' : (1,0), 'S' : (0,-1), 'W' : (-1,0)}

position = [0,0]
waypoint_move = [10,1]

with open("input.txt","r") as f:
	for l in f.readlines():
		option = l[0]

		if option == "R":
			deg = int(l[1:])
			count = deg // 90

			for _ in range(count):
				temp = waypoint_move[1]
				waypoint_move[1] = (-1) * waypoint_move[0]
				waypoint_move[0] = temp

		elif option == "L":
			deg = int(l[1:])
			count = deg // 90

			for _ in range(count):
				temp = waypoint_move[0]
				waypoint_move[0] = (-1) * waypoint_move[1]
				waypoint_move[1] = temp

		else:
			if option == "F":
				steps = int(l[1:])

				position[0] += waypoint_move[0] * steps
				position[1] += waypoint_move[1] * steps

			else:
				vector = vectors[option]

				steps = int(l[1:])

				waypoint_move[0] += vector[0] * steps
				waypoint_move[1] += vector[1] * steps

print(abs(position[0]) + abs(position[1]))