"""
1) Split the input data apart into the grids and shapes sections
	grid 	-> List[List[str]]
	regions -> tuples(int, int, List[int])]
"""

filepath = "/Users/jonas/Downloads/input-12.txt"

import re

shape_header_re = re.compile(r'^(\d+):$')
shape_row_re = re.compile(r'^[#.]+$')
region_re = re.compile(r'^(\d+)x(\d+):\s+([\d\s]+)$')

counter = 0
read_row = True

grid = []
regions = []

with open(filepath, "r") as file:
	
	grid_list = []

	for line in file:
		print(line.strip())
		if not line:
			continue
		
		m = shape_header_re.match(line)
		if m:
			# we have three lines below that are the shape
			read_row = True
		elif read_row:
			if counter >= 3:
				grid.append(grid_list)
				grid_list = []
				counter = 0
				read_row = False
			else:
				grid_list.append(list(line.strip()))
				counter += 1
		m = region_re.match(line)
		if m:
			w = int(m.group(1))
			h = int(m.group(2))
			counts = list(map(int, m.group(3).split()))
			regions.append((w, h, counts))	

print(grid)
