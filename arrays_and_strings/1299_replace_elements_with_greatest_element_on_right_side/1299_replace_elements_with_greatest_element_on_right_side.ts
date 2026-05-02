// 1299. Replace Elements with Greatest Element on Right Side
//
// Given an array arr, replace every element with the greatest element
// among all elements to its right. Replace the last element with -1.
// Return the modified array.
//
// Example: [17,18,5,4,6,1] -> [18,6,6,6,1,-1]

// Strategy: reverse traversal with a running max
// Scanning left-to-right would require looking ahead for the max each time: O(n^2).
// Scanning right-to-left lets us maintain a running max of everything seen so far,
// so each position can be filled in O(1).
//
// At each step:
//   1. Save the current value (we're about to overwrite it).
//   2. Write the running max into arr[i].
//   3. Update the running max if the saved value was larger.
// The last element is handled automatically: max starts at -1, so arr[n-1] = -1.

function replaceElements(arr: number[]): number[] {
    let max = -1; // rightmost sentinel required by the problem

    for (let i = arr.length - 1; i >= 0; i--) {
        const curr = arr[i];  // save before overwriting
        arr[i] = max;
        if (curr > max) max = curr;
    }

    return arr;
}

/*
Walkthrough — arr = [17, 18, 5, 4, 6, 1]

i=5: curr=1,  arr[5]=-1, max=max(-1,1)=1    -> [17,18,5,4,6,-1]
i=4: curr=6,  arr[4]=1,  max=max(1,6)=6     -> [17,18,5,4,1,-1]
i=3: curr=4,  arr[3]=6,  max=max(6,4)=6     -> [17,18,5,6,1,-1]
i=2: curr=5,  arr[2]=6,  max=max(6,5)=6     -> [17,18,6,6,1,-1]
i=1: curr=18, arr[1]=6,  max=max(6,18)=18   -> [17,6,6,6,1,-1]
i=0: curr=17, arr[0]=18, max=max(18,17)=18  -> [18,6,6,6,1,-1]

Result: [18,6,6,6,1,-1]

Time Complexity:  O(n) — single right-to-left pass
Space Complexity: O(1) — modified in place, only one extra variable
*/

export { replaceElements };
