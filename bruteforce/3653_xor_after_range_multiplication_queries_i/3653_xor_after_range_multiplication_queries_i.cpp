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
