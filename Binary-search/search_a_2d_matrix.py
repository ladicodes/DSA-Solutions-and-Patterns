"""
# lc 74 - search a 2d matrix

# Problem description
Given an m x n integer matrix with the following properties:
1. Each row is sorted in non-decreasing order.
2. The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

# intuition
My initial instinct was a Two-Pass Binary Search: first searching the boundaries of each row to find the row which contains the target, then searching within that row. While this is functional, that approach often requires extra space for mapping or auxiliary arrays. Looking out for an optimal solution, I realized that a matrix is essentially a single sorted list that has been wrapped into rows. By treating it as a 1D array, we can achieve the same result in a single pass with constant space.

# approach
We treat the 2D matrix as a virtual 1D array of length (rows * cols).
1. Initialize two pointers: l = 0 and r = (rows * cols) - 1. 
   - (rows * cols) gives us the total amount of elements in the array
2. In each iteration, calculate the mid index.
   - mid = (l + r) // 2
3. Use the Bridge Formula to map the 1D mid index back to 2D coordinates:
   - row = mid // cols (Determines which row the index falls into)
   - col = mid % cols (Determines the specific column)
4. Compare matrix[row][col] with the target and shrink the search space accordingly.



# walkthrough
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
- Dimensions: rows = 3, cols = 4. Total elements = 12.
- Range: l = 0, r = 11.

Iteration 1:
- mid = (0 + 11) // 2 = 5
- Map to 2D: row = 5 // 4 = 1, col = 5 % 4 = 1.
- matrix[1][1] = 11. Since 11 > 3, set r = mid - 1 = 4.

Iteration 2:
- mid = (0 + 4) // 2 = 2
- Map to 2D: row = 2 // 4 = 0, col = 2 % 4 = 2.
- matrix[0][2] = 5. Since 5 > 3, set r = mid - 1 = 1.

Iteration 3:
- mid = (0 + 1) // 2 = 0
- Map to 2D: row = 0 // 4 = 0, col = 0 % 4 = 0.
- matrix[0][0] = 1. Since 1 < 3, set l = mid + 1 = 1.

Iteration 4:
- mid = (1 + 1) // 2 = 1
- Map to 2D: row = 1 // 4 = 0, col = 1 % 4 = 1.
- matrix[0][1] = 3. Target found! Return True.
"""


# code

class Solution:
    def searchMatrix(self, matrix, target):
    
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, (rows * cols) - 1
        
        while l <= r:
            mid = (l + r) // 2
            # Mapping 1D index to 2D row/col
            row, col = mid // cols, mid % cols
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return False

"""
# time complexity
- Time: O(log(m * n)) — This is a standard binary search over all elements.
- Space: O(1) — We only store a few pointers; no extra data structures used.

# ps: binary search knowledge needed to understand problem
"""