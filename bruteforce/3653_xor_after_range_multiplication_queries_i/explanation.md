# LC 3653 - XOR After Range Multiplication Queries I

Here I attempt to explain my solution to LC problem #3653.

## Solution Details

- Problem: https://leetcode.com/problems/xor-after-range-multiplication-queries-i/
- Language: C++
- Difficulty: Medium
- Solved: Yes

## Understanding the Problem

There is no special trick (at least that I can see) in this problem, the steps are clearly laid out in the problem statement. So we do just that, follow the steps.

Note, since we're performing these large multiplications, we're bound to overflow the 32-bit integer. One quick fix is to multiply the result by a long datatype (1ll), thereby making the operation an integer modulo of a long (64-bits at least) datatype number.

## Bruteforce! (C++)

```cpp
// u/algo-xero
class Solution {
public:
    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        const int MOD = 1e9 + 7;
        for (auto const& q : queries) {
            int idx = q[0];
            while (idx <= q[1]) {
                nums[idx] = (1ll * nums[idx] * q[3]) % MOD;
                idx += q[2];
            }
        }
        int res = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            res ^= nums[i];
        }
        return res;
    }
};
```

## Conclusion

This is one of the easier mediums on Leetcode, there's probably an optimization trick somewhere, or perhaps this is solvable with segment trees? At any rate, once you nail the bruteforce, further optimization is usually a fun challenge.

Time complexity: O(Q * N), in the absolute worst case we run each query for each number.

Space complexity: O(1)

Solution by [u/algo-xero](https://leetcode.com/u/algo-xero)
