'''

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
 
'''
class Solution(object):
    def candy(self, ratings):
        # number of children
        n = len(ratings)
        # start by giving each child 1 candy (minimum requirement)
        candies = [1] * n

        # left to right pass: ensure right child gets more if rating increases
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1  # give one more than left neighbor

        # right to left pass: ensure left child gets more if its rating is higher
        # use max to preserve any larger value already assigned from the left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # total candies needed is the sum of the assigned candies
        return sum(candies)

# Walkthrough Example:
# ratings = [1,0,2]
# Start candies = [1,1,1]
# Left->Right: index2 (2>0) -> candies = [1,1,2]
# Right->Left: index0 (1>0) -> candies = [2,1,2]
# Sum = 5

# Time Complexity: O(n) — two linear passes over the ratings.
# Space Complexity: O(n) — extra array `candies` of size n.