"""1855. Maximum Distance Between a Pair of Values

Given two non-increasing integer arrays nums1 and nums2, return the maximum
value of j - i such that i <= j and nums1[i] <= nums2[j].

Example: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5] -> 2
         (i=2, j=4: nums1[2]=5 <= nums2[4]=5, distance = 4-2 = 2)

Strategy: greedy two pointers
j never resets between iterations of i. As i increases nums1[i] gets smaller,
so the furthest valid j can only stay the same or move further right — never back.
"""


def maxDistance(nums1: list[int], nums2: list[int]) -> int:
    max_dist = 0
    j = 0

    for i in range(len(nums1)):
        # Extend j as far right as the condition holds for this i.
        while j < len(nums2) and nums1[i] <= nums2[j]:
            j += 1
        # j is one past the last valid index; enforce i <= j-1.
        if j > i:
            max_dist = max(max_dist, (j - 1) - i)

    return max_dist


"""
Walkthrough — nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]

i=0 (55): j advances to 1 (nums2[1]=20 < 55), max_dist = max(0, 0-0) = 0
i=1 (30): j stays at 1 (nums2[1]=20 < 30), j==i -> skip
i=2 (5):  j advances to 5 (all remaining satisfy >=5), max_dist = max(0, 4-2) = 2
i=3 (4):  j already 5 (OOB), max_dist = max(2, 4-3) = 2
i=4 (2):  j already 5 (OOB), max_dist = max(2, 4-4) = 2

Result: 2

Why j never resets:
  nums1 is non-increasing, so nums1[i+1] <= nums1[i].
  If nums1[i] <= nums2[j], then nums1[i+1] <= nums2[j] too.
  The valid range for j cannot shrink as i grows.

Time Complexity:  O(n + m) — i and j each traverse their array at most once
Space Complexity: O(1)
"""
