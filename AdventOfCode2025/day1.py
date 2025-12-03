"""
Algorithm:
	Starting number = 0
	Read out the file line by line
	For each line:
		determine direction
		determine step size
		add step size (use helper function)
		if pointer = 0 -> increase counter
	return pointer

For the cycle: assume we step out of bounds
current at 5 we go the left by 6
5 - 6 -> -1
If we are bigger than five, new result is 100 + -1
We have to take into consieration that the number can be multiple times higher than 100 range
Example 578 -> Here we have to take mod 100% to understand the final position where we are going to land
It doesnt matter how many spins around we have to do since we only care about the final position that we land on

"""

def addSteps(direction, steps, current_pointer) -> int:
	number = steps % 100
	if direction == "L":
		result = current_pointer - number
		if result < 0:
			result = 100 - abs(result)
	else:
		result = current_pointer + number
		if result > 99:
			result -= 100
	return result

filepath = "/Users/jonas/Downloads/input.txt"
	
current_position = 50
counter = 0

with open(filepath, "r") as f:
	for line in f:
		line = line.strip()
		direction = line[0]
		steps = int(line[1:len(line)])
		current_position = addSteps(direction, steps, current_position)
		if current_position == 0:
			counter += 1

print(counter)

