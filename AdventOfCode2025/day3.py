# Read out each line of the battery bank
# Loop over the line and keep a track of currently highest seen digit
# If found digit that is higher than current digit, pass it to second digit, 
# replace first digit

def highest_voltage(bank):
	highest_value = -1
	second_highest = -1
	for digit in bank[::-1]:
		number = int(digit)
		if second_highest == -1:
			second_highest = number
		elif highest_value == -1:
			highest_value = number
		elif number > highest_value:
			if highest_value > second_highest:
				second_highest = highest_value
			highest_value = number
	return (highest_value, second_highest)

test_string = "987654321111111"
print(highest_voltage(test_string))
test_string_2 = "811111111111119"
print(highest_voltage(test_string_2))
test_string_3 = "234234234234278"
print(highest_voltage(test_string_3))
test_string_4 = "818181911112111"
print(highest_voltage(test_string_4))

filepath = "/Users/jonas/Downloads/input-3.txt"
total_sum = 0
with open(filepath, "r") as f:
	for line in f:
		line = line.strip()
		highest_value = -1
		second_highest = -1

		for digit in line[::-1]:
			number = int(digit)
			if number > highest_value:
				second_highest = highest_value
				highest_value = number
			elif number > second_highest:
				second_highest = number
		total_sum += (highest_value + second_highest)
print(total_sum)
		
