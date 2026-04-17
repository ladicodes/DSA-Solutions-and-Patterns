from typing import List

def reverse(num: int) -> int:
    st = str(num)
    reverse_st = st[::-1]
    return int(reverse_st)
    
#Loop through and immediately check a hasmap for valid reverses; update the map as
#you loop
#map is lazy so it wasn't running when it was unused
class Solution_before:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        nums_map = {}
        min_d_array: list[int] = []
        for idx, num in enumerate(nums):
            rev = reverse(num)
            if num in nums_map:
                idxs = nums_map.get(num)
                # print("before map: ", idxs)
                # print("currend idx:", idx)
                # idxs = map(lambda x: idx - x, idxs)
                # idxs = [idx - x for x in idxs]
                d = idx - idxs
                # print("after map: ", idxs)
                min_d_array.append(d)
            nums_map[rev] = idx
        else:
            min_d = -1 if not min_d_array else min(min_d_array)
            return min_d
        
class Solution_final:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        nums_map = {}
        min_dist = float('inf')
        for idx, num in enumerate(nums):
            rev = reverse(num)
            if num in nums_map:
                idxs = nums_map.get(num)
                dist = idx - idxs
                min_dist = min(min_dist, dist)
            nums_map[rev] = idx
        return min_dist if min_dist != float('inf') else -1
        

                    
                
                
                
            
        
        

if __name__ == "__main__":
    test_cases = [
        [12, 21, 11],              # → 1, pair (0,1): reverse(12)=21
        [1, 3, 2, 1],              # → 3, pair (0,3): reverse(1)=1
        [1, 2, 3],                 # → -1, no mirror pairs
        [13, 31, 31],              # → 1, duplicate targets, closest wins
        [12, 21, 21],              # → 1, reverse(12)=21 appears twice
        [120, 21, 45],             # → 1, reverse(120)=21, leading zero omitted
        [7,21,39,37,47,72,12,74], # -> 3
    ]

    for nums in test_cases:
        print(f"Input:       {nums}")
        print(f"Output:      {Solution_final().minMirrorPairDistance(nums)}")
        print("-" * 35)
    # n = 6
    # print(f"Input:       {test_cases[n]}")
    # print(f"Output:      {Solution().minMirrorPairDistance(test_cases[n])}")
    # print("-" * 35)