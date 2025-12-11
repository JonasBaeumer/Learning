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

def add_and_shift(numbers, value, remaining, k):
	"""
	numbers: current chosen digits (as a list of ints), in order
	value:   new digit (int) from the bank we are considering
	remaining: how many digits are left AFTER this one in the string
	k:       target length (here: 12)
	"""
	# While:
	# - we have at least one digit in numbers,
	# - if we keep the current last digit AND all remaining digits,
	#   we would still have more than k total → so we are allowed to drop one,
	# - and the last digit is smaller than the new digit,
	#   then drop the last digit to make room for a better (bigger) one.
	while numbers and len(numbers) + remaining > k and numbers[-1] < value:
		numbers.pop()

	# If we still don't have k digits yet, append this one.
	if len(numbers) < k:
		numbers.append(value)

	return numbers

def highest_voltage_2(bank: str) -> int:
	k = 12
	numbers = []
	n = len(bank)

	for i, ch in enumerate(bank):
		digit = int(ch)
		remaining = n - i - 1  # digits left *after* this one
		numbers = add_and_shift(numbers, digit, remaining, k)

		# numbers now holds exactly k digits forming the maximum possible number
	return int("".join(str(d) for d in numbers))

test_string = "987654321111111"
print(highest_voltage_2(test_string))
test_string_2 = "811111111111119"
print(highest_voltage_2(test_string_2))
test_string_3 = "234234234234278"
print(highest_voltage_2(test_string_3))
test_string_4 = "818181911112111"
print(highest_voltage_2(test_string_4))

filepath = "/Users/jonas/Downloads/input-3.txt"
total_sum = 0
with open(filepath, "r") as f:
	for line in f:
		line = line.strip()
		number = highest_voltage_2(line)
		total_sum += number
print(total_sum)
		
