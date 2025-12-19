"""
- Transform text file into NxN grid that can be iterated over
- Naive approach: For each value take it as center and check all directions
	- Potential edge case: When we are out of bounds (default false)
"""
#grid = [
#        ['.','@','@'],
#        ['.','@','.'],
#        ['@','.','@']
#]

"""
Check a specific field wether it is out of bound or if not if it has a paper role
"""
def check_field(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
        else:
                if grid[i][j] == "@":
                        return 1
                return 0

#print(check_field(0,0))
#print(check_field(0,1))
#print(check_field(0,2))
#print(check_field(1,0))
#print(check_field(-1,-1))

"""
Should return false IF THERE ARE LESS THAN FOUR ROLES IN ADJACENT AREA
"""
def check_adjacent_eight(i, j):
	adjacent_roles = 0
	# Top left -> i-1, j-1
	adjacent_roles += check_field(i-1, j-1)
	# top -> i-1
	adjacent_roles += check_field(i-1, j)
	# top right -> i-1, j+1
	adjacent_roles += check_field(i-1, j+1)
	# left -> j-1
	adjacent_roles += check_field(i, j-1)
	# right -> j+1
	adjacent_roles += check_field(i, j+1)
	# bottom left -> i+1, j-1
	adjacent_roles += check_field(i+1, j-1)
	# bottom -> i+1
	adjacent_roles += check_field(i+1, j)
	# bottom right -> i+1, j+1
	adjacent_roles += check_field(i+1, j+1)
	#print(adjacent_roles)
	return adjacent_roles < 4

#print(check_adjacent_eight(1,1))
#print(check_adjacent_eight(0,0))

filepath = "/Users/jonas/Downloads/input-4.txt"
total_sum = 0
grid = []
with open(filepath, "r") as f:
	for line in f:
		line = line.strip()
		row = list(line)
		grid.append(row)
for i in range(len(grid)):
	for j in range(len(grid[0])):
		if grid[i][j] == '@':
			total_sum += check_adjacent_eight(i,j)
print(total_sum)
#print(grid)
