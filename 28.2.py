def merge_sort(arr):
    if len(arr) <= 1:
        return

    temp = [None] * len(arr)
    _merge_sort(arr,temp,0, len(arr) - 1)


def _merge_sort(arr,temp,left,right):
    if left >= right:
        return

    mid = (left + right) // 2

    _merge_sort(arr,temp,left,mid)
    _merge_sort(arr,temp,mid + 1,right)
    _merge(arr,temp,left,mid,right)

def _merge(arr,temp,left,mid,right):
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k +=1

    while i <=mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for idx in range(left,right + 1):
        arr[idx] = temp[idx]


data = [38,27,43,3,9,82,10]
merge_sort(data)
print(data)



