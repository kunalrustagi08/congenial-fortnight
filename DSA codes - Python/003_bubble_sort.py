def bubble_sort_1(arr):

    l = len(arr)

    for i in range(l-1):
        for j in range(i,l):

            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    
    return arr

def bubble_sort_2(arr):

    index_decrement = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True

        for i in range(index_decrement):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
            
            index_decrement -= 1        # Since the last element is always sorted after an iteration, no need to check it again
    
    return arr

arr = [1,7,3,9,0,2]
print(bubble_sort_1(arr))
print(bubble_sort_2(arr))