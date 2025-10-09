# We could try to sort the array first, however not optimal approach that would only work under some 
# constraints as sorting (for example using sorted() has n log n runtime)
# Can we solve this with using the unsorted array?
# Approach: Transform array into a set, which gives us O(1) lookup time for each element
# Then we can loop through the set and for each element check wether the i+1 is also in the 
# set, if that is the case we have a subsequence, and can check for the next element, etc.
# Small catch: To avoid any duplicate work, we have to make sure that we are checking for a
# given element in the array wether this is the smallest or the beginning of the subsequence
# because if it is not we are checking a subsequence of the longest sequence of this, which in the 
# worst case can lead to O(n^2). Therefore if i-1 in set do nothing, because we are only looking at
# a subset right now. Also duplicates are not a problem, because set removes them
# Runtime: O(n) + O(n) + O(1) = O(n)
# Spacetime: O(n) + O(3) = O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest_sequence = 0
        current_sequence = 0
        current_value = 0

        for num in numbers:
            if num in numbers:
                current_value = num
                current_sequence = 1
                if current_value-1 in numbers:
                    continue
                elif current_value+1 in numbers:
                    current_sequence += 1
                    current_value += 1

                    while(current_value+1 in numbers):
                        current_sequence+=1
                        current_value+=1

                if current_sequence > longest_sequence:
                    longest_sequence = current_sequence

        return longest_sequence
