"""
First idea: We can mathematically calculate the actual size of the rectacle by calculating all combinations of points 
We then keep the max value.

Question: How do I calculate the surface of a rectangle using two points?

Approach for Part II: The key idea is not that dont always have a valid triangle formed between any arbitrary two points, rather
we have specific conditions that fill space. Therefore the new approach is the following:
1) Using the initial list of points in order, we calculate all the green points between them and put them in a set for fast lookup
	Rule: Every two adjacent points in the list from a valid line in between them. 
2) When we now want to check which red points would form a valid triangle, we now have to check wether the complete out border 
of that rectangle is filled with red (or green) points. If yes, then we can deduce the interior is as well and the rectangle 
is a valid candidate 
	Open question: How do we identify red points along the line since they are also valid along the line of two red points
	Proposal: Add the red points to the green point list as well since being red doesnt give us any special advantage when we dont
	look at the respective points as part of the two opposite red edge points
3) Go through the list of all candidates and calculate the max surface (similar to part I)
"""

def calculate_surface(point_a: tuple[int, int], point_b: tuple[int, int]) -> int:
	# First we need to calculate point_c and point_d

	# And then we can calculate the length of two adjacent edges and when we then calculate a * b
	# and that gives us the total surface or the rectangle
	# width  = |x2 - x1|
        # height = |y2 - y1|
        # area = |x2 - x1| * |y2 - y1|
	width = abs(point_b[0] - point_a[0]) + 1
	height = abs(point_b[1] - point_a[1]) + 1
	return width * height

def find_max_rectangle(tiles: list(tuple[int, int])) -> int:
	max_value = 0
	for i in range(len(tiles)):
		for j in range(i+1, len(tiles)):
			max_value = max(max_value, calculate_surface(tiles[i], tiles[j]))
	return max_value


red_tiles = []
filepath = '/Users/jonas/Downloads/input-9.txt'
with open(filepath, "r") as file:
	for line in file:
		coordinates = line.strip().split(',')
		red_tiles.append((int(coordinates[0]), int(coordinates[1])))
print(find_max_rectangle(red_tiles))
