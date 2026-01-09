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

from collections import deque

def find_shortest_path_for_machine(goal_state: str, instructions: list[list[int]]):
	start_state = "." * len(goal_state)
	visited = set()
	queue = deque()

	queue.append((start_state, 1))
	while queue:
		state, index = queue.popleft()
		visited.add(state)
		
		for instruction in instructions:
			new_state = _flip_string(state, instruction)
			if new_state == goal_state:
				return index
			else:
				if new_state not in visited:
					queue.append((new_state, index + 1))
	# We couldnt find any working solution to reach the goal state
	return -1

def _increase_joltage(joltage: list[int], instruction: list[int]):
	joltage = joltage 
	for i in range(len(joltage)):
		if i in instruction:
			joltage[i] += 1
	return joltage

print(_increase_joltage([0,0,0], [0,2]))
print(_increase_joltage([0,0,0], [0,1]))
print(_increase_joltage([0,0,0], [2]))
print(_increase_joltage([0,0,0], [0,1,2]))

"""
Follow up for part II where we not only now have to hit the final state but hitting it while pressing the right buttons the exact amount of times. 
"""
def find_shortest_path_to_joltage_state(goal_state: list[int], instructions: list[list[int]]):
	start_state = [0] * len(goal_state)
	visited = set()
	queue = deque()

	queue.append((start_state, 1))
	while queue:
		state, index = queue.popleft()
		visited.add((state, index))

		#for instruction in instructions:
	return None


print(find_shortest_path_for_machine("###", [[0], [1], [2]]))
print(find_shortest_path_for_machine(".###.#", [[0,1,2,3,4], [0,3,4], [0,1,2,4,5], [1,2]]))

def first_part(machines: list[str]):
	result = 0
	for machine in machines:
		result += find_shortest_path_for_machine(machine[0], machine[1])
	return result

import re
filepath = '/Users/jonas/Downloads/input-10.txt'

machines = []
with open(filepath, 'r') as file:
	for line in file:
		line.strip()
		# 1) We have to splitt each line into the proper datastructures by using regex
		machines.append(_parse_string(line.strip()))
print(machines[0])
print(len(machines))
print(first_part(machines))
		
		
