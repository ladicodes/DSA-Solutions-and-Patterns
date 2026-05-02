'''

Code
Testcase
Test Result
Test Result
88. Merge Sorted Array
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
'''
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # i: index of last valid element in the initial part of nums1
        i = m - 1
        # j: index of last element in nums2
        j = n - 1
        # k: index where we should place the next largest element in nums1
        k = m + n - 1

        # Merge from the back: place the larger of nums1[i] and nums2[j] at nums1[k]
        while i >= 0 and j >= 0:
            # If current element in nums1 is bigger, move it to position k
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1  # shrink nums1 pointer leftward
            else:
                # Otherwise take element from nums2 and place it at k
                nums1[k] = nums2[j]
                j -= 1  # shrink nums2 pointer leftward
            k -= 1  # move placement pointer left after each placement

        # If there are remaining elements in nums2, copy them over.
        # (No need to copy remaining nums1 elements because they are already in place.)
        while j >= 0:
            nums1[k] = nums2[j]  # copy remaining item from nums2
            j -= 1
            k -= 1

# Walkthrough Example:
# nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Start pointers: i=2 (value 3), j=2 (value 6), k=5
# Step 1: compare 3 and 6 -> place 6 at nums1[5] -> nums1 becomes [1,2,3,0,0,6]
# Step 2: i=2, j=1 (value 5), k=4 -> compare 3 and 5 -> place 5 at nums1[4]
# Step 3: continue until nums2 is exhausted or merged; final nums1 = [1,2,2,3,5,6]

# Time Complexity: O(m + n) — each element from both arrays is visited at most once.
# Space Complexity: O(1) — we modify nums1 in place without extra arrays.