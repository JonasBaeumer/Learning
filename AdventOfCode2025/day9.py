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
"""
This method that all points in a straight line between two points to the set. Important we also include the actual original points 
not just the space in between them (so this is inclusive)
"""
def add_green_points(green_points: set[tuple[int, int]], point_a: tuple[int, int], point_b: tuple[int, int]) -> set[tuple[int, int]]:
	green_points = green_points.copy()
	a_x, a_y = point_a[0], point_a[1]
	b_x, b_y = point_b[0], point_b[1]
	
	if a_x == b_x: # Add y coordinates
		for i in range(min(a_y, b_y), max(a_y, b_y) + 1):
			green_points.add((a_x, i)):
	else: # Add x coordinates
		for i in range(min(a_x, b_x), max(a_x, b_x) + 1):
			green_points.add((i, a_y)):
	return green_points

"""
This method takes a set of red points and checks wether there is a valid list of greenpoints that forms the edges of this rectangle
Important since we can not assume the relative position of the actual edges we are looking at we need to normalize the coordinates 
otherwise our border could be for example through the center (like an X) between the edges.
"""
def find_valid_rectangle_candidates(red_points: list(tuple[int, int]), green_points: set[tuple[int, int]]) -> list(tuple[int, int]):
	valid_rectangles = []
	for i in range(len(red_points)):
		for j in range(i + 1, len(red_points)):
			a_x, a_y = red_points[i]
			b_x, b_y = red_points[j]

			# A (top-left) - D (top-right) - B (bottom - right) - C (bottom - left)
			x1 = min(a_x, b_x)
			x2 = max(a_x, b_x)
			y1 = min(a_y, b_y)
			y2 = max(a_y, b_y)
			a = (x1, y2) # top left
			b = (x2, y1) # bottom right
			c = (x1, y1) # Bottom left
			d = (x2, y2) # top right

			# Now check for each of these points that all the outer borders have green points connected
			valid_rectangle = True			
			# A -> D
			for x in range(a[0], d[0] + 1):
				if (x, a[1]) not in green_points:
					valid_rectangle = False
					break
			# D -> B
			if valid_rectangle:
				for y in range(d[1], b[1] -1, -1):
					if (d[0], y) not in green_points:
						valid_rectangle = False
						break
			# B -> C 
			if valid_rectangle:
				for x in range(b[0], c[0] -1, -1):
					if (x, b[1]) not in green_points:
						valid_rectangle = False
						break
			# C -> A
			if valid_rectangle:
				for y in range(c[1], a[1] + 1):
					if (c[0], y) not in green_points:
						valid_rectangle = False
						break
			if valid_rectangle:
				valid_rectangles.append((red_points[i], red_points[j]))	
	return valid_rectangles

"""
This method goes through the list of points and builds up out green_points set in combination with add_green_points()
"""
def find_green_points(red_points: list(tuple[int, int]), green_points: set[tuple[int, int]]) -> set[tuple[int, int]]:
	for i in range(0, len(red_points)):
		a = red_points[i]
		b = red_points[(i+1) % n]
		green_points = add_green_points(green_points, a, b)
	return green_points 

red_tiles = []
filepath = '/Users/jonas/Downloads/input-9.txt'
with open(filepath, "r") as file:
	for line in file:
		coordinates = line.strip().split(',')
		red_tiles.append((int(coordinates[0]), int(coordinates[1])))
green_points = 
print(find_max_rectangle(red_tiles))
