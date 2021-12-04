
code = [3,8,1005,8,310,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,28,1,105,11,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,55,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,76,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,98,1,1004,7,10,1006,0,60,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,127,2,1102,4,10,1,1108,7,10,2,1102,4,10,2,101,18,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,166,1006,0,28,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,190,1006,0,91,1,1108,5,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,220,1,1009,14,10,2,1103,19,10,2,1102,9,10,2,1007,4,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,258,2,3,0,10,1006,0,4,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,286,1006,0,82,101,1,9,9,1007,9,1057,10,1005,10,15,99,109,632,104,0,104,1,21102,1,838479487636,1,21102,327,1,0,1106,0,431,21102,1,932813579156,1,21102,1,338,0,1106,0,431,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,179318033447,1,21101,385,0,0,1105,1,431,21101,248037678275,0,1,21101,0,396,0,1105,1,431,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,709496558348,1,21102,419,1,0,1105,1,431,21101,825544561408,0,1,21101,0,430,0,1106,0,431,99,109,2,22101,0,-1,1,21101,40,0,2,21102,462,1,3,21101,0,452,0,1106,0,495,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,457,458,473,4,0,1001,457,1,457,108,4,457,10,1006,10,489,1101,0,0,457,109,-2,2106,0,0,0,109,4,2101,0,-1,494,1207,-3,0,10,1006,10,512,21101,0,0,-3,22101,0,-3,1,22101,0,-2,2,21101,1,0,3,21102,531,1,0,1105,1,536,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,559,2207,-4,-2,10,1006,10,559,22101,0,-4,-4,1106,0,627,21202,-4,1,1,21201,-3,-1,2,21202,-2,2,3,21102,578,1,0,1105,1,536,22101,0,1,-4,21101,1,0,-1,2207,-4,-2,10,1006,10,597,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,619,21201,-1,0,1,21102,1,619,0,105,1,494,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]

# code = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]


i = 0
p = 0

def increase_code(size):
	global code
	code += [0 for _ in range(size)]

increase_code(1000)

def calculate_color(panel):
	global i,p

	outcount = 0
	values = []

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

				if len(options) >= 1 and options[-1] == '2':
					address = p + (code[i+1])
					if len(code)-1 < address:
						increase_code(address-(len(code)-1))
					var1 = code[address]

				if len(options) >= 2 and options[-2] == '2':
					address = p + (code[i+2])
					if len(code)-1 < address:
						increase_code(address-(len(code)-1))
					var2 = code[address]

				increase = p if len(options) >= 3 and options[-3] == '2' else 0	

				code[code[i+3]+increase] = var1 + var2
			i+=4
		elif(opcode == 2):
			options = str(config)[:-2]
			if not options:
				code[code[i+3]] = code[code[i+1]] * code[code[i+2]]
			else:
				var1 = code[i+1] if len(options) >= 1 and options[-1] == '1' else code[code[i+1]]
				var2 = code[i+2] if len(options) >= 2 and options[-2] == '1' else code[code[i+2]]

				if len(options) >= 1 and options[-1] == '2':
					address = p + (code[i+1])
					if len(code)-1 < address:
						increase_code(address-(len(code)-1))
					var1 = code[address]

				if len(options) >= 2 and options[-2] == '2':
					address = p + (code[i+2])
					if len(code)-1 < address:
						increase_code(address-(len(code)-1))
					var2 = code[address]

				increase = p if len(options) >= 3 and options[-3] == '2' else 0	

				code[code[i+3]+increase] = var1 * var2
			i+=4
		elif(opcode == 3):

			options = str(config)[:-2]

			increase = p if options == "2" else 0

			# x = input()
			code[code[i+1]+increase] = panel # int(x)

			i+=2
		elif(opcode == 4):

			options = str(config)[:-2]
			if not options:
				# print(code[code[i+1]])
			 	values += [code[code[i+1]]]
			else:
				var1 = code[i+1] if len(options) >= 1 and options[-1] == '1' else code[code[i+1]]

				if len(options) >= 1 and options[-1] == '2':
					address = p + (code[i+1])
					if len(code)-1 < address:
						increase_code(address-(len(code)-1))
					var1 = code[address]

				# print(var1)
				values += [var1]

			outcount+=1
			if (outcount == 2):
				return values
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

				if len(options) >= 1 and options[-1] == '2':
					address = p + (code[i+1])
					if len(code)-1 < address:
						increase_code(address-(len(code)-1))
					var1 = code[address]

				if len(options) >= 2 and options[-2] == '2':
					address = p + (code[i+2])
					if len(code)-1 < address:
						increase_code(address-(len(code)-1))
					var2 = code[address]

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

				if len(options) >= 1 and options[-1] == '2':
					address = p + (code[i+1])
					if len(code)-1 < address:
						increase_code(address-(len(code)-1))
					var1 = code[address]

				if len(options) >= 2 and options[-2] == '2':
					address = p + (code[i+2])
					if len(code)-1 < address:
						increase_code(address-(len(code)-1))
					var2 = code[address]

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

				if len(options) >= 1 and options[-1] == '2':
					address = p + (code[i+1])
					if len(code)-1 < address:
						increase_code(address-(len(code)-1))
					var1 = code[address]

				if len(options) >= 2 and options[-2] == '2':
					address = p + (code[i+2])
					if len(code)-1 < address:
						increase_code(address-(len(code)-1))
					var2 = code[address]


				increase = p if len(options) >= 3 and options[-3] == '2' else 0	

				code[code[i+3]+increase] = 1 if var1 < var2 else 0
			i+=4
		elif (opcode == 8):
			options = str(config)[:-2]
			if not options:
				code[code[i+3]] = 1 if code[code[i+1]] == code[code[i+2]] else 0
			else:
				var1 = code[i+1] if len(options) >= 1 and options[-1] == '1' else code[code[i+1]]
				var2 = code[i+2] if len(options) >= 2 and options[-2] == '1' else code[code[i+2]]

				if len(options) >= 1 and options[-1] == '2':
					address = p + (code[i+1])
					if len(code)-1 < address:
						increase_code(address-(len(code)-1))
					var1 = code[address]

				if len(options) >= 2 and options[-2] == '2':
					address = p + (code[i+2])
					if len(code)-1 < address:
						increase_code(address-(len(code)-1))
					var2 = code[address]

				increase = p if len(options) >= 3 and options[-3] == '2' else 0	

				code[code[i+3]+increase] = 1 if var1 == var2 else 0
			i+=4
		elif (opcode == 9):
			options = str(config)[:-2]
			if not options:
				p += code[code[i+1]]
			else:
				var1 = code[i+1] if len(options) >= 1 and options[-1] == '1' else code[code[i+1]]

				if len(options) >= 1 and options[-1] == '2':
					address = p + (code[i+1])
					if len(code)-1 < address:
						increase_code(address-(len(code)-1))
					var1 = code[address]
				p += var1
			i+=2
		else:
			break

vector = [1,0]

def rotate(direction):
	global vector
	if direction == "l":
		if vector == [1,0]:
			vector = [0,-1]
		elif vector == [0,-1]:
			vector = [-1,0]
		elif vector == [-1,0]:
			vector = [0,1]
		elif vector == [0,1]:
			vector = [1,0]
	else:
		if vector == [1,0]:
			vector = [0,1]
		elif vector == [0,1]:
			vector = [-1,0]
		elif vector == [-1,0]:
			vector = [0,-1]
		elif vector == [0,-1]:
			vector = [1,0]

position = [0,0]
painted = {[0,0]}