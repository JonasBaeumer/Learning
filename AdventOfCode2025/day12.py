filepath = "/Users/jonas/Downloads/input-12.txt"

with open(filepath, "r") as file:
	for line in file:
		print(line.strip())
