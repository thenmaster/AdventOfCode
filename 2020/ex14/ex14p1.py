mask = None
mem = {}
with open("input.txt", "r") as f:
	for line in f.readlines():
		content = line.split(" = ")
		if content[0].strip() == "mask":
			mask = content[1].strip()
		else:
			value = int(content[1].strip())
			position = content[0][content[0].index("[")+1:content[0].index("]")]

			collect = ""
			for mask_val, input_val in zip(mask, bin(value)[2:].zfill(36)):
				if mask_val != 'X':
					collect += mask_val
				else:
					collect += input_val

			mem[position] = int(collect, 2)

total = 0
for val in mem:
	total += mem[val]
print(total)