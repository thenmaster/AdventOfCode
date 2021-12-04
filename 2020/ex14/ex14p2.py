def generatePossibleAddresses(address):
	if 'X' not in address:
		return [address]
	else:
		return generatePossibleAddresses(address.replace("X", "0", 1)) + generatePossibleAddresses(address.replace("X", "1", 1))

mask = None
mem = {}

with open("input.txt", "r") as f:
	for line in f.readlines():
		content = line.split(" = ")
		if content[0].strip() == "mask":
			mask = content[1].strip()
		else:
			value = int(content[1].strip())
			position = int(content[0][content[0].index("[")+1:content[0].index("]")])

			collect = ""
			for mask_val, input_val in zip(mask.zfill(36), bin(position)[2:].zfill(36)):
				if mask_val == '0':
					collect += input_val
				else:
					collect += mask_val

			addresses = generatePossibleAddresses(collect)

			for address in addresses:
				mem[address] = value

total = 0
for val in mem:
	total += mem[val]
print(total)