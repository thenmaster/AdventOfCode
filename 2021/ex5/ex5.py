import sys

class Point(object):
	"""docstring for Point"""
	def __init__(self, x: int, y:int):
		super(Point, self).__init__()
		self.x = x
		self.y = y

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def __eq__(self, other):
		return (self.x == other.x) and (self.y == other.y)

	def __hash__(self):
		return hash((self.x, self.y))

	def __ne__(self, other):
		return not(self == other)

	def __str__(self):
		return str((self.x, self.y))

	def __repr__(self):
		return str((self.x, self.y))

def add_or_increment_point(point: Point):
	global field
	if point in field:
		field[point] += 1
	else:
		field[point] = 1

if len(sys.argv) < 2:
	print("Usage: python3 ex5.py <filename>")
	quit()

filename = sys.argv[1]

field = {}

#parse input
with open(filename) as file:
	for line in file:
		points = tuple(map(lambda x: tuple(map(lambda y: int(y), x.split(","))), line.strip().split(" -> ")))
		
		#ends of line
		start = Point(points[0][0], points[0][1])
		end = Point(points[1][0], points[1][1])

		if start.get_x() == end.get_x():
			add_or_increment_point(start)
			add_or_increment_point(end)

			diff = abs(start.get_y() - end.get_y())
			less = min(start.get_y(), end.get_y())

			for i in range(less+1, (less+diff)):
				point = Point(start.get_x(), i)
				add_or_increment_point(point)
		elif start.get_y() == end.get_y():
			add_or_increment_point(start)
			add_or_increment_point(end)

			diff = abs(start.get_x() - end.get_x())
			less = min(start.get_x(), end.get_x())

			for i in range(less+1, (less+diff)):
				point = Point(i, start.get_y())
				add_or_increment_point(point)
		else:
			print("Part 1 ignore line " + line)
			continue

intersects = dict(filter(lambda x: x[1] >=2, field.items()))
print(field)
print(intersects)
print("Part 1: " + str(len(intersects)))

print() #For output separation

field = {}

#parse input
with open(filename) as file:
	for line in file:
		points = tuple(map(lambda x: tuple(map(lambda y: int(y), x.split(","))), line.strip().split(" -> ")))
		
		#ends of line
		start = Point(points[0][0], points[0][1])
		end = Point(points[1][0], points[1][1])

		if start.get_x() == end.get_x():
			add_or_increment_point(start)
			add_or_increment_point(end)

			diff = abs(start.get_y() - end.get_y())
			less = min(start.get_y(), end.get_y())

			for i in range(less+1, (less+diff)):
				point = Point(start.get_x(), i)
				add_or_increment_point(point)
		elif start.get_y() == end.get_y():
			add_or_increment_point(start)
			add_or_increment_point(end)

			diff = abs(start.get_x() - end.get_x())
			less = min(start.get_x(), end.get_x())

			for i in range(less+1, (less+diff)):
				point = Point(i, start.get_y())
				add_or_increment_point(point)

		elif abs(start.get_y() - end.get_y()) // abs(start.get_x() - end.get_x()) == 1:

			add_or_increment_point(start)
			add_or_increment_point(end)
			#45º angle
			vector = ((end.get_x() - start.get_x()) // abs(end.get_x() - start.get_x()),
			 (end.get_y() - start.get_y()) // abs(end.get_y() - start.get_y()))
			
			new_point = Point(start.get_x() + vector[0], start.get_y() + vector[1]) 
			while new_point != end:
				add_or_increment_point(new_point)
				new_point = Point(new_point.get_x() + vector[0], new_point.get_y() + vector[1]) 
		else:
			raise ValueError("Non 45º diagonal line!")

		# print(line.strip())
		# print(field)
		# input()

intersects = dict(filter(lambda x: x[1] >=2, field.items()))
print(field)
print(intersects)
print("Part 2: " + str(len(intersects)))