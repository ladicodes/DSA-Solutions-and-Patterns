use std::{cmp::min, collections::HashMap};

struct Solution();
fn main() {
    let test_cases = vec![
        vec![12, 21, 11],
        vec![1, 3, 2, 1],
        vec![1, 2, 3],
        vec![13, 31, 31],
        vec![12, 21, 21],
        vec![120, 21, 45],
    ];

    for nums in test_cases {
        println!("Input:       {:?}", nums);
        println!("Output:      {}", Solution::min_mirror_pair_distance(nums));
        println!("{}", "-".repeat(35));
    }
}

impl Solution {
    fn min_mirror_pair_distance(nums: Vec<i32>) -> i32 {
        let mut nums_map: HashMap<i32, i32> = HashMap::new();
        let mut min_distance: i32 = i32::MAX;

        //iterators in Rust are also lazy like in python
        for (idx, &num) in nums.iter().enumerate() {
            let reverse_number = &num
                .to_string()
                .chars()
                .rev()
                .collect::<String>()
                .parse::<i32>()
                .unwrap();
            if nums_map.contains_key(&num) {
                min_distance = min(min_distance, idx as i32 - nums_map.get(&num).unwrap());
            };

            nums_map.insert(*reverse_number, idx as i32);
        }

        if min_distance < i32::MAX {
            min_distance
        } else {
            -1
        }
    }
}
