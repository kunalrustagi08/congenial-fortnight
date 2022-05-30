def selection_sort(arr):

    max_index = 0
    
    for i in range(len(arr)-1):
        low_index = i

        for j in range(i+1, len(arr)):

            if arr[j] < arr[low_index]:
                low_index = j

        if i != low_index:    
            arr[i], arr[low_index] = arr[low_index], arr[i]

    return arr

arr = [1,5,0,2,9,10,-1]
print(selection_sort(arr))
