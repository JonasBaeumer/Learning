"""
Initial idea: Just count the number of splitters in the diagram to determine how many times the beam was split (each splitter produces one new beam)
Problem (why it doesnt work): We can guarantee that all of the splitters in the diagram are actually hit, so we have to simulate the beams
flowing through the diagram first before counting how many splitters were actually hit. 

New approach: Simulate the beams flowing through the diagram. Then calculate how many splitters have an incoming beam (e.g. on top of them)
That will give us the total number of beams hit. 
"""

# 1) Simulate beam flow through diagram
"""
Approach: Go from diagram row by row, if you hit a splitter, check if it has an incoming beam on top, then change field left and right of beam 
to '|'. -> This just simulated splitter.

Which behaviors do I need to be aware of? 
-> Splitters need to have incoming beam to split light 
	-> If I splitt the light I have to be careful not to overwrite splitters on the side
-> When propagating beams downward
	-> Make sure to avoid overwriting a splitter below with a beam of light 

Edge cases: Check if out of bounds, then nothing happens
"""
def simulate_beams(diagram: list[list[str]]) -> (int, list[list[str]]):
	beam_counter = 0
	# Go through each line
	for i in range(len(diagram)): 
		for j in range(len(diagram[0])):
			# Check if field is beam ('|'), splitter ('^') or empty space ('.')
			if diagram[i][j] == '^':
			# If splitter:
				# We check if splitter has incoming beam on top of it
				if i > 0 and diagram[i-1][j] == '|': 
					beam_counter += 1
					# If yes -> We check if left, right has empty space
					# If empty space -> replace with light beam
					if j - 1 >= 0 and diagram[i][j-1] == '.':
						diagram[i][j-1] = '|'
					if j + 1 < len(diagram[i]) and diagram[i][j+1] == '.':
						diagram[i][j+1] = '|'
			# If Empty space:
			elif diagram[i][j] == '.':
				# We check is space above has beam:
				if i > 0 and diagram[i-1][j] == '|':
					# If yes change field to beam to pass it down
					diagram[i][j] = '|'
			# Remember to check for S (start point in first row)
			if i == 0 and diagram[i][j] == 'S':
				diagram[i][j] = '|'
			# If beam: Nothing

	return (beam_counter,diagram)
	
# Part 2: Explore all possible options
"""
Idea: I can use the diagram for part I as the base map of all possible scenarios / paths 
from particles through the space. Now I just need to start from the top and count all 
possible paths to the end. Essentially a recursive dfs search through the "tree". 

Essentially we have a splitt whenever we hit a splitter branch ('^') as we can then decide to go
either left or right (e.g. two decisions).

What is our base case? When we have reached the end of the diagram with our beam / we would 
step out of bounds so then we return 1 (to signal that we have hit the end of the path). For 
the internal dfs method we give the starting point i,j for the diagram as input and go downwards
from there. 
"""

from 

def explore_with_tachyon_manifold(diagram: list[list[str]]) -> int:
	
	@cache
	def dfs(start_x, start_y):
		# Base case: We have reached out of bounds
		# Only valid if we step out of bounds at bottom not left/right
		if start_y < 0 or start_y >= len(diagram[0]):
			return 0 # -> We stepped out of bounds to the side
		# We have reached the bottom end of the diagram
		if start_x >= len(diagram):
			return 1
		# Continue basic exploration since we are not done
		# check if our field is a splitter
			# if yes splitt search recursively to left and right 
		# check if our field is beam
			# continue search directly below

filepath = '/Users/jonas/Downloads/input-7.txt'
diagram = []
with open(filepath, 'r') as file:
	for line in file:
		diagram.append(list(line.strip()))

result, diagram = simulate_beams(diagram)
print(diagram)
	

