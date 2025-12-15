import random
import time

def insertion_sort(arr,left,right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1

        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
def quicksort(arr,limit=10):
    _quicksort(arr,0,len(arr) - 1,limit)

def _quicksort(arr,low,high,limit):
    if high - low + 1 <= limit:
        insertion_sort(arr,low,high)
        return

    if low < high:
        p = partition(arr,low,high)
        _quicksort(arr,low,p - 1,limit)
        _quicksort(arr,p + 1,high,limit)

def  partition(arr,low,high):
    pivot = arr[high]
    i = low - 1

    for j in range(low,high):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i + 1],arr[high] = arr[high], arr[i + 1]
    return i + 1

def test(limit,size=10_000):
    data = [random.randint(0,1_000_000) for _ in range(size)]
    start = time.time()
    quicksort(data,limit)
    return time.time() - start

for limit in [0,5,10,20,50]:
    print(f"limit={limit}:{test(limit):.4f} sec")




