adapters = []

with open("input.txt", "r") as f:
	for line in f.readlines():
		adapters += [int(line)]

adapters += [max(adapters) + 3]

adapters += [0]

adapters.sort()

count1 = 0
count3 = 0
print(adapters)
for i in range(len(adapters)-1):
	if adapters[i+1] - adapters[i] == 1:
		count1+=1
	elif adapters[i+1] - adapters[i] == 3:
		count3+=1

print(count1)
print(count3)
print(count1*count3)