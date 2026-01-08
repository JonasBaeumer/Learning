"""
1. Use coordinate compression to map large coordinates to a smaller grid
2. Build a 2D grid marking red points and lines between adjacent red points
3. Use flood fill to mark interior points as green
4. For rectangle validation, only check the perimeter (not all interior points)
5. Find the maximum area rectangle
"""

import signal
import time

class TimeoutError(Exception):
	pass

def timeout_handler(signum, frame):
	raise TimeoutError("Operation timed out after 15 seconds")

def unique_sorted(arr):
	"""Remove duplicates from sorted array"""
	if not arr:
		return []
	result = [arr[0]]
	for i in range(1, len(arr)):
		if arr[i] != arr[i-1]:
			result.append(arr[i])
	return result

def abs(x):
	return x if x >= 0 else -x

def calculate_area(point_a: tuple[int, int], point_b: tuple[int, int]) -> int:
	"""Calculate area of rectangle formed by two opposite corners"""
	width = abs(point_b[0] - point_a[0]) + 1
	height = abs(point_b[1] - point_a[1]) + 1
	return width * height

def is_enclosed(a: tuple[int, int], b: tuple[int, int], grid: list[list[str]], 
                x_map: dict[int, int], y_map: dict[int, int]) -> bool:
	"""
	Check if rectangle formed by points a and b is valid.
	Only checks the perimeter (top/bottom edges and left/right edges).
	This is O(width + height) instead of O(width * height).
	"""
	# Map original coordinates to compressed grid coordinates
	ax, ay = a
	bx, by = b
	
	# Get compressed coordinates
	x1 = min(x_map[ax], x_map[bx])
	x2 = max(x_map[ax], x_map[bx])
	y1 = min(y_map[ay], y_map[by])
	y2 = max(y_map[ay], y_map[by])
	
	# Check top and bottom edges
	for x in range(x1, x2 + 1):
		if grid[y1][x] == '.' or grid[y2][x] == '.':
			return False
	
	# Check left and right edges
	for y in range(y1, y2 + 1):
		if grid[y][x1] == '.' or grid[y][x2] == '.':
			return False
	
	return True

def flood_fill(grid: list[list[str]], start: tuple[int, int]):
	"""Flood fill to mark interior points as green (X) - uses stack (DFS) like Go version"""
	stack = [start]
	directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	
	while stack:
		x, y = stack.pop()  # LIFO (stack) to match Go version
		
		# Skip if already filled or out of bounds
		if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
			continue
		if grid[y][x] != '.':
			continue
		
		grid[y][x] = 'X'
		
		# Add neighbors
		for dx, dy in directions:
			nx, ny = x + dx, y + dy
			if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
				if grid[ny][nx] == '.':
					stack.append((nx, ny))

def get_inside_point(grid: list[list[str]]) -> tuple[int, int]:
	"""
	Find a point inside the polygon using ray casting.
	Casts a ray to the left and counts edge crossings.
	"""
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[y][x] != '.':
				continue
			
			# Cast ray to the left and count edge crossings
			hits = 0
			prev = '.'
			
			for i in range(x, -1, -1):
				cur = grid[y][i]
				if cur != prev:
					hits += 1
				prev = cur
			
			# Odd number of crossings means inside
			if hits % 2 == 1:
				return (x, y)
	
	raise ValueError("No inside point found")

# Set up timeout
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(15)

try:
	start_time = time.time()
	
	# Read input
	red_points = []
	filepath = '/Users/jonas/Downloads/input-9.txt'
	with open(filepath, "r") as file:
		for line in file:
			line = line.strip()
			if not line:
				continue
			coordinates = line.split(',')
			red_points.append((int(coordinates[0]), int(coordinates[1])))
	
	# Coordinate compression: map large coordinates to smaller grid indices
	all_x = sorted([p[0] for p in red_points])
	all_y = sorted([p[1] for p in red_points])
	unique_x = unique_sorted(all_x)
	unique_y = unique_sorted(all_y)
	
	# Create mapping from original coordinates to compressed indices
	x_map = {x: i for i, x in enumerate(unique_x)}
	y_map = {y: i for i, y in enumerate(unique_y)}
	
	# Create compressed grid
	grid = [['.' for _ in range(len(unique_x))] for _ in range(len(unique_y))]
	
	# Map red points to compressed coordinates and mark them
	compressed_points = []
	for orig_point in red_points:
		cx = x_map[orig_point[0]]
		cy = y_map[orig_point[1]]
		grid[cy][cx] = '#'
		compressed_points.append((cx, cy))
	
	# Draw lines between adjacent red points (marking green tiles on the path)
	for i in range(len(compressed_points)):
		a = compressed_points[i]
		b = compressed_points[(i + 1) % len(compressed_points)]
		
		if a[0] == b[0]:  # Vertical line
			y0, y1 = min(a[1], b[1]), max(a[1], b[1])
			for y in range(y0, y1 + 1):
				grid[y][a[0]] = '#'
		elif a[1] == b[1]:  # Horizontal line
			x0, x1 = min(a[0], b[0]), max(a[0], b[0])
			for x in range(x0, x1 + 1):
				grid[a[1]][x] = '#'
	
	# Flood fill interior points
	inside_point = get_inside_point(grid)
	flood_fill(grid, inside_point)
	
	# Find maximum area rectangle
	max_area = 0
	n = len(red_points)
	
	for i in range(n):
		# Check timeout periodically
		if time.time() - start_time > 15:
			raise TimeoutError("Operation timed out")
		
		for j in range(i + 1, n):
			# Check timeout more frequently for large inputs
			if (i * n + j) % 10000 == 0 and time.time() - start_time > 15:
				raise TimeoutError("Operation timed out")
			
			if is_enclosed(red_points[i], red_points[j], grid, x_map, y_map):
				area = calculate_area(red_points[i], red_points[j])
				if area > max_area:
					max_area = area
	
	print(max_area)
	
	# Cancel alarm if we finish successfully
	signal.alarm(0)
	
except TimeoutError as e:
	signal.alarm(0)
	print(f"Error: {e}")
	exit(1)
except Exception as e:
	signal.alarm(0)
	print(f"Error: {e}")
	import traceback
	traceback.print_exc()
	raise
