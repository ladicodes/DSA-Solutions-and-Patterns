// 1855. Maximum Distance Between a Pair of Values
//
// Given two non-increasing integer arrays nums1 and nums2, return the maximum
// value of j - i such that i <= j and nums1[i] <= nums2[j].
//
// Example: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5] -> 2

// Strategy: greedy two pointers
// j never resets between iterations of i. As i increases nums1[i] gets smaller,
// so the furthest valid j can only stay the same or move further right — never back.

package arrays

func maxDistance(nums1 []int, nums2 []int) int {
	maxDist := 0
	j := 0

	for i := range nums1 {
		// Extend j as far right as the condition holds for this i.
		for j < len(nums2) && nums1[i] <= nums2[j] {
			j++
		}
		// j is one past the last valid index; enforce i <= j-1.
		if j > i {
			if dist := (j - 1) - i; dist > maxDist {
				maxDist = dist
			}
		}
	}

	return maxDist
}

/*
Walkthrough — nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]

i=0 (55): j advances to 1 (nums2[1]=20 < 55), maxDist = max(0, 0-0) = 0
i=1 (30): j stays at 1 (nums2[1]=20 < 30), j==i -> skip
i=2 (5):  j advances to 5 (all remaining satisfy >=5), maxDist = max(0, 4-2) = 2
i=3 (4):  j already 5 (OOB), maxDist = max(2, 4-3) = 2
i=4 (2):  j already 5 (OOB), maxDist = max(2, 4-4) = 2

Result: 2

Time Complexity:  O(n + m) — i and j each traverse their array at most once
Space Complexity: O(1)
*/
