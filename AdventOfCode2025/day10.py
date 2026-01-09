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
	
"""
Main method to determine the shortest path for a given machine
"""
def find_shortest_path_for_machine(goal_state: str, instructions: list[list[int]]):
	start_state = "." * len(goal_state)
	visited = set()
	queue = deque()

	queue.append((start_state, 0))
	while queue:
		state, index = queue.popleft()
		visited.append(state)
		
		for instruction in instructions:
			new_state = _flip_string(state, instruction)
			if new_state == goal_state:
				return index
			else:
				if new_state not in visited:
					queue.append(new_state, index + 1)
	# We couldnt find any working solution to reach the goal state
	return -1
	
print(find_shorte

import re
filepath = '/Users/jonas/Downloads/input-10.txt'

with open(filepath, 'r') as file:
	for line in file:
		line.strip()
		# 1) We have to splitt each line into the proper datastructures by using regex
		_parse_string(line.strip())
		
		
