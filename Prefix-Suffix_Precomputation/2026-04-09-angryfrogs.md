# Problem: Angry Frogs

## Link
https://leetcode.com/discuss/interview-question/4585427/Meta-or-OA-or-Angry-Frogs/

## Pattern
Prefix / Suffix Precomputation (under Arrays)

## Intuition
From any starting block, one frog jumps as far left as possible and the other
as far right as possible, but only onto blocks of equal or greater height.
Instead of simulating both frogs from every starting position (O(N²)), we
precompute the furthest reachable left and right index for every block in two
linear passes, then pick the starting block that maximises the spread.

## Approach (Step by Step)
1. Build `left[]` (left to right pass): for each index `i`, if the block to its
   left is >= `blocks[i]`, inherit `left[i-1]` (the frog can pass through);
   otherwise the frog is stuck, so `left[i] = i`.
2. Build `right[]` (right to left pass): if the block to
   the right is >= `blocks[i]`, inherit `right[i+1]`; otherwise `right[i] = i`.
3. For every index `i`, compute `distance = right[i] - left[i] + 1` (the question says the `distance` is computed  as K-J+1 where K is the rightmost index, i.e., `right[i]`, and J is the leftmost index, i.e., `left[i]`).
4. Return the maximum `distance` across all indices.

## Complexity
- Time: O(N) — two single passes over the array
- Space: O(N) — for the `left[]` and `right[]` arrays