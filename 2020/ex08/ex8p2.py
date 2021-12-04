import copy

def execute(code):
	acc = 0
	i = 0

	executed = []

	while i < len(code):
	
		if i in executed:
			return False, acc

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

	return True, acc

code = []

with open("input.txt", "r") as f:
	for line in f.readlines():
		code += [line.strip()]


for i in range(len(code)):
	content = code[i].split()

	new_code = copy.deepcopy(code)

	if content[0] == "nop":
		new_line = "jmp " + content[1]
		new_code[i] = new_line
	elif content[0] == "jmp":
		new_line = "nop " + content[1]
		new_code[i] = new_line 

	result = execute(new_code)

	if result[0]:
		print(new_code)
		print(result)
		break