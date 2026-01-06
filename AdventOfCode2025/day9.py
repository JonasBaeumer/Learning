"""
First idea: We can mathematically calculate the actual size of the rectacle by calculating all combinations of points 
We then keep the max value.

Question: How do I calculate the surface of a rectangle using two points?
"""

tiles = []
filepath = '/Users/jonas/Downloads/input-9.txt'
with open(filepath, "r") as file:
	for line in file:
		coordinates = line.strip().split(',')
		tiles.append((int(coordinates[0]), int(coordinates[1])))
print(tiles)
