from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        least = 1
        
        for i in range(len(nums)):
            num = nums[i]
            if num <= 0:
                continue

            if num == least:
                least = num + 1
            if num > least:
                return least
            
        return least

solution = Solution()
print(solution.firstMissingPositive([-1, 0, 1, 2, 3]))
