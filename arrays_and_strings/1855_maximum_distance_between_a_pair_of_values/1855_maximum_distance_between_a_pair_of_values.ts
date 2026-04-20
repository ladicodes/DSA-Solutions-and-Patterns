// 1855. Maximum Distance Between a Pair of Values
//
// Given two non-increasing integer arrays nums1 and nums2, return the maximum
// value of j - i such that i <= j and nums1[i] <= nums2[j].
//
// Example: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5] -> 2
//          (i=2, j=4: nums1[2]=5 <= nums2[4]=5, distance = 4-2 = 2)

// Strategy: greedy two pointers
// For each i we want j pushed as far right as possible while nums1[i] <= nums2[j].
// Key insight: j never needs to reset between iterations of i.
// As i increases, nums1[i] gets smaller (non-increasing), so the furthest valid j
// can only stay the same or move further right — never backward.
// This gives us a single left-to-right pass over both arrays.

function maxDistance(nums1: number[], nums2: number[]): number {
    let maxDist = 0;
    let j = 0;

    for (let i = 0; i < nums1.length; i++) {
        // Extend j as far right as the condition holds for this i.
        while (j < nums2.length && nums1[i] <= nums2[j]) {
            j++;
        }
        // j is now one past the last valid index, so the furthest valid j was j-1.
        // Also enforce i <= j (i.e. j > i means j-1 >= i).
        if (j > i) {
            maxDist = Math.max(maxDist, (j - 1) - i);
        }
    }

    return maxDist;
}

/*
Walkthrough — nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]

i=0, nums1[0]=55:
  j=0: nums2[0]=100 >= 55 -> j++
  j=1: nums2[1]=20  <  55 -> stop
  j=1 > i=0: maxDist = max(0, (1-1)-0) = 0

i=1, nums1[1]=30:
  j=1: nums2[1]=20 < 30 -> stop immediately (j doesn't reset, still 1)
  j=1 == i=1: skip (no valid j >= i)

i=2, nums1[2]=5:
  j=1: nums2[1]=20 >= 5 -> j++
  j=2: nums2[2]=10 >= 5 -> j++
  j=3: nums2[3]=10 >= 5 -> j++
  j=4: nums2[4]=5  >= 5 -> j++
  j=5: out of bounds -> stop
  j=5 > i=2: maxDist = max(0, (5-1)-2) = 2

i=3, nums1[3]=4:
  j=5: out of bounds -> while skipped
  j=5 > i=3: maxDist = max(2, (5-1)-3) = max(2, 1) = 2

i=4, nums1[4]=2:
  j=5: out of bounds -> while skipped
  j=5 > i=4: maxDist = max(2, (5-1)-4) = max(2, 0) = 2

Result: 2

Why j never resets:
  nums1 is non-increasing, so nums1[i+1] <= nums1[i].
  If nums1[i] <= nums2[j], then nums1[i+1] <= nums2[j] too.
  The valid range for j cannot shrink as i grows, so the previous j
  is always a safe (and optimal) starting point for the next iteration.

Time Complexity:  O(n + m) — i and j each traverse their array at most once
Space Complexity: O(1)
*/

export { maxDistance };
