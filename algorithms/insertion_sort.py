def insertion_sort(nums):

    # i is our postion tracker
    for i in range(len(nums)):
        # j comes back to teh current position after sorting below
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            # swap
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
    return nums


print(insertion_sort([4,3,2,1]))