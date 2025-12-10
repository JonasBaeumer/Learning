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
		elif number >= highest_value:
			if highest_value > second_highest:
				second_highest = highest_value
			highest_value = number
	return (highest_value, second_highest)

test_string = "818181911112111"
print(highest_voltage(test_string))
test_string_2 = "811111111111119"
print(highest_voltage(test_string_2))
test_string_3 = "234234234234278"
print(highest_voltage(test_string_3))
test_string_4 = "818181911112111"
print(highest_voltage(test_string_4))
test_string_5 = "8553334231333333322333224115242343435135523343222332535523213448433134323333943412253333331323323432"
print(highest_voltage(test_string_5))
test_string_6 = "2221235222332215222222222212722222334222723221322222522222122222423212222222122124353332123442222223"
print(highest_voltage(test_string_6))

filepath = "/Users/jonas/Downloads/input-3.txt"
total_sum = 0
with open(filepath, "r") as f:
	for line in f:
		line = line.strip()
		n1, n2 = highest_voltage(line)
		total_sum += (n1 * 10 + n2)
print(total_sum)
		
