// 3225. Maximum Score From Grid Operations
//
// Given an n×n grid, you may paint any column j black from row 0 down to row i
// (one operation covers a prefix of the column). A white cell scores grid[i][j]
// if it has at least one horizontally adjacent black cell. Return the max score.

// Strategy: column-by-column DP
//
// Key observation: the score from adjacent columns depends only on the "height"
// (number of blacked-out rows) of two neighbouring columns, not on every column
// independently. So we sweep left to right and track heights.
//
// State:  dp[i][j][t]
//   i = height of column j (rows 0..i-1 are black)
//   j = column index
//   t = 0: score up to col j, NOT yet counting white cells in col j-1
//           that are adjacent to col j's black part (right-side adjacency
//           for col j-1 — unknown until we know height of col j)
//   t = 1: score up to col j, INCLUDING white cells in col j that are
//           adjacent to col j-1's black part (left-side adjacency for col j)
//
// Transition (col j-1 has height i, col j has height l):
//   curr = Σ grid[k][j]  for k in [l, i-1]   (white in col j, left-adjacent to col j-1)
//   prev = Σ grid[k][j-1] for k in [i, l-1]  (white in col j-1, right-adjacent to col j)
//
//   maxPrev = max(dp[i][j-1][1],          // left-adj of col j-1 already counted
//                 dp[i][j-1][0] + prev)   // add right-adj of col j-1 now
//
//   dp[l][j][0] = max(dp[l][j][0], maxPrev)         // don't count col j's right-adj yet
//   dp[l][j][1] = max(dp[l][j][1], maxPrev + curr)  // count col j's left-adj now

function maximumScore(grid: number[][]): number {
    const n = grid.length;
    if (n === 1) return 0;

    // dp[i][j] = [score without right-adj, score with left-adj]
    const dp: [number, number][][] = Array.from({ length: n + 1 }, () =>
        Array.from({ length: n }, () => [0, 0])
    );

    for (let j = 1; j < n; j++) {
        for (let i = 0; i <= n; i++) {
            const dp0 = dp[i][j - 1][0];
            const dp1 = dp[i][j - 1][1];

            let prev = 0;

            // Sum of grid[k][j] for k = 0..i-1 (will be trimmed as l grows).
            let curr = 0;
            for (let k = 0; k < i; k++) curr += grid[k][j];

            for (let l = 0; l <= n; l++) {
                // As l increases into the black zone of col j-1 (l <= i),
                // row l-1 of col j becomes black — subtract it from curr.
                if (l > 0 && l <= i) curr -= grid[l - 1][j];

                // As l grows past i, rows i..l-1 of col j-1 become right-adjacent
                // to col j's black part — accumulate them into prev.
                if (l > i) prev += grid[l - 1][j - 1];

                const maxPrev = Math.max(dp1, dp0 + prev);
                dp[l][j] = [
                    Math.max(dp[l][j][0], maxPrev),
                    Math.max(dp[l][j][1], maxPrev + curr),
                ];
            }
        }
    }

    // Answer is the best score at the last column with left-adjacency counted.
    let maxVal = -Infinity;
    for (let i = 0; i <= n; i++) {
        maxVal = Math.max(maxVal, dp[i][n - 1][1]);
    }
    return maxVal;
}

/*
Walkthrough — grid = [[0,0,0],[0,1,0],[0,0,1]]  (n = 3)

Heights range 0..3. The DP fills dp[height][col][0/1] column by column.
At col 2 the best configuration is found by checking all heights i (col 1)
paired with all heights l (col 2) and picking the maximal [1] value.

Time Complexity:  O(n^3)
  — outer loops: n columns × (n+1) previous heights = O(n^2)
  — inner l-loop: O(n), sum computation: O(n) amortised across i
Space Complexity: O(n^2) — dp table is (n+1) × n × 2
*/

export { maximumScore };
