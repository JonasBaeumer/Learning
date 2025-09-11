# Naive approach
# Runtime: O(n) + O(n log n) + O(k) = O(n log n + k)
# Spacetime: O(n) + O(k) = O(n + k)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        memory = {}

        for number in nums:
            if number in memory:
                memory[number] += 1
            else:
                memory[number] = 1
        
        # sort dictionary

        sorted_memory = sorted(memory.items(), key=lambda x:x[1], reverse=True)
        counter = 0
        final = []
        while(counter < k):
            final.append(sorted_memory[counter][0])
            counter+=1
        return final
