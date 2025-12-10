# Two pointer approach
# Initial approach: We use a two pointer approach that grows and shrinks as long as 
# the interval is not 
# [[1,3],[1,5],[6,7]]
# First iteration: i=0, j=1 Overlap or inclusion? YES
#   MOVE RIGHT POINTER
# Second iteration i=0, j=2 Overlap or inclusion? NO
#   MERGE APPOINTMENTS from i to j (2 appointments)
#   RESULT = [[1,5]]
#   MOVE LEFT POINTER
# Third iteration i=1, j=2 Overlap or inclusion? NO
#   MERGE APPOINTMENTS from i to j (1 appointment)
#   RESULT = [[1,5], [6,7]]
#   Since only single appointment attempt to move both pointers by 1
# Growing interval as long as we have overlapping or inclusive appointment range
# After merging set both i=j and move j by one 

# Easier approach:
# Iterate through the list and always compare it with the last present element in our copy list
# Important we got to sort the list before to ensure that we dont have problems with the logic 

# Runtime: O(nlogn)
# Spacetime: O(n)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        copy_list = []

        # 1) Sort intervals by start time to not break implementation
        intervals.sort(key=lambda x: x[0])
        copy_list.append(intervals[0])
        print(intervals)

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            cl_start, cl_end = copy_list.pop()
            # Interval partially overlaps
            if cl_start <= start <= cl_end or cl_start <= end <= cl_end:
                print("partially overlaps")
                new_start = min(start, cl_start)
                new_end = max(end, cl_end)
                copy_list.append([new_start, new_end])
            # Interval is superset of last stored interval
            elif start <= cl_start <= cl_end <= end:
                print("superset")
                copy_list.append([start, end])
            # Value is strictly smaller
            elif end <= cl_start:
                copy_list.append([start, end])
                copy_list.append([cl_start, cl_end])
            # Interval doesnt overlap
            if cl_end < start:
                print("no overlap")
                copy_list.append([cl_start, cl_end])
                copy_list.append([start, end])
        
        return copy_list
