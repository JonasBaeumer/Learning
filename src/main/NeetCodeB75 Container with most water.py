# volume = min(bar[i], bar[j]) * dist(bar[i], bar[j])
# Optimized approach: Two pointers
# Idea: Our limiting factor is min(bar[i], bar[j]) so we want to ensure that we want to change 
# the smaller numbers to see a potential change,
# Runtime: O(n)
# Spacetime: O(3) -> O(1) 

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        highest_amount = 0
        
        while (left < right):
            total = min(heights[left], heights[right]) * (right - left)
            if (total > highest_amount):
                highest_amount = total
            if (heights[left] < heights[right]):
                left+=1
            else:
                right -=1

        return highest_amount

# volume = min(bar[i], bar[j]) * dist(bar[i], bar[j])
# Naive approach: Use nested for loop to discover all options
# Runtime: O(n) * O(n) = O(n^2)
# Spacetime: O(1) 

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        highest_amount = 0

        for i in range(len(heights)):
            for j in range(len(heights)):
                total = min(heights[i], heights[j]) * abs(i-j) 
                if (total > highest_amount) and (i != j):
                    highest_amount = total
        
        return highest_amount
