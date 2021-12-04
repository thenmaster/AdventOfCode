import copy

program = [3,8,1001,8,10,8,105,1,0,0,21,34,59,76,101,114,195,276,357,438,99999,3,9,1001,9,4,9,1002,9,4,9,4,9,99,3,9,102,4,9,9,101,2,9,9,102,4,9,9,1001,9,3,9,102,2,9,9,4,9,99,3,9,101,4,9,9,102,5,9,9,101,5,9,9,4,9,99,3,9,102,2,9,9,1001,9,4,9,102,4,9,9,1001,9,4,9,1002,9,3,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99]

# program = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

def run(setting, signal):
	code = copy.deepcopy(program)
	i = 0
	inputrun = 0
	output = 0
	while i < len(code):
		config = code[i]
		opcode = int(str(config)[-2:])
		if (opcode == 99):
			break
		elif(opcode == 1):
			options = str(config)[:-2]
			if not options:
				code[code[i+3]] = code[code[i+1]] + code[code[i+2]]
			else:
				var1 = code[i+1] if len(options) >= 1 and options[-1] == '1' else code[code[i+1]]
				var2 = code[i+2] if len(options) >= 2 and options[-2] == '1' else code[code[i+2]]
				code[code[i+3]] = var1 + var2
			i+=4
		elif(opcode == 2):
			options = str(config)[:-2]
			if not options:
				code[code[i+3]] = code[code[i+1]] * code[code[i+2]]
			else:
				var1 = code[i+1] if len(options) >= 1 and options[-1] == '1' else code[code[i+1]]
				var2 = code[i+2] if len(options) >= 2 and options[-2] == '1' else code[code[i+2]]
				code[code[i+3]] = var1 * var2
			i+=4
		elif(opcode == 3):
			# x = input()
			x = setting if inputrun == 0 else signal
			inputrun+=1
			code[code[i+1]] = int(x)
			i+=2
		elif(opcode == 4):
			options = str(config)[:-2]
			if not options:
				print(code[code[i+1]])
				output = code[code[i+1]]
				if (code[code[i+1]] != 0):
					break
			else:
				print(code[i+1])
				output = code[i+1]
				if (code[i+1] != 0):
					break
			i+=2
		elif (opcode == 5):
			options = str(config)[:-2]
			if not options:
				if (code[code[i+1]] != 0):
					i = code[code[i+2]]
					continue
			else:
				var1 = code[i+1] if len(options) >= 1 and options[-1] == '1' else code[code[i+1]]
				var2 = code[i+2] if len(options) >= 2 and options[-2] == '1' else code[code[i+2]]
				if (var1 != 0):
					i = var2
					continue
			i+=3
		elif (opcode == 6):
			options = str(config)[:-2]
			if not options:
				if (code[code[i+1]] == 0):
					i = code[code[i+2]]
					continue
			else:
				var1 = code[i+1] if len(options) >= 1 and options[-1] == '1' else code[code[i+1]]
				var2 = code[i+2] if len(options) >= 2 and options[-2] == '1' else code[code[i+2]]
				if (var1 == 0):
					i = var2
					continue
			i+=3
		elif (opcode == 7):
			options = str(config)[:-2]
			if not options:
				code[code[i+3]] = 1 if code[code[i+1]] < code[code[i+2]] else 0
			else:
				var1 = code[i+1] if len(options) >= 1 and options[-1] == '1' else code[code[i+1]]
				var2 = code[i+2] if len(options) >= 2 and options[-2] == '1' else code[code[i+2]]
				code[code[i+3]] = 1 if var1 < var2 else 0
			i+=4
		elif (opcode == 8):
			options = str(config)[:-2]
			if not options:
				code[code[i+3]] = 1 if code[code[i+1]] == code[code[i+2]] else 0
			else:
				var1 = code[i+1] if len(options) >= 1 and options[-1] == '1' else code[code[i+1]]
				var2 = code[i+2] if len(options) >= 2 and options[-2] == '1' else code[code[i+2]]
				code[code[i+3]] = 1 if var1 == var2 else 0
			i+=4
		else:
			break
	return output

power = 0
combination = []

for a in range(0,5):
	for b in range(0,5):
		for c in range(0,5):
			for d in range(0,5):
				for e in range(0,5):
					out = 0
					inputs = [a,b,c,d,e]
					if len(inputs) != len(set(inputs)): # each setting is only used once
						continue
					for i in inputs:
						out = run(i,out)
					if(out > power):
						power = out
						combination = inputs
print(combination)
print(power)