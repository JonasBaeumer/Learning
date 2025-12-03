"""
Pseudo Code

Go over the list of instructions and and get first character
First character is either L or R
Then take what is left since that determines how many steps we have to do
If we "overstep" left or right.
Start at 0 if we are coming from right or start at 99 if we come from left
"""

def main():
	filepath = "/Users/jonas/Downloads/input.txt"

	with open(filepath, "r") as f:
    		for line in f: 
        		print(line.strip())   # .strip() removes newline characters
			break

main()	
