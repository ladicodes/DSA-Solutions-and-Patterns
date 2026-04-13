// 15. 3Sum
//
// Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
// such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
//
// The solution set must not contain duplicate triplets.

function threeSum(nums: number[]): number[][] {
	// Sort first so two-pointer scanning works in linear time per fixed index.
	nums.sort((a, b) => a - b);

	const result: number[][] = [];

	// Fix one value, then use two pointers on the remaining subarray.
	for (let i = 0; i < nums.length - 2; i++) {
		// Skip duplicate fixed values to avoid duplicate triplets.
		if (i > 0 && nums[i] === nums[i - 1]) {
			continue;
		}

		let left = i + 1;
		let right = nums.length - 1;

		while (left < right) {
			const currentSum = nums[i] + nums[left] + nums[right];

			if (currentSum === 0) {
				result.push([nums[i], nums[left], nums[right]]);

				// Skip duplicate values at both pointers.
				while (left < right && nums[left] === nums[left + 1]) {
					left++;
				}
				while (left < right && nums[right] === nums[right - 1]) {
					right--;
				}

				left++;
				right--;
			} else if (currentSum < 0) {
				// Need a larger sum, move left pointer right.
				left++;
			} else {
				// Need a smaller sum, move right pointer left.
				right--;
			}
		}
	}

	return result;
}

/*
Walkthrough Example

nums = [-1, 0, 1, 2, -1, -4]
After sorting: [-4, -1, -1, 0, 1, 2]

i = 0 (value = -4)
  left = 1, right = 5
  -4 + (-1) + 2 = -3 < 0 -> move left
  -4 + (-1) + 2 = -3 < 0 -> move left
  -4 + 0 + 2 = -2 < 0 -> move left
  -4 + 1 + 2 = -1 < 0 -> move left
  No triplet for i = 0

i = 1 (value = -1)
  left = 2, right = 5
  -1 + (-1) + 2 = 0 -> add [-1, -1, 2]
  move pointers inward
  left = 3, right = 4
  -1 + 0 + 1 = 0 -> add [-1, 0, 1]

i = 2 (value = -1)
  Duplicate fixed value of previous i, skip

Result: [[-1, -1, 2], [-1, 0, 1]]

Time Complexity:  O(n^2)
Space Complexity: O(1) extra space (excluding output)
*/

export { threeSum };
