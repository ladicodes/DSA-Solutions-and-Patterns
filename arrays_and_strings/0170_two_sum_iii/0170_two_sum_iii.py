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