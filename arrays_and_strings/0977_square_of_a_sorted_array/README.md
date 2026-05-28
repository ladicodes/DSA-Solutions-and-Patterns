

#  Squares of a Sorted Array

[Question](https://leetcode.com/problems/-squares-of-a-sorted-array/)

## Approach

On seeing the question , i quickly tought of transversing through the `nums` array once, squaring each element in the array.
then use the inbuilt sort method in both `rust` and `python` to sort the values in place and return the result.

But doing this would leave us with a Time complexity of $$O(NLogN)$$,which wouldn't be ideal given the question.

So i decided to use two pointers from both ends, and to transverse the `nums` array from the end , check which of the squared values is greater and set it to the current position in the `result` array.Then we adjust the pointers based on the element used and the process repeats until completed . 

Why this? approach .

We are given a non decreasing array that could have negative integers, for example [-4,-3,0,1,3,3], the squared value ofthe elements increase as the elements becomed larger positively and also as it becomes larger negatively.

So the largest squared element of the result must either be the first or the last element of `nums` .Hence we need to compare the those values and keep shifting according to the used element. 

The key idea is to Utilize two pointers from both ends to fill the result array backwards based on squared values.


## Complexity Analysis

* **Time Complexity: $$O(N)$$** Since we only transverese through the array once
* **Space Complexity: $$O(N)$$** Since we only make use of an array of size `N`

## Implementation

```python
# python solution
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i,j = 0,n-1       # initialized pointers 
        result = [0]*n    # initialized result arrays for easy indexing  

        for k in range(n-1,-1,-1):  #k starts at n-1 decreasing till 0
            
            if nums[i]**2 > nums[j]**2:
                result[k] = nums[i]**2
                i += 1
            else:
                result[k] = nums[j]**2
                j -= 1
        return result     
        

```

I also decided to try write it in rust sice i started learning rust
### My first rust solution
```rust
impl Solution {
    pub fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {
        let n:usize = nums.len();
        // initializing pointers 
        let mut i:usize = 0;
        let mut j:usize = n-1;

        // initializing result array
        let mut result:Vec<i32> = vec![0;n];
        
        // k starts at n-1 decreasing till 0
        for k in (0..n).rev(){
            if nums[i].pow(2) > nums[j].pow(2){
                result[k] = nums[i].pow(2);
                i += 1;
            }
            else{
                result[k] = nums[j].pow(2);
                j -= 1;
            }

        }
        return result 
    }
}
```

