export {}

function minMirrorPairDistance(nums: number[]): number {
    let numsMap: Map<number, number> = new Map();
    let min_dist: number = Infinity;

    for(let i = 0; i < nums.length; i++){
        const reverseNumber = Number(String(nums[i]).split("").reverse().join(""));
        if (numsMap.has(nums[i])){
            min_dist = Math.min(min_dist, i - numsMap.get(nums[i])!)
        };

        numsMap.set(reverseNumber, i)
    };

    return min_dist < Infinity ? min_dist : -1

};

const testCases: number[][] = [
    [12, 21, 11],
    [1, 3, 2, 1],
    [1, 2, 3],
    [13, 31, 31],
    [12, 21, 21],
    [120, 21, 45],
];

for (const nums of testCases) {
    console.log(`Input:       ${JSON.stringify(nums)}`);
    console.log(`Output:      ${minMirrorPairDistance(nums)}`);
    console.log("-".repeat(35));
}