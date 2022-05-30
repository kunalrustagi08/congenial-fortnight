def partition(left ,right):

    pivot_index = right
    pivot = arr[pivot_index]
    right = right - 1

    while True:

        while arr[left] < pivot:
            left += 1
        
        while arr[right] > pivot:
            right -= 1
        
        if left >= right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
    
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]

    return left


def quick_sort(left, right):
    if right - left <= 0:
        return
    
    pivot = partition(left, right)
    quick_sort(left, pivot-1)
    quick_sort(pivot+1, right)


def quickselect(index, left, right):

    if right - left <= 0:
        print("1:", left, right, arr)
        print(arr[left])
        return arr[left]

    pivot = partition(left, right)

    if index < pivot:
        quickselect(index, left, pivot-1)
    elif index > pivot:
        quickselect(index, pivot+1, right)
    else:
        print("2:", left, right, pivot, arr)
        print(arr[pivot])
        return arr[pivot]


arr = [0,5,2,1,6,3]    
# quick_sort(arr, 0, 5)
print(arr)
x = quickselect(1, 0, 5)
print(x)