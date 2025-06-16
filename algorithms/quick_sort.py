def quick_sort(nums):
    # Base case: return list  if only one item or less
    if len(nums) <= 1:
        return nums
    

    # select a pivot : last value recommended
    pivot = nums[-1]

    # partition the list into left and right list
    left = [x for x in nums[:-1]  if x < pivot]
    right = [x for x in nums[:-1] if x >= pivot]


    # return a recursive sort of left and right items with pivot in the middle
    return quick_sort(left) + [pivot] + quick_sort(right) 





print(quick_sort([4,6,2,7,12,8,3,8]))