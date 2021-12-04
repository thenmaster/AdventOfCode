count = 0 

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

with open("input.txt", "r") as f:
	lines = []
	for line in f.readlines():
		if line != "\n":
			lines += [line.strip()]
		else:
			passport = {}
			for l in lines:
				content = l.split(" ")
				for detail in content:
					data = detail.split(":")
					passport[data[0]] = data[1]

			count+=1
			for field in fields:
				if field not in passport:
					count-=1
					break

			lines = []

print(count)