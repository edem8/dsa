def binary_search(nums, target):

    # Define a start and end point
    start = 0
    end = len(nums) - 1

    
    while start <= end:
        # find the mid of the array based of what start, end are.
        mid = (start + end) // 2
        # if target is the mid value return FOUND
        if nums[mid] == target:
            return f"ITEM AT POSITION {mid + 1}"

        # Else re-adjust the start and end based of whether or not the mid value is larger or lesser than target
        if nums[mid] < target:
            start = mid + 1
            continue
        end = mid - 1

    return "ITEM NOT IN LIST"


print(binary_search([1, 3, 5, 7, 8, 9], 9))
