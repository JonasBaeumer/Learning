# Runtime: O(n) + O(n) + O(k) = O(2n + k) = O(n)
# Spacetime: O(n) + O(2k) + O(k) = O(n + 3k) = O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

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
