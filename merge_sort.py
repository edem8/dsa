def merge_sort(nums):
    # if len 1 then theres no need to sort it
    if len(nums) < 2:
        return nums

    # find the middle
    mid = len(nums) // 2

    # split the array into left and right half and perform merge_sort
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    # merge the to halves when they cant be split
    return merge(left, right)


def merge(left, right):

    i = j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result





print(merge_sort([4,2,6,9,10,3,6,8]))