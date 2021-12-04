
with open("input.txt", "r") as f:
	numbers = f.readline().split(",")

last_rounds = {}
last_spoken = ""
current_round = 0

for n in numbers:
	current_round+=1
	last_rounds[int(n)] = current_round
	last_spoken = int(n)

print(last_spoken)
# print(last_rounds)
print("============")	

while current_round < 30000000:
	if last_spoken not in last_rounds:
		last_rounds[last_spoken] = current_round
		last_spoken = 0
	else:
		last_turn = last_rounds[last_spoken]
		last_rounds[last_spoken] = current_round
		last_spoken = current_round - last_turn

	current_round+=1

print(last_spoken)
# print(last_rounds)
print("=========")