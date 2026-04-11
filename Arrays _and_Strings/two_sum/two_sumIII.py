""""
There are many approaches to the twosum problem.
This is the approach using enumerate to create a dictionary for the list
""""

def two_sum(nums: [int], target: int):
    # Instantiating an empty dictionary store
    num_dict = {}

    #Using the enumerate function and looping through each values of the list
    for idx, val in enumerate(nums, start=1):

        # Getting the remainder by subtracting each looped val from target
        remainder = target - val

        if remainder in num_dict.keys():
            return [num_dict[remainder], idx]

        # Add the val and ind as key and value respectively to the num_dict
        num_dict[val] = idx

    return []

#### How it works given the nums = [2, 7, 11, 15] and target = 9:
# At first, the "num_dict" is empty
# The enumerate function turns nums to pairs of index and value, so the first pair is (1, 2) where 1 is the index and 2 is the value
# the first loop will have idx=1 and val is 2, after deducting val from target which is 9 we get 7
# the condition checks if 7 is in num_dict, which is false because num_dict is empty at first iteration
# It then adds the current val in the iteration and it idx as key and value pairs respectively to num_dict, so num_dict becomes {2: 1}
# the second loop will have idx=2 and val=7, after deducting val from target which is 9 we get 2
# the condition checks if 2 is in num_dict, which is true because num_dict has {2: 1}
# it then returns the value of 2 in num_dict which is 1 and the current idx which is 2, so the output is [1, 2]
# but if any 2 values in the list can't make up the target, we get an empty list []
