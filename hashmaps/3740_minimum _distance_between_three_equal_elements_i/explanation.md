# LC 3740 Minimum Distance Between Three Equal Elements I

Here I attempt to explain my solution to LC problem #3740.

## Solution Details

- Language: C++
- Difficulty: Easy
- Solved: Yes

## Understanding the Problem

This problem requests that we find the minimum 'distance' between any triplet of the same number in the given array.

The 'distance' here is given by the formula:

```
D = abs(nums[i] - nums[j]) + abs(nums[j] - nums[k]) + abs(nums[k] - nums[i])
```

Where nums[i] = nums[j] = nums[k] and i != j != k.

Okay, cool. One way to solve this would be to bruteforce, slap on three nested for loops and you're done. Certainly the constraints should allow this (N <= 100), but we're smart; we want something a little bit better than the naive cubic time solution.

So, sacrificing a little memory instead, we can reduce the TC by an some order of magnitudes lower to linear time by using a hashmap. 

Our plan would be to 'collect' the indices of each unique number in the array, then 'scan' through to compute the smallest 'distance' so far. Now, it's worth mentioning that arrays with size N < 3 are automatically disqualified, since no unique index triplets can exist here, saving some compute.

## Solution (C++)

```cpp
// u/algo-xero
using umap = unordered_map<int, vector<int>>;

class Solution {
public:
    int minimumDistance(vector<int>& nums) {
        if (nums.size() < 3) {
            return -1;
        }
        int n = nums.size();
        umap indices;
        for (int i = 0; i < n; ++i) {
            indices[nums[i]].push_back(i);
        }
        int dist = INT_MAX;
        for (const auto &[_, v] : indices) {
            for (int i = 0; i + 2 < v.size(); ++i) {
                dist = min(dist, 
                    abs(v[i] - v[i+1]) + 
                    abs(v[i+1] - v[i+2]) + 
                    abs(v[i+2] - v[i])
                );
            }
        }
        return (dist == INT_MAX) ? -1 : dist;
    }
};
```

## Conclusion

This is a rather simple problem. The first instinct is to enumerate all possible combinations of triplets, an approach that'd yield you no better than a time complexity in the order of O(N^3).

However, you should try to resist that temptation and look for better methods, like we saw here dropping two layers down to O(N). 

Time Complexity: O(N). Technically, the inner nested loop runs at most L-2 times, where L is the number of elements in the vector for that key. It's effectively the sum of (L-2) across all K keys which is:

$$
\sum_{i=1}^{n}(L -2) = \sum_{i=1}^{k}L - \sum_{i=1}^{k}2\ 
$$

Which equates to:

$$
\sum_{i=1}^{k}L - 2K
$$

But since this will always be less than N, it's safe to say total TC is O(N).

Space Complexity: O(N), from the hashmap.

Solution by [u/algo-xero](https://leetcode.com/u/algo-xero)
