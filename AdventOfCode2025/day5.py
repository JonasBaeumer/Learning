filepath = '/Users/jonas/Downloads/input-5.txt'


"""
TODO: We want to check wether the second part of the list of available ingredient IDS fall within any of the specified ingredient
lists above. 
First step: break down the input into the two parts (intervalls, and ingredient IDs)
Second step: create two datastructures from these blocks
"""

"""
This method checks wether a given ID is between any intervall in rd_range
"""
def check_ingredient_fresh(id: int, id_range: list[(int, int)]) -> bool:
	for interval in id_range:
		a,b = interval
		if id < a:
			continue
		if a <= id <= b:
			return 1
	return 0

test_range = [(27,273), (300, 320)]
test_id = 302	
print(check_ingredient_fresh(test_id, test_range))

"""
Calculate all fresh IDs that are contained in total
Important: The ranges can overlap so we need to merge overlapping intervalls first
We have sorted the list therefore we know that out starting points must be at least equal, since the right side is bigger that 
leads to two possible scenarios:
A) The intervals do not overlap 
B) The intervals partially overlap. What does that mean?
	If the intervals partially overlap that means that the starting point and/or the endpoint are within the original interval
	If they are there are two possibilities: Either the interval stays the same (since both start and end are contained within interval)
	or we grow the right side of the inveral if the end of the new one is bigger 
"""
def calculate_total_fresh_ids(id_range: list([int, int])) -> int:
	sum = 0
	left,right = (id_range[0][0], id_range[0][1] + 1)
	for i in range (1, len(id_range)):
		interval = id_range[i]
		# print((left,right))
		# 1. Case they dont overlap. We have to add the sum (stop-start) and replace the interval
		if interval[0] >= right:
			sum += (right - left) 
			left,right = (interval[0], interval[1] + 1)
		# 2. They do partially overlap, find out if we need to expand interval or can keep it the same
		if interval[1] + 1 > right:
			right = interval[1] + 1
	sum += (right - left)
	return sum

test_id_ranges = [(1,12), (2,15), (18,19)]
print(calculate_total_fresh_ids(test_id_ranges))


id_ranges = []
ingredient_ids = []
result = 0

with open(filepath, 'r') as f:
	text = f.read().strip()
	blocks = text.split("\n\n")
	# Create id_ranges
	block0_lines = blocks[0].splitlines()
	for line in block0_lines:
		a,b = line.split("-")
		id_ranges.append((int(a), int(b)))
	# Create ingredient_ids
	block1_lines = blocks[1].splitlines()
	for line in block1_lines:
		id = int(line.strip())
		if check_ingredient_fresh(id, id_ranges):
			result += 1
		ingredient_ids.append(id)

# For part II we need to sort the id_ranges
id_ranges.sort(key=lambda x:x[0])
print(calculate_total_fresh_ids(id_ranges))
		
		
