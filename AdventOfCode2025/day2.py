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

import sys
filepath = "/Users/jonas/Downloads/input-2.txt"

def check_invalid_id(number: int) -> bool: 
	s = str(number)
	if len(s) % 2 != 0:
		return False
	half = len(s) // 2
	return s[:half] == s[half:]

print(check_invalid_id(198198))
print(check_invalid_id(100101))

# Read out intervalls 
with open(filepath, "r") as f:
	for line in f:
		ranges = line.split(",")

result = 0
# Break down ranges into intervalls
for rang in ranges:
	left_string, right_string = rang.split("-")
	left_edge = int(left_string)
	right_edge = int(right_string)
	for i in range(left_edge, right_edge + 1):
		if check_invalid_id(i):
			result += i
print(result)
result = 0
line = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
ranges = line.split(",")
for rang in ranges:
	left_string, right_string = rang.split("-")
	left_edge = int(left_string)
	right_edge = int(right_string)
	for i in range(left_edge, right_edge + 1):
		if check_invalid_id(i):
			result += i
print(result)

