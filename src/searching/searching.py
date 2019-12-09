# STRETCH: implement Linear Search				
def linear_search(arr, target):
    for x in range(0, len(arr)):
        if arr[x] == target:
            return x

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
    low = 0
    high = len(arr)-1

    if len(arr) == 0:
        return -1 # array empty
    elif arr[low] > target > arr[high]:
        return -1 # not found

    # TO-DO: add missing code
    while True:
        guess = (high + low) // 2
        if arr[guess] == target:
            return guess
        elif arr[guess] > target:
            high = guess
        elif arr[guess] < target:
            low = guess


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1 # array empty
    elif arr[low] > target > arr[high]:
        return -1

    if arr[middle] == target:
        return middle
    elif arr[middle] < target:
        return binary_search_recursive(arr, target, middle, high)
    else:
        return binary_search_recursive(arr, target, low, middle)