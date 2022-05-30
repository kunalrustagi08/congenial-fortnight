def get_max_element(arr):

    max_element = arr[0]

    for i in arr:

        if i > max_element:
            max_element = i

    return max_element

arr = [1,5,0,2,9,10,-1]
print(get_max_element(arr))