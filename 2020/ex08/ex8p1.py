code = []

with open("input.txt", "r") as f:
	for line in f.readlines():
		code += [line.strip()]

acc = 0
i = 0

executed = []

while i < len(code):
	
	if i in executed:
		break

	line = code[i]
	executed += [i]
	content = line.split()

	if content[0] == "acc":
		acc += int(content[1])
		i+=1
	elif content[0] == "jmp":
		i+= int(content[1])
	elif content[0] == "nop":
		i+=1
	else:
		raise ValueError("Unknown instruction")

print(acc)