count = 0

with open("input.txt", "r") as f:
	for line in f.readlines():
		line = line.strip()
		data = line.split(":")
		password = data[1]

		char = data[0].split()[1]
		amounts = data[0].split()[0]

		low = int(amounts.split("-")[0])
		high = int(amounts.split("-")[1])

		amount = password.count(char)

		if amount <= high and low <= amount:
			count+=1

print(count)