import copy

current = []

with open("input.txt", "r") as f:
	for l in f.readlines():
		current += [[c for c in l.strip()]]

def pretty_print(layout):
	for line in layout:
		print(line)
	print("====================================")

new = []

EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."

while True:
	new = copy.deepcopy(current)

	for i in range(len(current)):
		for j in range(len(current[i])):
			if current[i][j] == EMPTY:
				if not ((i-1 >= 0 and current[i-1][j] == OCCUPIED) 
					or (i+1 <= len(current)-1 and current[i+1][j] == OCCUPIED)
					or (j-1 >= 0 and current[i][j-1] == OCCUPIED)
					or (j+1 <= len(current[i])-1 and current[i][j+1] == OCCUPIED) 
					or (j+1 <= len(current[i])-1 and i+1 <= len(current)-1 and current[i+1][j+1] == OCCUPIED) 
					or (j-1 >= 0 and i+1 <= len(current)-1 and current[i+1][j-1] == OCCUPIED) 
					or (j+1 <= len(current[i])-1 and i-1 >=0 and current[i-1][j+1] == OCCUPIED)
					or (j-1 >= 0 and i-1 >= 0 and current[i-1][j-1] == OCCUPIED)):
						new[i][j] = OCCUPIED

			if current[i][j] == OCCUPIED:
				total = 0
				if (i-1 >= 0 and current[i-1][j] == OCCUPIED):
					total+=1 
				if (i+1 <= len(current)-1 and current[i+1][j] == OCCUPIED):
					total+=1
				if (j-1 >= 0 and current[i][j-1] == OCCUPIED):
					total+=1
				if (j+1 <= len(current[i])-1 and current[i][j+1] == OCCUPIED):
					total+=1 
				if (j+1 <= len(current[i])-1 and i+1 <= len(current)-1 and current[i+1][j+1] == OCCUPIED): 
					total+=1
				if (j-1 >= 0 and i+1 <= len(current)-1 and current[i+1][j-1] == OCCUPIED):
					total+=1
				if (j+1 <= len(current[i])-1 and i-1 >=0 and current[i-1][j+1] == OCCUPIED):
					total+=1
				if (j-1 >= 0 and i-1 >= 0 and current[i-1][j-1] == OCCUPIED):
					total+=1

				if total>=4:
					new[i][j] = EMPTY

	if new == current:
		break

	current = new


print([item for sub in current for item in sub].count(OCCUPIED))