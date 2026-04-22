export {}

function maxDistance(nums1: number[], nums2: number[]): number {
    let [n, m] = [nums1.length, nums2.length];
    let [i, j] = [0,0]
    let maxDist = 0;
    while(i < n && j < m){
        if(nums1[i] <= nums2[j]){
            maxDist = Math.max(maxDist, j - i)
            j++
        } else if(nums1[i] > nums2[j]){
            i++
        };
    };

    return maxDist
}

const testCases: [number[], number[]][] = [
    [[55, 30, 5, 4, 2], [100, 20, 10, 10, 5]],
    [[2, 2, 2], [10, 10, 1]],
    [[30, 29, 19, 5], [25, 25, 25, 25, 25]],
    [[5, 4, 3, 2, 1], [5, 4, 3, 2, 1]],
    [[1], [1]],
];

for (const [nums1, nums2] of testCases) {
    console.log(`Input:       nums1=${JSON.stringify(nums1)}, nums2=${JSON.stringify(nums2)}`);
    console.log(`Output:      ${maxDistance(nums1, nums2)}`);
    console.log("-".repeat(35));
}