"""
This method performs the operation on all the numbers in the array
The last field always contains the operator
"""
def part_one(calculation: list[str]) -> int:
	result = int(calculation[0])
	operator = calculation[len(calculation)-1]
	for i in range(1,len(calculation)-1):
		if operator == '+':
			result += int(calculation[i])
		elif operator == '*':
			result *= int(calculation[i])
		else:
			return 0
	return result

print(part_one(['6612', '1526', '583', '922', '+']))	
print(part_one(['1', '2', '3', '4', '*']))

"""
For part two we now need to change how we read in the numbers, in particular instead of reading in the normal rows we now need to construct
the calculation rows by reading each column multiple times, meaning that we read them over an over per column to construct the numbers for
the calculation properly. 
Ex: We have a column 31, 12, 431
	-> Read column once: only 4, read twice 123, read three times 314, need it 
The good thing: Since we perform the same operation on all number we build from this column due to cummutative property, it does not matter
in which order we actually build the numbers, so we can literally start from the front of the number and then move backwards.  
"""

ops_array = []
filepath = '/Users/jonas/Downloads/input-6.txt'
with open(filepath, "r") as f:
	# Create the 2D array 
	for line in f:
		ops_array.append(line.strip().split())

result = 0
ops_array = [
	['123', '328', '51', '64'],
	['45', '64', '387', '23'],
	['6', '98', '215', '314'],
	['*', '+', '*', '+']
]
num_rows = len(ops_array)
num_cols = len(ops_array[0])

for i in range(num_cols - 1, -1, -1):
	calculation = []
	max_height = max(len(ops_array[row][i]) for row in range(num_rows - 1))
	numbers = [""] * max_height # stable buffer for this column
	for j in range(num_rows - 1):
		token = ops_array[j][i]
		offset = max_height - len(token)
		for l, ch in enumerate(token):
			numbers[offset + l] += ch
		
		print(numbers)
	
	op = ops_array[num_rows - 1][i]
	calculation = numbers + [op]
	numbers = []
	print(part_one(calculation))
	result += part_one(calculation)
print(result)
#print(ops_array[len(ops_array)-1])
