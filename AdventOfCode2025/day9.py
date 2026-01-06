"""
First idea: We can mathematically calculate the actual size of the rectacle by calculating all combinations of points 
We then keep the max value.

Question: How do I calculate the surface of a rectangle using two points?
"""

def calculate_surface(point_a: tuple[int, int], point_b: tuple[int, int]) -> int
	# First we need to calculate point_c and point_d

	# And then we can calculate the length of two adjacent edges and when we then calculate a * b
	# and that gives us the total surface or the rectangle
	# width  = |x2 - x1|
        # height = |y2 - y1|
        # area = |x2 - x1| * |y2 - y1|
        width = abs(

def find_max_rectangle(tiles: list(tuple[int, int])) -> int:


tiles = []
filepath = '/Users/jonas/Downloads/input-9.txt'
with open(filepath, "r") as file:
	for line in file:
		coordinates = line.strip().split(',')
		tiles.append((int(coordinates[0]), int(coordinates[1])))
print(tiles)
