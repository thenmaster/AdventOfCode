import string
count = 0 

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def validate_passport_content(passport):
	byr = passport["byr"]
	if len(byr) != 4 or int(byr) < 1920 or int(byr) > 2002:
		return False

	iyr = passport["iyr"]
	if len(iyr) != 4 or int(iyr) < 2010 or int(iyr) > 2020:
		return False

	eyr = passport["eyr"]
	if len(eyr) != 4 or int(eyr) < 2020 or int(eyr) > 2030:
		return False

	hgt = passport["hgt"]
	if hgt[-2:] == "cm":
		if len(hgt) != 5 or int(hgt[0:3]) < 150 or int(hgt[0:3]) > 193:
			return False
	elif hgt[-2:] == "in":
		if len(hgt) != 4 or int(hgt[0:2]) < 59 or int(hgt[0:2]) > 76:
			return False
	else:
		return False

	hcl = passport["hcl"]
	if hcl[0] != "#" or len(hcl[1:]) != 6 or not all(c in string.hexdigits for c in hcl[1:]):
		return False

	ecl = passport["ecl"]
	if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
		return False

	pid = passport["pid"]
	if len(pid) != 9:
		return False


	return True

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

			contains_all_fields = True
			for field in fields:
				if field not in passport:
					contains_all_fields = False
					break

			if contains_all_fields and validate_passport_content(passport):
				count+=1

			lines = []

print(count)