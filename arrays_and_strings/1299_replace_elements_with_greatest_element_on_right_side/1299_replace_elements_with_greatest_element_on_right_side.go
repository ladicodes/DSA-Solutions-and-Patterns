// 1299. Replace Elements with Greatest Element on Right Side
//
// Given an array arr, replace every element with the greatest element
// among all elements to its right. Replace the last element with -1.
// Return the modified array.
//
// Example: [17,18,5,4,6,1] -> [18,6,6,6,1,-1]

// Strategy: reverse traversal with a running max
// Scanning right-to-left lets us maintain a running max in O(1) per element
// instead of looking ahead on every step (which would be O(n^2)).

package arrays

func replaceElements(arr []int) []int {
	maxVal := -1 // rightmost sentinel required by the problem

	for i := len(arr) - 1; i >= 0; i-- {
		curr := arr[i] // save before overwriting
		arr[i] = maxVal
		if curr > maxVal {
			maxVal = curr
		}
	}

	return arr
}

/*
Walkthrough — arr = [17, 18, 5, 4, 6, 1]

i=5: curr=1,  arr[5]=-1, max=1   -> [17,18,5,4,6,-1]
i=4: curr=6,  arr[4]=1,  max=6   -> [17,18,5,4,1,-1]
i=3: curr=4,  arr[3]=6,  max=6   -> [17,18,5,6,1,-1]
i=2: curr=5,  arr[2]=6,  max=6   -> [17,18,6,6,1,-1]
i=1: curr=18, arr[1]=6,  max=18  -> [17,6,6,6,1,-1]
i=0: curr=17, arr[0]=18, max=18  -> [18,6,6,6,1,-1]

Result: [18,6,6,6,1,-1]

Time Complexity:  O(n) — single right-to-left pass
Space Complexity: O(1) — modified in place, only one extra variable
*/
