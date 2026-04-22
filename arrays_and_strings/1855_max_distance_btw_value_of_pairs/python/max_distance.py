from typing import List


class Solution:
    @staticmethod
    def maxDistance(nums1: List[int], nums2: List[int]) -> int:
        #If i less than or equal to j...keep moving j forward till nums1[i] <= nums2[j]
        #else move i forward
        n, m = len(nums1), len(nums2)
        max_dist = 0
        i = 0
        j = 0
        while (i < n and j < m):
            # print("values of i and j", i, j, nums1[i] ,nums2[j])
            if i > j:
                j = i
                if j >= m:
                    break
            if nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                i += 1
        return max_dist
            
if __name__ == "__main__":
    test_cases = [
        ([55, 30, 5, 4, 2], [100, 20, 10, 10, 5]),       # → 2
        ([30,29,19,5], [25,25,25,25,25]),       # → 2
        ([2, 2, 2], [10, 10, 1]),                          # → 1
        ([30, 29, 19, 5], [25, 25, 25, 25, 25]),          # → 2
        ([5, 4, 3, 2, 1], [5, 4, 3, 2, 1]),               # → 0, only i==j valid
        ([1], [1]),                                        # → 0, single element
    ]

    for nums1, nums2 in test_cases:
        print(f"Input:       nums1={nums1}, nums2={nums2}")
        print(f"Output:      {Solution.maxDistance(nums1, nums2)}")
        print("-" * 35)
#     n = 1
# print(f"Input:       nums1={test_cases[1][0]}, nums2={test_cases[1][1]}")
# print(f"Output:      {Solution.maxDistance(test_cases[1][0], test_cases[1][1])}")
# print("-" * 35)