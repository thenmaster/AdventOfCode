from treelib import Node, Tree

tree = Tree()
tree.create_node("COM", "com")

with open("input.txt") as file:
	line = file.readline()
	while line:
		data = line.strip().split(')')
		if not tree.contains(data[0].lower()):
			tree.create_node(data[0], data[0].lower(), parent="com")
		if tree.contains(data[1].lower()):
			tree.get_node(data[1].lower()).update_bpointer(data[0].lower())
		else:
			tree.create_node(data[1],data[1].lower(), parent=data[0].lower())

		line = file.readline()

count = 0

for node in tree.nodes:
	count += tree.depth(node)

print(count)