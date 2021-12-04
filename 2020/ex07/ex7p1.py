def find_bags(rules, bag):
	bags = set()
	for rule in rules:
		if bag in rules[rule] or bag[:-1] in rules[rule]:
			bags.add(rule)

	total = set([b for b in bags])
	for new_bag in bags:
		total = total | find_bags(rules, new_bag)

	return total

rules = {}
with open("input.txt", "r") as f:
	for line in f.readlines():
		rule = line.split("contain")
		rules[rule[0].strip()] = rule[1].strip()

bags = find_bags(rules, "shiny gold bag")

print(len(bags))