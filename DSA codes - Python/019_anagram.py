from operator import le
import re


def anagrams_of(s):

    if len(s) == 1:
        return [s[0]]
    
    collection = []
    substring_anagrams = anagrams_of(s[1:])
    print(1, substring_anagrams)

    for substring in substring_anagrams:

        for index in range(len(substring)+1):

            # print(substring)

            copy = str(substring)
            collection.append(copy[:index] + s[0] + copy[index:])
            print(2, collection)
    
    return collection

print(anagrams_of('abc'))


"""
1st R: abc => bc
2nd R: bc => c
3rd R: c

2nd R:
sa = [c]
for element in ['c']:
    for i in 2:
        collection.append(''+b+c)
        collection.append(c+b+'')

c = [bc, cb]

1st R:
sa = [bc, cb]




"""