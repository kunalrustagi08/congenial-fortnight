def duplicate_char(arr):

    d = {i:0 for i in arr}

    for i in arr:
        if d[i] == 1:
            return i
        else:
            d[i] = 1
    
    return -1

arr =  ["a", "b", "c", "d", "c", "e","f"]
print(duplicate_char(arr))