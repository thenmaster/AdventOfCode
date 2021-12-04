def count_bags(rules, bag):
	amount = 1

	#plurals suck....
	if bag in rules:
		rule = rules[bag]
	else:
		rule = rules[bag + "s"]

	content = rule.split(",")
	for c in content:
		c = c.strip()
		if c != "no other bags.":
			s = c.split(" ")
			print(" ".join(s[1:])[:-1])
			amount += int(c[0])*count_bags(rules, " ".join(s[1:]).replace(".", "")) # get rid of the pesky . at the end

	return amount

rules = {}

with open("input.txt", "r") as f:
	for line in f.readlines():
		rule = line.split("contain")
		rules[rule[0].strip()] = rule[1].strip()

amount = count_bags(rules, "shiny gold bags")

print(amount-1)