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
