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