use std::collections::HashMap;

// struct Solution {}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, i32> = HashMap::new();

        for (index, value) in nums.iter().enumerate() {
            let diff = &target - value;
            let i = map.get(&diff);
            if i != Option::None {
                let i = *(i.unwrap());
                let j = index as i32;
                return vec![i, j];
            }
            map.insert(*value, index as i32);
        }
        vec![]
    }
}

// In this problem, We are asked to find a two numbers in the given array [nums] that sums up to the given [target]

/*
Example:

Given the following:
nums = [2, 7, 11, 15]
target = 9

To find the two numbers that sum of to 9, we iterate over the array: nums

Algorithm for this specific example
Step 1:
    index = 0
    value = 2 (element at index 0 in the given array)
    diff = 9 - 2 = 7

    Since diff(difference) is 7, we check the [map] we are caching the values from the array in if it exists there
    We haven't inserted anything in the map, so not found

    We store (2: 0) into the map


Step 2:
    index = 1
    value = 7
    diff = 9 - 7 = 2

    Now, we check the [map] again for 2. Remember we stored 2 in previous step, so it must contain two

    Boom!, we've found a matching pair that sums up to the target. i.e, 7 = 2 = 9

    So index 0(value to the key 2 in the map) and index 1 in the current step for 7 are returned

    return [0, 1] or [1, 0]

*/
