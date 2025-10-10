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
