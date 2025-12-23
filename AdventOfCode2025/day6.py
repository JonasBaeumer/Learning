"""
1. We have to create a two grid array first
"""

ops_array = []
filepath = '/Users/jonas/Downloads/input-6.txt'
with open(filepath, "r") as f:
	# Create the 2D array 
	for line in f:
		ops_array.append(line.strip().split())

for j in range(len(ops_array)):
	print(ops_array[j][0])
#print(ops_array[len(ops_array)-1])
