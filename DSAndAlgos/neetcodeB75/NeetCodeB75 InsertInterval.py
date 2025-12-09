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

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervall_processed = False
        new_list = []
        i = 0

        while i < len(intervals):
            start, end = intervals[i]
            # MERGE
            if start <= newInterval[0] <= end or start <= newInterval[1] <= end:
                # Find new bounds
                new_left_bound = min(newInterval[0], start)
                new_right_bound = max(newInterval[1], end)
                # If we overlap the last element we added we have to remove it and merge it
                if len(new_list) != 0:
                    if new_list[len(new_list)-1][0] <= new_left_bound <= new_list[len(new_list)-1][1]:
                        new_left_bound = min(new_list[len(new_list)-1][0], new_left_bound)
                        new_right_bound = max(new_list[len(new_list)-1][1], new_right_bound)
                        new_list.pop()
                new_list.append((new_left_bound, new_right_bound))
            # INSERT
            elif newInterval[1] < start:
                new_list.append(newInterval)
                new_list.append(intervals[i]) 
            else:
                new_list.append(intervals[i])
            i += 1
        return new_list
