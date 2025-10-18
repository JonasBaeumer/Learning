# Example 1: Factorial Calculation
# This code defines a recursive function to calculate factorial 
# of a number, where function repeatedly calls itself with smaller
# values until it reaches the base case.

# What is the base case? We reached the last number we can multiply (e.g. 1)
# or else whole computation becomes 0

def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
        
print(factorial(4))
