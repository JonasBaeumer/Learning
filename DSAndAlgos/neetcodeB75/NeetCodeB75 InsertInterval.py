# Intervalls are non overlapping in the beginning
# Add intervall such that still sorted and intervalls are not overlapping
# Initial approach: Loop over intervalls and check wether we have to merge or can just add
# -> First do in new list then later do it in place for O(1) extra space
# Do we need two pointers here? Actually no, we can just use one pointer and always do a left sided merge
# Algo:
"""
create new list
Loop over list (with two pointers):
    Does intervall need to be added or merged?
        If yes: Four scenarios
            1. Appointment can be added before new appointment
            2. Appointment needs to be merged with left 
        If no -> Can just add interval[i] and move on
"""

#Runtime: O(n) 
#Space: O(n) duplicate list not done in place
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_start, new_end = newInterval
        inserted = False

        for start, end in intervals:
            # Case 1: current interval is completely before newInterval (no overlap)
            if end < new_start:
                res.append([start, end])

            # Case 2: current interval is completely after newInterval (no overlap)
            elif start > new_end:
                if not inserted:
                    res.append([new_start, new_end])
                    inserted = True
                res.append([start, end])

            # Case 3: overlap → merge into newInterval
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)

        # If newInterval goes at the very end and hasn't been inserted yet
        if not inserted:
            res.append([new_start, new_end])

        return res
