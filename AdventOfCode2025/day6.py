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

#print(part_one(['6612', '1526', '583', '922', '+']))	
#print(part_one(['1', '2', '3', '4', '*']))

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

def get_chunk_widths_from_ops_row(ops_row: str):
	"""
	Returns a list of chunk widths, one per problem, based on the operator row.
	Each chunk width includes the trailing spacing up to (but not including) the next operator.
	"""
	ops_positions = [i for i, ch in enumerate(ops_row) if ch in ('+', '*')]
	widths = []
	for idx in range(len(ops_positions)):
		start = ops_positions[idx]
		end = ops_positions[idx + 1] if idx + 1 < len(ops_positions) else len(ops_row)
		widths.append(end - start)
	return widths, ops_positions


def split_line_into_chunks(line: str, ops_positions, widths, total_len):
	"""
	Splits one full row-string into fixed-width chunks aligned to operator positions.
	Keeps internal spaces (important for subcolumns).
	"""
	line = line.rstrip("\n").ljust(total_len)
	chunks = []
	for start, w in zip(ops_positions, widths):
		chunks.append(line[start:start + w])
	return chunks


def build_calculation_from_problem_chunks(problem_chunks, op, right_to_left=True):
	"""
	problem_chunks: list[str] of the SAME problem chunk across rows (numbers rows only, no operator row)
	op: '+' or '*'
	Returns: list like ['4', '431', '623', '+'] (order depends on right_to_left)
	"""
	if not problem_chunks:
		return [op]

	h = len(problem_chunks)              # number of number-rows
	w = max(len(r) for r in problem_chunks)

	# pad each row in this chunk so column indexing is safe
	rows = [r.ljust(w) for r in problem_chunks]

	col_range = range(w - 1, -1, -1) if right_to_left else range(w)

	numbers = []
	for c in col_range:
		digits = []
		for r in range(h):
			ch = rows[r][c]
			if ch != ' ':
				digits.append(ch)
		if digits:  # ignore empty subcolumns
			numbers.append("".join(digits))

	return numbers + [op]


def parse_worksheet(ops_array):
	"""
	ops_array: list[str] of all rows in the worksheet (last row is operator row).
	Returns: list of calculations, each calculation is a list[str] like ['4','431','623','+']
	"""
	ops_row = ops_array[-1]
	widths, ops_positions = get_chunk_widths_from_ops_row(ops_row)
	total_len = len(ops_row)

	# chunk every row
	chunked_rows = [
		split_line_into_chunks(row, ops_positions, widths, total_len)
		for row in ops_array
	]

	num_rows = len(ops_array) - 1
	num_problems = len(widths)

	calculations = []
	for p in range(num_problems):
		op = chunked_rows[-1][p].strip()   # chunk contains spaces, operator is the non-space char
		problem_chunks = [chunked_rows[r][p] for r in range(num_rows)]
		calc = build_calculation_from_problem_chunks(problem_chunks, op, right_to_left=True)
		calculations.append(calc)

	return calculations

calculations = parse_worksheet(ops_array)

result = 0
for calc in calculations:
	result += part_one(calc)
print(result)
		


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
