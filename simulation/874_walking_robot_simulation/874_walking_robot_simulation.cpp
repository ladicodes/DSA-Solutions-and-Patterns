// u/algo-xero
using p_set = set<pair<int, int>>;

class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        p_set obs;
        for (auto const& ob : obstacles)
            obs.insert({ob[0], ob[1]});

        int x = 0, y = 0, dir = 0, res = 0;

        for (auto const& cmd : commands) {
            if (cmd == -1) {
                dir = (((dir + 1) % 4) + 4) % 4; 
            }
            else if (cmd == -2) {
                dir = (((dir - 1) % 4) + 4) % 4; 
            }
            else {
                int units = cmd;
                // there should be a more efficient way of doing this, 
                // however, i'm very lazy.
                while (units--) {
                    int nx = x, ny = y;
                    if (dir == 0) ny++;
                    else if (dir == 1) nx++;
                    else if (dir == 2) ny--;
                    else nx--;
                    if (obs.contains({nx, ny})) break;
                    x = nx, y = ny;
                    y = ny;
                }
                res = max(res, x*x + y*y);
            }
        }

        return res; 
    }
};
