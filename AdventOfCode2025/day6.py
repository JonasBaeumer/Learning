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

Why did first appproach for part II fail? Because we removed empty spaces in the string which stould have stay part of the calculation. 
Problem: Single or multi digit numbers do not always stay in the same position below / compared to a larger number. Therefore, we need 
to ensure that we check the relative subcolumn that a small than max length number has to be placed. Example 
"325" and "8" means that 8 can be placed in three relative positions which determines which number it will be added to. 

New approach: We first need to read out the last line with all the operation to determine the length of gaps then we can determine which spaces are actually subcolumn spaces 
In total we have 5 rows (last one has the operators)
"""

ops_array = []
filepath = '/Users/jonas/Downloads/input-6.txt'
with open(filepath, "r") as f:
	# Create the 2D array 
	for line in f:
		ops_array.append(line.rstrip("\n"))

def build_problem_spans_from_ops_row(ops_row: str, sep_min=2):
	spans = []
	n = len(ops_row)
	i = 0

	while i < n:
		# skip separator spaces (2+ spaces)
		j = i
		if ops_row[i] == ' ':
			j = i
		while j < n and ops_row[j] == ' ':
			j += 1
			if (j - i) >= sep_min:
				i = j
				continue
		start = i
		i += 1
		while i < n:
			if ops_row[i] == ' ':
				j = i
				while j < n and ops_row[j] == ' ':
					j += 1
				if (j - i) >= sep_min:
					break 
			# else: single space → keep going inside chunk
			i += 1
		end = i
		spans.append((start, end))

	return spans

distances = []
counter = 0
for i in range(len(ops_array[4])):
	if ops_array[4][i] != ' ':
		distances.append(counter) 
		counter = 0
	else:
		counter += 1	

# Now get break our string apart and seperate them based on the actual length of the column 
def split_row(s: str):
	# pad to same width as operator row so slicing never OOB
	if len(s) < len(ops_array[4]):
		s = s.ljust(len(ops_array[4]))

	chunks = []
	for start, end in spans:
		chunk = s[start:end]          # keep internal spaces (subcolumn alignment)
		chunks.append(chunk)
	return chunks

spans = build_problem_spans_from_ops_row(ops_array[4], sep_min=2)
chunked = [split_row(row) for row in ops_array]
print(chunked[0])

from math import prod

def eval_problem_columnwise(problem_rows: list[str], op_row_chunk: str) -> int:
	"""
	problem_rows: list of strings (same width), one per row of digits (NOT including operator row)
	op_row_chunk: the operator chunk string for this problem (contains '+' or '*', plus spaces)

	Returns the evaluated result for this one problem.
	"""
	if not problem_rows:
		return 0

	width = len(problem_rows[0])

	# operator is the one non-space char in this chunk
	op = next((ch for ch in op_row_chunk if ch in "+*"), None)
	if op is None:
		raise ValueError(f"No operator found in chunk: {repr(op_row_chunk)}")

	numbers = []
	# Read columns right-to-left
	for c in range(width - 1, -1, -1):
		digits = []
		# Digits top-to-bottom in that column (skip spaces)
		for r in range(len(problem_rows)):
			ch = problem_rows[r][c]
			if ch != " ":
				digits.append(ch)

	if digits:  # this column actually forms a number
		numbers.append(int("".join(digits)))

	# Now evaluate
	if op == "+":
		return sum(numbers)
	else:  # '*'
		return prod(numbers)


def eval_all_problems(chunked: list[list[str]]) -> int:
	"""
	chunked[row][problem] = string chunk for that problem at that row.
	Assumes last row is the operator row.
	"""
	num_rows = len(chunked)
	num_probs = len(chunked[0]) if num_rows else 0

	total = 0
	for p in range(num_probs):
		problem_rows = [chunked[r][p] for r in range(num_rows - 1)]   # all digit rows
		op_chunk = chunked[num_rows - 1][p]                      # operator row chunk
		total += eval_problem_columnwise(problem_rows, op_chunk)

	return total

print(eval_all_problems(chunked))


"""
result = 0
#ops_array = [
#	['123', '328', '51', '64'],
#	['45', '64', '387', '23'],
#	['6', '98', '215', '314'],
#	['*', '+', '*', '+']
#]
#num_rows = len(ops_array)
#num_cols = len(ops_array[0])

for i in range(len(ops_array[0])):
	calculation = []
	for j in range(len(ops_array)):
		calculation.append(ops_array[j][i])
	#print(calculation)
	result += part_one(calculation)
print(result)
print(result)
#print(ops_array[len(ops_array)-1])
"""
