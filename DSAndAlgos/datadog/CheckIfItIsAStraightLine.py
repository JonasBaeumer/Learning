# Runtime O(n)
# Space: O(1)

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        # First two points right to calculate the reference slope
        (x1, y1), (x2, y2) = coordinates[0], coordinates[1]

        # Get cross product components:
        dx = x2 - x1
        dy = y2 - y1

        # For all the reamining points in coordinates:
        for x, y in coordinates[2:]:
            # Check if they are collinear with our earlier cross product 
            if dy * (x - x1) != dx * (y - y1):
            # (essentially: Is the new points on the same line as the first twoon the )
                return False
            
        return True 
