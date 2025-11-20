# Brute Force: Runtime O(n * m)

# Two pointer approach: O(n log n  + m log n) -> 

# is overlap bigger > than duration:
# If yes -> we ahve found our solution 


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        i = 0
        j = 0

        # while the pointers are in bounds:
        while i < len(slots1) and j < len(slots2):

            # Get appointment overlaps (max)
            s1_start_time, s1_end_time = slots1[i]
            s2_start_time, s2_end_time = slots2[j]
            
            start_time = max(s1_start_time, s2_start_time)
            end_time = min(s1_end_time, s2_end_time)

            print(start_time)
            print(end_time)
            if end_time - start_time >= duration:
            # If overlap >= duration:
                return [start_time, start_time + duration]
            
            # Check with pointer we have to move 
            if s1_end_time < s2_end_time:
                i+=1
            else:
                j+=1
            
        # No valid appointments 
        return []
