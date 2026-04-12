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

function minimumDistance(nums: number[]): number {
	// Map to store the last two indices for each value.
	// Type: Map<number, number[]> where the array contains [prev_index] or [prev_index, current_index]
	const lastTwoIndexes = new Map<number, number[]>();

	let minDistance = Number.MAX_VALUE; // Initialize to maximum possible value.
	let hasGoodTuple = false;          // Flag: has any value appeared 3+ times?

	// Iterate through the array with index and value.
	for (let i = 0; i < nums.length; i++) {
		const value = nums[i];

		// Get the previously stored indices for this value, if any.
		const prev = lastTwoIndexes.get(value);

		// Case 1: Value has not been seen before.
		// Initialize by storing its current index.
		if (!prev) {
			lastTwoIndexes.set(value, [i]);
			continue;
		}

		// Case 2: Value has been seen once (prev contains 1 element).
		// Now we have two occurrences, so store both indices.
		if (prev.length === 1) {
			lastTwoIndexes.set(value, [prev[0], i]);
			continue;
		}

		// Case 3: Value has been seen twice (prev contains 2 elements).
		// Now we have at least 3 occurrences, which satisfies our condition.
		hasGoodTuple = true;

		// Calculate the distance: 2 * (current - second_to_last).
		// prev[0] is the index of the second-to-last occurrence.
		// i is the index of the current occurrence.
		const distance = 2 * (i - prev[0]);

		// Update the minimum distance found so far.
		if (distance < minDistance) {
			minDistance = distance;
		}

		// Slide the window: keep only the last two occurrences.
		// Drop prev[0] and keep prev[1] (last) and i (current).
		lastTwoIndexes.set(value, [prev[1], i]);
	}

	// Return the result based on whether we found a valid tuple.
	return hasGoodTuple ? minDistance : -1;
}

/*
Walkthrough Example

nums = [1, 2, 3, 1, 2, 3, 1]

Step 1: i=0, value=1
  prev = undefined
  Store Map: {1: [0]}

Step 2: i=1, value=2
  prev = undefined
  Store Map: {1: [0], 2: [1]}

Step 3: i=2, value=3
  prev = undefined
  Store Map: {1: [0], 2: [1], 3: [2]}

Step 4: i=3, value=1
  prev = [0]
  prev.length === 1, so store [0, 3]
  Store Map: {1: [0, 3], 2: [1], 3: [2]}

Step 5: i=4, value=2
  prev = [1]
  prev.length === 1, so store [1, 4]
  Store Map: {1: [0, 3], 2: [1, 4], 3: [2]}

Step 6: i=5, value=3
  prev = [2]
  prev.length === 1, so store [2, 5]
  Store Map: {1: [0, 3], 2: [1, 4], 3: [2, 5]}

Step 7: i=6, value=1
  prev = [0, 3]
  prev.length === 2, so we have a valid tuple!
  ✓ hasGoodTuple = true
  distance = 2 * (6 - 0) = 12
  minDistance = min(Number.MAX_VALUE, 12) = 12
  Slide window: store [3, 6] (drop 0, keep 3 and 6)
  Store Map: {1: [3, 6], 2: [1, 4], 3: [2, 5]}

Final: hasGoodTuple = true, so return 12

Time Complexity:  O(n) — single pass through the array
Space Complexity: O(n) — map stores up to n unique values with at most 2 indices each
*/

export { minimumDistance };
