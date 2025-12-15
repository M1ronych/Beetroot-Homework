def binary_search_recursive(arr,target,left=0,right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search_recursive(arr,target,left,mid - 1)
    else:
        return binary_search_recursive(arr,target,mid + 1,right)

