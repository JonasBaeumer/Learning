# Invalid ID requirements
# - Any ID which is consist only of a sequence of digits repeated twice
# Ex: 11-22 range, contains 11, 22 which are both illegal (1, 1) and (2, 2)
# - No number has leading 0s (no ID at all)
# Ex: 0101 no ID (but should not appear here)

# Main problem: How do we detect the duplicates sequences?
# We could use a sliding window approach that keeps a set in which we store 
# the all numbers that we have already seen, the moment we hit a number from 
# the set again we stop the window and move forward through both sequences 
# to check wether both numbers are the same.
# When do we escape? 
# 1) When one number is different than the other
# 2) We have hit the end of the string on the right side but our left inner pointer has
#    not yet hit the start point of our second sequence (11211 is a valid number)  
"""

"""

filepath = "/Users/jonas/Downloads/input-2.txt"

# Read out intervalls 
with open(filepath, "r") as f:
	for line in f:
		ranges = line.split(",")

# Break down ranges into intervalls
for range in ranges:
	range_edges = range.split("-")
	print("left_edge: " + range_edges[0] + " right_edge: "
+ range_edges[1])


