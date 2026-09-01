

from typing import List, Optional, Dict, Set

#  Squares of a Sorted Array

# LeetCode: https://leetcode.com/problems/-squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i,j = 0,n-1       # initialized pointers 
        result = [0]*n    # initialized result arrays for easy indexing  

        for k in range(n-1,-1,-1):  #k starts at n-1 decreasing till 0
            
            if nums[i]**2 > nums[j]**2:
                result[k] = nums[i]**2
                i += 1
            else:
                result[k] = nums[j]**2
                j -= 1
        return result     
        
# --- Driver Code for Local Testing ---

if __name__ == "__main__":
    sol = Solution()
    result = sol.sortedSquares([-4,-3,1, 2, 3])
    print(f"Result: {result}")

