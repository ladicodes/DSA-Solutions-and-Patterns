// My first rust solution

#[derive(Debug)]
struct Solution;

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

fn main() {
    //  Define sample input vector
    let nums = vec![-4, -1, 0, 3, 10];
    
    // Call the function
    let output = Solution::sorted_squares(nums);
    
    // Print the result using debug formatting 
    println!("Sorted Squares: {output:?}");
}