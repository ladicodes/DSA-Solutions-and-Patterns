## 15. 3Sum

### Pattern
- Sorting + Two Pointers

### Intuition
After sorting the array, we can fix one value and then find two other values using a left and right pointer. Because the array is sorted:
- moving `left` right increases the sum,
- moving `right` left decreases the sum.

This allows us to find valid triplets in linear time for each fixed index.

### Approach (Step by Step)
1. Sort the input array.
2. Loop through each index `i` from `0` to `n - 3` as the fixed number.
3. Skip duplicate fixed values (`nums[i] == nums[i - 1]`) to avoid duplicate triplets.
4. Set `left = i + 1` and `right = n - 1`.
5. While `left < right`:
   - Compute `sum = nums[i] + nums[left] + nums[right]`.
   - If `sum == 0`, record the triplet and skip duplicates for both `left` and `right`.
   - If `sum < 0`, move `left` right.
   - If `sum > 0`, move `right` left.
6. Return all collected triplets.

### Example
Input:
- `nums = [-1, 0, 1, 2, -1, -4]`

Sorted:
- `[-4, -1, -1, 0, 1, 2]`

Output:
- `[[-1, -1, 2], [-1, 0, 1]]`

### Complexity
- Time: `O(n^2)`
  - Sorting is `O(n log n)`, two-pointer scans dominate at `O(n^2)`.
- Space: `O(1)` extra (excluding output storage).

### Why duplicates are avoided
- Skip duplicate `i` values before running two pointers.
- After finding a valid triplet, move both pointers past equal adjacent values.

This guarantees each unique triplet appears exactly once.
