
#I think I have an idea from what I saw in Xero's solution to a similar problem.
#I'll first build a dictionary of each value and it's reverse. I'll just need to 
#  then look for when a value
def reverse(num: int) -> int:
    st = str(num)
    reverse_st = st[::-1]
    return int(reverse_st)
    

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        # nums_map: dict[int, list[int]] = {}
        valid_idxs: list[tuple] = []
        for i, num in enumerate(nums):
            rev = reverse(num)
            for j in range(len(nums)):
                if j == i:
                    continue
                elif rev == nums[j] and i < j:
                    valid_idxs.append((i, j))
        if not valid_idxs:
            return -1
        min_d = map(lambda x: abs(x[0] -x[1] ), valid_idxs)
        return min(min_d)

                    
                
                
                
            
        
        

if __name__ == "__main__":
    test_cases = [
        [12, 21, 11],              # → 1, pair (0,1): reverse(12)=21
        [1, 3, 2, 1],              # → 3, pair (0,3): reverse(1)=1
        [1, 2, 3],                 # → -1, no mirror pairs
        [13, 31, 31],              # → 1, duplicate targets, closest wins
        [12, 21, 21],              # → 1, reverse(12)=21 appears twice
        [120, 21, 45],             # → 1, reverse(120)=21, leading zero omitted
    ]

    for nums in test_cases:
        print(f"Input:       {nums}")
        print(f"Output:      {Solution().minMirrorPairDistance(nums)}")
        print("-" * 35)