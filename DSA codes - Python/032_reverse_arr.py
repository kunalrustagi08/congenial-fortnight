def reverse_array(arr):

    temp = 0
    i = len(arr) - 1
    max_len = len(arr) - 1

    print(arr)

    while i >= max_len//2:
        arr[len(arr)-1 - i], arr[i] = arr[i], arr[len(arr)-1 - i]
        i -= 1
    print(arr)

reverse_array([1,2,3,4,5,6,])

    
