import copy

program = [3,8,1001,8,10,8,105,1,0,0,21,34,59,76,101,114,195,276,357,438,99999,3,9,1001,9,4,9,1002,9,4,9,4,9,99,3,9,102,4,9,9,101,2,9,9,102,4,9,9,1001,9,3,9,102,2,9,9,4,9,99,3,9,101,4,9,9,102,5,9,9,101,5,9,9,4,9,99,3,9,102,2,9,9,1001,9,4,9,102,4,9,9,1001,9,4,9,1002,9,3,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99]

# program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

def run(setting, signal,state, ip):
	code = state
	i = ip
	output = 0
	while i < len(code):
		config = code[i]
		opcode = int(str(config)[-2:])
		if (opcode == 99):
			return None
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
			x = setting if setting != None else signal
			setting = None
			code[code[i+1]] = int(x)
			i+=2
		elif(opcode == 4):
			options = str(config)[:-2]
			if not options:
				return (code[code[i+1]], code, i+2)

				if (code[code[i+1]] != 0):
					break
			else:
				return (code[i+1], code, i+2)
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

power = 0
combination = []

for a in range(5,10):
	for b in range(5,10):
		for c in range(5,10):
			for d in range(5,10):
				for e in range(5,10):
					inputs = [a,b,c,d,e]
					if len(inputs) != len(set(inputs)): # each setting is only used once
						continue

					outputs = [0,0,0,0,0]
					states = [program[:] for _ in range(5)]
					ips = [0,0,0,0,0]

					print(inputs)
					stop = False
					while not stop:
						for i in range(len(inputs)):
							out = run(inputs[i],outputs[i-1],states[i],ips[i])
							if out == None:
								stop = True
								break
							else:
								outputs[i] = out[0]
								states[i] = out[1]
								ips[i] = out[2]
								inputs[i] = None
						# print(outputs)
						# print(states)
						# print(ips)
						# print(inputs)
						# input()

					if(outputs[4] > power):
						power = outputs[4]
						combination = [a,b,c,d,e]
print(combination)
print(power)