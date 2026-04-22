# Maximum Distance Between a Pair of Values

**Platform:** LeetCode — [Problem 1855](https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/)  
**Difficulty:** Medium  
**Topic:** Arrays, Two Pointers

---

## Problem

Given two non-increasing integer arrays `nums1` and `nums2`, return the maximum distance `j - i` such that `i <= j` and `nums1[i] <= nums2[j]`. If no valid pair exists, return `0`.

**Example:**
Input:  nums1 = [55, 30, 5, 4, 2], nums2 = [100, 20, 10, 10, 5]
Output: 2

---

## Approach — Two Pointers

Since both arrays are non-increasing and `i` must be less than or equal to `j`, we can use two pointers starting at the beginning of each array. Keep advancing `j` as long as the pair is valid. When `nums1[i] > nums2[j]` is hit, advance `i` to find a smaller value that satisfies the constraint of nums1[i] <= nums2[j] again. Track the maximum `j - i` seen throughout.

### Pseudocode
function maxDistance(nums1, nums2):
i = 0, j = 0
max_dist = 0
while i< len(nums1) and j < len(nums2):
    if nums1[i] <= nums2[j]:
        max_dist = max(max_dist, j - i)
        j++
    else:
        i++

return max_dist

- **Time:** O(n + m)
- **Space:** O(1)

---

## Implementations

| Language | File |
|----------|------|
| Python | `python/max_distance.py` |
| Rust | `rust/src/main.rs` |
| TypeScript | `TS/maxDistance.ts` |

---

## Running Locally

**Python**
```bash
python3 max_distance.py
```

**Rust**
```bash
cargo run
```

**TypeScript**
```bash
tsx maxDistance.ts
```