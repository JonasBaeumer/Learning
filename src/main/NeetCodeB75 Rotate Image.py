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
