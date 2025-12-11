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

def add_and_shift(numbers, value):
	for i in range(len(numbers)):
		if value >= numbers[i]:
			tmp = numbers[i]
			numbers[i] = value
			value = tmp
		else:
			break

	return numbers

print(add_and_shift([2,3,4,2,3,4,2,3,4,2,7,8], 4))
print(add_and_shift([4,3,4], 6))
print(add_and_shift([2,3,4,5,1],3))


def highest_voltage_2(bank: str) -> int:
	numbers = list(map(int, bank[-12:]))
	prefix = bank[:-12]
	for digit in prefix[::-1]:
		numbers = add_and_shift(numbers,int(digit))
	return int("".join(str(d) for d in numbers))

filepath = "/Users/jonas/Downloads/input-3.txt"
total_sum = 0
with open(filepath, "r") as f:
	for line in f:
		line = line.strip()
		number = highest_voltage_2(line)
		total_sum += number
print(total_sum)
		
