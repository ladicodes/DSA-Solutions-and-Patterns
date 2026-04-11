from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Step 1: convert to a list of the integer values in base-10
        val_list = [(digits[i]*(10**(len(digits)-i-1))) for i in range(len(digits))]

        # Step 2: sum all values
        sum_dig = sum(val_list)

        # Step 3: add 1, convert to string (to allow easy iteration), then convert to list using list comprehension
        return [int(dig) for dig in str(sum_dig+1)]
