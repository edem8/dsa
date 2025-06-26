def Linear_search(arr, target):
    # basically go through all of the array or list
    # works on Unsorted or sorted lists
    #  O(n)

    for i in len(arr):
        if arr[i] == target:
            return True

    return False
