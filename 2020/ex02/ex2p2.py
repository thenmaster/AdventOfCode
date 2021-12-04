count = 0

with open("input.txt", "r") as f:
	for line in f.readlines():
		line = line.strip()
		data = line.split(":")
		password = data[1].strip()

		char = data[0].split()[1]
		places = data[0].split()[0]

		first = int(places.split("-")[0])-1
		second = int(places.split("-")[1])-1

		if password[first] == char or password[second] == char :
			if not ( password[first] == char and password[second] == char) :
				count+=1

print(count)