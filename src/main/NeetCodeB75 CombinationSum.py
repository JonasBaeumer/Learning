# Runtime: 
# Spacecomplexity: 
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combination_list = []
        
        def dfs(current_combination, nums, target):
            # Base case:
            if not nums:
                return
            if target == 0:  
                combination_list.append(current_combination)
                return
            if target < 0: # We overshot, so no valid solution can be found
                return
            
            # Else we continue our search
            print(current_combination)
            new_combination = current_combination + [nums[0]]
            left = dfs(new_combination, nums, target - nums[0])
            right = dfs(current_combination, nums[1:], target)
        
        dfs([], nums, target)
        return combination_list

  
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # Base case:
        if target == 0: # 
            return [[]]
        if target < 0: # We overshot, so no valid solution can be found
            return []

        combinations = []
        # We go through our list as a starting point and recursively call the 
        # function with the same list, and target minus current value
        for value in nums:
            sub_combination = self.combinationSum(nums, target - value)
            for combo in sub_combination:
                if sum(combo) + value == target:
                    combinations.append(combo + [value])

        unique = set(tuple(sorted(c)) for c in combinations if sum(c) == target)
        return [list(u) for u in unique]
        # How do ensure to reognize a failure of the previous level return []

        # We have to unwrap the list on each level to append it to the current element before passing it down

        # We need to do a duplicate check to not pass duplicate parameters down
