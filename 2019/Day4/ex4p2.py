def validate_number(num):
	num_str = str(num)
	if len(num_str) != 6:
		return False
	for i in range(0, len(num_str)-1):
		if int(num_str[i]) > int(num_str[i+1]):
			return False
	
	unique = "".join(set(num_str))

	for c in unique:
		if num_str.count(c) == 2:
			for i in range(0, len(num_str)-1):
				if num_str[i] == c and num_str[i+1] == c:
					return True
	return False

print(validate_number(123456))
print(validate_number(111111))
print(validate_number(111123))
print(validate_number(123213))
print(validate_number(12345))
print(validate_number(1234567))
print(validate_number(223450))
print(validate_number(123789))
print(validate_number(112233))
print(validate_number(123444))
print(validate_number(111122))

count = 0

for i in range(236491, 713788): # replace your numbers here
	if validate_number(i):
		count+=1

print(count)