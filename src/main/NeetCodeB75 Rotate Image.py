# Naive approach: Optimized approach, can we make the changes in place?
# Idea: We have two loops and four pointers
# Pointers for layers of matrix (top, bottom), pointers for rotation inside a layer (left, right)
# Outer loop: After each layer is swaped top + 1, bottom - 1, when top > bottom (terminate)
# Inner loop: After each iteration move left + 1 until left == right, then rotation is done
# For the inner loop: Use an offset to iterature through distance between left and right and keep all four pointers as absolute
# Time complexity: n rows, n columns = nxn = O(n^2)
# Space complexity: no new storage, just need to store one value in place, O(1)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        top, bottom = 0, len(matrix) - 1
        while (top <= bottom):
            left, right = top, bottom
            storage = None
            for i in range(right-left):
                # We always store the top left element
                storage = matrix[top][left]

                # Bottom left -> Top left
                matrix[top][left] = matrix[bottom-i][left-i]
                # Bottom right -> Bottom left
                matrix[bottom-i][left-i] = matrix[bottom][right]
                # Top right -> Bottom right
                matrix[bottom][right] = matrix[top+i][right+i]
                # Top left (Storage) -> Top right
                matrix[top+i][right+i] = storage

                left+=1
                right-=1

            
            top+=1
            bottom-=1

# Naive approach: Go through each of the rows one by one in the original matrix and add it as a column in matrix)
# Time complexity: n rows, n columns = nxn = O(n^2)
# Space complexity: 2 matrices with n rows and n columns = n^2 + n^2 = O(n^2)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Go through our initial matrix
        rotated_matrix = [[0] * len(matrix) for _ in range(len(matrix))]
        
        #Iterate through each row one by one
        for row in range(len(matrix)):
            # Iterate through all values in the row 
            for i in range(len(matrix[row])):
                rotated_matrix[i][len(matrix) - 1 - row] = matrix[row][i]

        print(rotated_matrix)
