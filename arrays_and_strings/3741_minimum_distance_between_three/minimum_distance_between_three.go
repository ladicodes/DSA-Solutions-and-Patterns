// Minimum Distance Between Same-Value Elements
//
// Given an array of integers nums, return the minimum distance between any two indices
// of the same value that has appeared at least 3 times in the array.
//
// The distance between indices i and j is calculated as 2 * (i - j) where i > j.
// This represents the span between the current occurrence and the second-to-last occurrence,
// multiplied by 2 (possibly representing a custom distance metric).
//
// If no value appears at least 3 times, return -1.
//
// Pattern: Hash Map + Sliding Window (tracking last two occurrences)
//
// Example:
//   Input:  nums = [1, 2, 3, 4, 5, 1, 1]
//   Output: 2
//   Explanation: Value 1 appears at indices [0, 5, 6].
//                Distance = 2 * (6 - 5) = 2
//
// Example:
//   Input:  nums = [1, 0, 1, 4, 1, 3]
//   Output: -1
//   Explanation: No value appears 3 or more times.

package main

func minimumDistance(nums []int) int {
	// Map to store the last two indices of each value.
	// We use a slice to hold either [index] or [prev_index, index].
	lastTwoIndexes := make(map[int][]int)

	minDistance := 1<<31 - 1 // Initialize to max integer value.
	hasGoodTuple := false    // Flag: has any value appeared 3+ times?

	// Iterate through the array.
	for i, value := range nums {
		prev := lastTwoIndexes[value]

		// Case 1: Value not seen before. Initialize with current index.
		if len(prev) == 0 {
			lastTwoIndexes[value] = []int{i}
			continue
		}

		// Case 2: Value seen once before. Now store both indices.
		if len(prev) == 1 {
			lastTwoIndexes[value] = []int{prev[0], i}
			continue
		}

		// Case 3: Value seen twice before. Now we have a valid tuple (3 occurrences).
		hasGoodTuple = true

		// Calculate the distance: 2 * (current - second_to_last).
		// prev[0] is the index of the second-to-last occurrence.
		// i is the index of the current occurrence.
		distance := 2 * (i - prev[0])

		// Update the minimum distance.
		if distance < minDistance {
			minDistance = distance
		}

		// Slide the window: keep only the last two occurrences.
		// Drop prev[0] and keep prev[1] (last) and i (current).
		lastTwoIndexes[value] = []int{prev[1], i}
	}

	// Return the result.
	if hasGoodTuple {
		return minDistance
	}
	return -1
}

/*
Walkthrough Example

nums = [1, 2, 3, 1, 2, 3, 1]

Step 1: i=0, value=1
  prev = []
  Store [0]
  lastTwoIndexes = {1: [0]}

Step 2: i=1, value=2
  prev = []
  Store [1]
  lastTwoIndexes = {1: [0], 2: [1]}

Step 3: i=2, value=3
  prev = []
  Store [2]
  lastTwoIndexes = {1: [0], 2: [1], 3: [2]}

Step 4: i=3, value=1
  prev = [0]
  Store [0, 3]
  lastTwoIndexes = {1: [0, 3], 2: [1], 3: [2]}

Step 5: i=4, value=2
  prev = [1]
  Store [1, 4]
  lastTwoIndexes = {1: [0, 3], 2: [1, 4], 3: [2]}

Step 6: i=5, value=3
  prev = [2]
  Store [2, 5]
  lastTwoIndexes = {1: [0, 3], 2: [1, 4], 3: [2, 5]}

Step 7: i=6, value=1
  prev = [0, 3]
  ✓ Valid tuple found!
  hasGoodTuple = true
  distance = 2 * (6 - 0) = 12
  minDistance = min(INT_MAX, 12) = 12
  Slide: store [3, 6] (drop 0, keep 3 and 6)
  lastTwoIndexes = {1: [3, 6], 2: [1, 4], 3: [2, 5]}

Final: hasGoodTuple = true, so return 12

Time Complexity:  O(n) — single pass through the array
Space Complexity: O(n) — map stores up to n unique values with at most 2 indices each
*/
