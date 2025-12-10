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

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
