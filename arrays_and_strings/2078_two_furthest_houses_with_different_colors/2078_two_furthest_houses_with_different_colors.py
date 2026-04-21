"""2078. Two Furthest Houses With Different Colors

There are n houses in a row, each painted with a color represented by colors[i].
Return the maximum distance between two houses with different colors.

Example: colors = [1,1,1,6,1,1,1] -> 3
         (house 0, color 1) and (house 3, color 6): distance = 3

Strategy: greedy from both ends
The furthest pair must involve either the first or last house.
Two scans suffice:
  1. Fix the last house, scan from the left for the first different color.
  2. Fix the first house, scan from the right for the first different color.
"""


def maxDistance(colors: list[int]) -> int:
    n = len(colors)

    # Scan from left: furthest house from the right end with a different color.
    i = 0
    while colors[i] == colors[n - 1]:
        i += 1
    dist1 = (n - 1) - i

    # Scan from right: furthest house from the left end with a different color.
    j = n - 1
    while colors[j] == colors[0]:
        j -= 1
    dist2 = j  # j - 0

    return max(dist1, dist2)


"""
Walkthrough — colors = [1,1,1,6,1,1,1]  (n = 7)

Scan from left (last house color = 1):
  i advances past indices 0,1,2 (all color 1), stops at i=3 (color 6)
  dist1 = 6 - 3 = 3

Scan from right (first house color = 1):
  j retreats past indices 6,5,4 (all color 1), stops at j=3 (color 6)
  dist2 = 3

Result: max(3, 3) = 3

---

colors = [0,8,8,8,0,0,0,8,8]  (n = 9)

Scan from left (last house color = 8):
  i=0: colors[0]=0 != 8 -> stop immediately
  dist1 = 8 - 0 = 8

Scan from right (first house color = 0):
  j=8: colors[8]=8 != 0 -> stop immediately
  dist2 = 8

Result: max(8, 8) = 8

Time Complexity:  O(n) — two linear scans, each at most n steps
Space Complexity: O(1)
"""
