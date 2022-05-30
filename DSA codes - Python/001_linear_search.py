def linear_search(arr, x):

    for i in range(len(arr)):
        if x == arr[i]:
            return i
        elif x < arr[i]:
            return -1
        i += 1
    
    return -1
        

arr = [1,4,34,64,230,445,450]
x = 3
print(f'Element {x} at position:',linear_search(arr, x))

