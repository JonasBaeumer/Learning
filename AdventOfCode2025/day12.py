"""
1) Split the input data apart into the grids and shapes sections
	grid 	-> List[List[str]]
	regions -> tuples(int, int, List[int])]

2) Use some form of backtracking / DFS algorithm to solve this 

2a) First supapproach, we can narrow down the list of available fields to check, even if all shapes would fit perfectly with no breaks, 
would there even be enough space in the grid to place them?
"""

"""
This method determines wether a field even has enough place to fit the required shapes if there are all spaces perfectly (no gaps)
"""
def _enough_available_space(a: int, b: int, quantities: list[int]) -> bool:
	space = [5, 7, 7, 7, 7, 7]
	area = a * b
	sum = 0

	for i in range(len(quantities)):
		sum += (quantities[i] *	space[i])
	
	return sum <= area



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
			print(_enough_available_space(w, h, counts))
sum = 0
for region in regions:
	sum += _enough_available_space(region[0], region[1], region[2])
print(sum)
