"""3225. Maximum Score From Grid Operations

Given an n×n grid, you may paint any column j black from row 0 down to row i.
A white cell scores grid[i][j] if it has at least one horizontally adjacent
black cell. Return the max score.

Strategy: column-by-column DP
dp[i][j][0] = max score up to col j with col j at height i,
              NOT yet counting right-adjacency of col j-1 towards col j.
dp[i][j][1] = same, but INCLUDING left-adjacency of col j towards col j-1.

Transition: for prev height i (col j-1) and curr height l (col j):
  curr = white cells in col j left-adjacent to black col j-1  (rows [l, i-1])
  prev = white cells in col j-1 right-adjacent to black col j (rows [i, l-1])
"""


def maximumScore(grid: list[list[int]]) -> int:
    n = len(grid)
    if n == 1:
        return 0

    # dp[i][j] = [score_no_right_adj, score_with_left_adj]
    dp = [[[0, 0] for _ in range(n)] for _ in range(n + 1)]

    for j in range(1, n):
        for i in range(n + 1):
            dp0 = dp[i][j - 1][0]
            dp1 = dp[i][j - 1][1]

            prev = 0
            curr = sum(grid[k][j] for k in range(i))

            for l in range(n + 1):
                # Row l-1 of col j turns black — remove it from left-adj sum.
                if 0 < l <= i:
                    curr -= grid[l - 1][j]
                # Row l-1 of col j-1 becomes right-adjacent to col j.
                if l > i:
                    prev += grid[l - 1][j - 1]

                max_prev = max(dp1, dp0 + prev)
                dp[l][j][0] = max(dp[l][j][0], max_prev)
                dp[l][j][1] = max(dp[l][j][1], max_prev + curr)

    return max(dp[i][n - 1][1] for i in range(n + 1))


"""
Time Complexity:  O(n^3) — n columns × (n+1) heights × O(n) inner loop
Space Complexity: O(n^2) — dp table is (n+1) × n × 2
"""
