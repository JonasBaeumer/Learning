"""
Approach:
	1) We need to splitt the input into three different datastructures respectively:
		- indicator light diagramme []
		- button wiring schematics ()
		- joltage requirements {}
	2) We start with an initial state of an empty lighting configuration (e.g. ...). We then perform BFS on the states using a queue until we find a solution
"""

"""
Helper function that uses regex to splitt our incoming string
"""
def _parse_string(line: str):
	# 1. Find indicator light diagramme
	pattern = re.search(r'\[([#.]+)\]', line).group(1)
	
	# 2. Extract button specifications
	button_texts = re.findall(r'\((.*?)\)', line)
	
	# 3. Extract jolts (for later)
	jolts_text = re.search(r'\{(.*?)\}', line).group(1)
	
	buttons = []
	for bt in button_texts:
		buttons.append([int(x) for x in bt.split(",")])
	
	jolts = [int(x) for x in jolts_text.split(",")]

	return pattern, buttons, jolts

"""
Helper method to flip a string using a given button command
"""
def _flip_string(line: str, lights: list[int]):
	line = line
	for light in lights:
		if line[light] == '#':
			line = line[:light] + '.' + line[light+1:] 
		else:
			line = line[:light] + '#' + line[light+1:]
	return line

test_string = '...'
print(_flip_string(test_string, [1]))
print(_flip_string(test_string, [1,2]))
	

import re
filepath = '/Users/jonas/Downloads/input-10.txt'

with open(filepath, 'r') as file:
	for line in file:
		line.strip()
		# 1) We have to splitt each line into the proper datastructures by using regex
		_parse_string(line.strip())
		
		
