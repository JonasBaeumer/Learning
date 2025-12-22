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
print(result)
		
		
