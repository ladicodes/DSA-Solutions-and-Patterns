## How it works given the nums = [2, 7, 11, 15] and target = 9:

1. At first, the "num_dict" is empty
2. The enumerate function turns nums to pairs of index and value, so the first pair is (1, 2) where 1 is the index and 2 is the value
3. the first loop will have idx=1 and val is 2, after deducting val from target which is 9 we get 7
4. the condition checks if 7 is in num_dict, which is false because num_dict is empty at first iteration
5. It then adds the current val in the iteration and it idx as key and value pairs respectively to num_dict, so num_dict becomes {2: 1}
6. the second loop will have idx=2 and val=7, after deducting val from target which is 9 we get 2
7. the condition checks if 2 is in num_dict, which is true because num_dict has {2: 1}
8. it then returns the value of 2 in num_dict which is 1 and the current idx which is 2, so the output is [1, 2]
9. but if any 2 values in the list can't make up the target, we get an empty list []
