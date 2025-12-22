filepath = '/Users/jonas/Downloads/input-5.txt'


"""
TODO: We want to check wether the second part of the list of available ingredient IDS fall within any of the specified ingredient
lists above. 
First step: break down the input into the two parts (intervalls, and ingredient IDs)
Second step: create two datastructures from these blocks
"""

id_ranges = []
ingredient_ids = []
reached_ingredients = False

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
		ingredient_ids.append(int(line.strip()))
	print(ingredient_ids[0])
	print(id_ranges[0])
		
