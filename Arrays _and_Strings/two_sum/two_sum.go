// Two Sum
//
// Given an array of integers nums and an integer target, return indices of the
// two numbers such that they add up to target.
//
// You may assume that each input would have exactly one solution, and you may
// not use the same element twice.
//
// You can return the answer in any order.

package twosum

func twoSum(nums []int, target int) []int {
	// Create a map to store each number and its index.
	seen := make(map[int]int)

	// Loop through the array with index.
	for i, num := range nums {
		// Calculate the number needed to complete the pair.
		diff := target - num

		// Check if we have already seen the complement.
		if j, found := seen[diff]; found {
			// Return the stored index and the current index.
			return []int{j, i}
		}

		// Store the current number mapped to its index.
		seen[num] = i
	}

	// No valid pair found (problem guarantees one always exists).
	return []int{}
}

/*
Step by Step Example

nums   = [2, 7, 11, 15]
target = 9

Step 1:
  i   = 0
  num = 2
  diff = 9 - 2 = 7

  Have we seen 7? No
  Store: {2: 0}

Step 2:
  i   = 1
  num = 7
  diff = 9 - 7 = 2

  Have we seen 2? Yes → stored at index 0
  Return: [0, 1]

Time Complexity:  O(n) — single pass through the array
Space Complexity: O(n) — map stores at most n entries
*/
