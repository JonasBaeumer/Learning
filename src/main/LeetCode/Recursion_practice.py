# Problem:
# Given a non-negative integer n, return the sum of its digits using recursion.

# For example:
#	•	Input: n = 1234
#	•	Output: 10 (since 1 + 2 + 3 + 4 = 10)
# Idea: We can use two operation to extract the relevant number
# We need to first: Get the last digit 
# Second: Remove it before passing the number down
# Basecase n is 0 
# Runtime: O(n), n length of number
# Spacetime: O(n)

def sumOfDigits(n: int) -> int:
    if n == 0:
        return 0
    return n%10 + sumOfDigits(n // 10)
        
print(sumOfDigits(1234))

# Example 2: Fibonacci Sequence
# This code defines a recursive function 
# to calculate nth Fibonacci number, where each number 
# is the sum of the two preceding ones, starting from 0 and 1.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# So fourth fibonacci number is 2 

# What is the base case?: We reach the smallest numbers 0, or 1 because that
# how then build up the sum

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(10))

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
