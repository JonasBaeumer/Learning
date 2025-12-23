"""
1. We have to create a two grid array first
"""

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

ops_array = []
filepath = '/Users/jonas/Downloads/input-6.txt'
with open(filepath, "r") as f:
	# Create the 2D array 
	for line in f:
		ops_array.append(line.strip().split())

result = 0
for i in range(len(ops_array[0])):
	calculation = []
	for j in range(len(ops_array)):
		calculation.append(ops_array[j][i])
	print(calculation)
	result += part_one(calculation)
print(result)
#print(ops_array[len(ops_array)-1])
