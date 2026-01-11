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
	new_joltage = joltage.copy() 
	for idx in instruction:
		new_joltage[idx] += 1
	return new_joltage

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

	queue.append((start_state, 0))
	while queue:
		state, index = queue.popleft()
		state_tuple = tuple(state)
		if state_tuple in visited:
			continue
		visited.add(state_tuple)
		
		if state == goal_state:
			return index

		for instruction in instructions:
			new_state = _increase_joltage(state, instruction)
			new_state_tuple = tuple(new_state)
			if any(new_state[i] > goal_state[i] for i in range(len(new_state))):
				continue 
			if new_state_tuple not in visited:
				queue.append((new_state, index + 1))
	return -1

print(find_shortest_path_to_joltage_state([1,1,1], [[0], [1], [2]]))
print(find_shortest_path_to_joltage_state([3,5,4,7], [[3], [1,3], [2], [2,3], [0,2], [0,1]]))


def first_part(machines: list[str]):
	result = 0
	for machine in machines:
		result += find_shortest_path_for_machine(machine[0], machine[1])
	return result

def second_part(machine: list[str]):
	result = 0
	for machine in machines:
		print(result)
		result += find_shortest_path_to_joltage_state(machine[2], machine[1])
	return result

"""
This methods models each button presses and its effects as a matrix for the lp to process
Worst case runtime: O(n^2)
"""
def _transform_parameters_for_lp(buttons: list[list[int]], length: int):
	A = []
	for row in range(length):
		A.append([1 if row in button else 0 for button in buttons])
	return A

import pulp
def pulp_lp_solver(buttons: list[list[int]], b: list[int]):
	A = _transform_parameters_for_lp(buttons, len(b))
	num_buttons = len(b)
	
	# define integer variables, x1...xn
	x = [pulp.LpVariable(f"x{i}", lowBound=0, cat='Integer') for i in range(num_buttons)]
	
	# Define minimization problem
	problem = pulp.LpProblem("Joltage", pulp.LpMinimize)

	# Add constraints: A*x = b
	for row in range(len(A)):
		problem += pulp.lpDot(A[row], x) == b[row]

	# Objective: minimize total presses
	problem += pulp.lpSum(x)
	
	# Solve
	problem.solve()

	print("Solution:")
	for var in x:
		print(var.name, "=", var.value())
	print("Min presses:", pulp.value(problem.objective))

import re
filepath = '/Users/jonas/Downloads/input-10.txt'

machines = []
with open(filepath, 'r') as file:
	for line in file:
		line.strip()
		# 1) We have to splitt each line into the proper datastructures by using regex
		machines.append(_parse_string(line.strip()))
print(machines[0])
# print(second_part(machines))

test_states = [[2, 3], [0, 3], [1, 3], [0, 1, 3]]
test_joltage = [34, 24, 10, 51]

pulp_lp_solver(test_states, test_joltage)


		
		
