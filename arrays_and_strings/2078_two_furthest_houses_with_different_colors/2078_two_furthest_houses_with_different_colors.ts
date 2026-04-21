// 2078. Two Furthest Houses With Different Colors
//
// There are n houses in a row, each painted with a color represented by colors[i].
// Return the maximum distance between two houses with different colors.
//
// Example: colors = [1,1,1,6,1,1,1] -> 3
//          (house 0, color 1) and (house 3, color 6): distance = 3

// Strategy: greedy from both ends
// The furthest pair must involve either the first or last house.
// Proof by contradiction: if the optimal pair is (i, j) with i > 0 and j < n-1,
// then since colors[i] != colors[j], at least one of (0, j) or (i, n-1) gives
// an equal or greater distance — so we never need to consider interior pairs only.
//
// This reduces the problem to two linear scans:
//   1. Fix the last house (index n-1), scan from the left to find the first
//      house with a different color — that maximises distance from the right end.
//   2. Fix the first house (index 0), scan from the right to find the first
//      house with a different color — that maximises distance from the left end.

function maxDistance(colors: number[]): number {
    const n = colors.length;

    // Scan from left: find furthest house from the right end with a different color.
    let i = 0;
    while (colors[i] === colors[n - 1]) {
        i++;
    }
    const dist1 = (n - 1) - i;

    // Scan from right: find furthest house from the left end with a different color.
    let j = n - 1;
    while (colors[j] === colors[0]) {
        j--;
    }
    const dist2 = j; // j - 0

    return Math.max(dist1, dist2);
}

/*
Walkthrough — colors = [1,1,1,6,1,1,1]  (n = 7)

Scan from left (fixing last house, color 1):
  i=0: colors[0]=1 == colors[6]=1 -> i++
  i=1: colors[1]=1 == colors[6]=1 -> i++
  i=2: colors[2]=1 == colors[6]=1 -> i++
  i=3: colors[3]=6 != colors[6]=1 -> stop
  dist1 = (7-1) - 3 = 3

Scan from right (fixing first house, color 1):
  j=6: colors[6]=1 == colors[0]=1 -> j--
  j=5: colors[5]=1 == colors[0]=1 -> j--
  j=4: colors[4]=1 == colors[0]=1 -> j--
  j=3: colors[3]=6 != colors[0]=1 -> stop
  dist2 = 3 - 0 = 3

Result: max(3, 3) = 3

---

colors = [0,8,8,8,0,0,0,8,8]  (n = 9)

Scan from left (fixing last house, color 8):
  i=0: colors[0]=0 != colors[8]=8 -> stop immediately
  dist1 = (9-1) - 0 = 8

Scan from right (fixing first house, color 0):
  j=8: colors[8]=8 != colors[0]=0 -> stop immediately
  dist2 = 8 - 0 = 8

Result: max(8, 8) = 8

Time Complexity:  O(n) — two linear scans, each at most n steps
Space Complexity: O(1)
*/

export { maxDistance };
