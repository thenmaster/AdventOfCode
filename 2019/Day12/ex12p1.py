#<x=7, y=10, z=17>
# <x=-2, y=7, z=0>
# <x=12, y=5, z=12>
# <x=5, y=-8, z=6>

# pos = {0 : [7,10,17], 1 : [2,7,0], 2 : [12,5,12], 3 : [5,-8,6]}

pos = {0 : [1,0,2], 1 : [2,10,-7], 2 : [4,8,8], 3 : [3,5,1]}


vel = {key : [0,0,0] for key in range(len(pos))}

print(vel)

for _ in range(10):
	#update velocity

	for i in range(len(pos)):
		for j in range(i+1, len(pos)):
			moon1 = pos[i]
			moon2 = pos[j]
			print(moon1)
			print(moon2)
			print("-------------")
			if moon1[0] < moon2[0]:
				vel[i][0]-=1
				vel[j][0]+=1
			elif moon1[0] > moon2[0]:
				vel[i][0]+=1
				vel[j][0]-=1
			if (moon1[1] < moon2[1]):
				vel[i][1]-=1
				vel[j][1]+=1
			elif moon1[0] > moon2[0]:
				vel[i][1]+=1
				vel[j][1]-=1
			if (moon1[2] < moon2[2]):
				vel[i][2]-=1
				vel[j][2]+=1
			elif moon1[0] > moon2[0]:
				vel[i][2]+=1
				vel[j][2]-=1
	print(vel)
	input()
