def get_intersection(x,y):
    intersection = []
    for key in x.keys():
        if y.get(key):
            intersection.append(key)
    
    return intersection
            


a = [1,3,5,7,9]
b = [0,2,3,7,1]


x = {i:True for i in a}
y = {i:True for i in b}

print(get_intersection(x,y))