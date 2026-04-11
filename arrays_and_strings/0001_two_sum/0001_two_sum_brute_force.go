// Two Sum - Brute Force Approach
//
// Given an array of integers nums and an integer target, return indices of the
// two numbers such that they add up to target.
//
// You may assume that each input would have exactly one solution, and you may
// not use the same element twice.
//
// You can return the answer in any order.
//
// This approach checks every possible pair without using extra space.
// It is the naive solution before optimizing with a hashmap.

package twosum

func twoSumBruteForce(nums []int, target int) []int {
	// Outer loop picks the first element of the pair.
	for i := range nums {
		// Inner loop picks the second element, always ahead of i.
		for j := i + 1; j < len(nums); j++ {
			// Check if this pair sums to the target.
			if nums[i]+nums[j] == target {
				return []int{i, j}
			}
		}
	}

	// No valid pair found (problem guarantees one always exists).
	return []int{}
}

/*
Step by Step Example

nums   = [2, 7, 11, 15]
target = 9

Step 1: i=0, j=1 → 2 + 7  = 9  ✓ Found!
Return: [0, 1]

(If it hadn't matched here, the loop would continue checking)
Step 2: i=0, j=2 → 2 + 11 = 13 ✗
Step 3: i=0, j=3 → 2 + 15 = 17 ✗
Step 4: i=1, j=2 → 7 + 11 = 18 ✗
... and so on until a match is found.

Time Complexity:  O(n²) — every pair is checked in the worst case
Space Complexity: O(1)  — no extra data structures used
*/
