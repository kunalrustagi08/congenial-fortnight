def binary_search(arr, x):

    low = 0
    high = len(arr) - 1

    while (low <= high):
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            high = mid - 1
        elif x > arr[mid]:
            low = mid + 1
    return -1


arr = [1,4,34,64,230,445,450]
x = 34
print(f'Element {x} at position:',binary_search(arr, x))