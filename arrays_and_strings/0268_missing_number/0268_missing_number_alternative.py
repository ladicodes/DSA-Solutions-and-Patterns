from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Step 1: n is exactly the length of the array
        n = len(nums)
        
        # Step 2: Calculate expected sum using Gauss's formula
        expected_sum = (n * (n + 1)) // 2
        
        # Step 3 & 4: The difference between expected and actual sum is the missing number
        return expected_sum - sum(nums)
