import re


def unique_paths(x,y):
    
    if x < 1 or y < 1:
        return 0
    if x == 1 or y == 1:
        return 1
    
    return unique_paths(x-1,y) + unique_paths(x,y-1)

print(unique_paths(3,7))