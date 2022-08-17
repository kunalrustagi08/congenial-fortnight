class Solution:
    def isValid(self, s: str) -> bool:
        
        hashmap = { ')':'(', '}':'{', ']':'[' }
        
        test = []
        
        for i in s:
            if i not in hashmap.keys():
                test.append(i)
            else:
                if test == [] or hashmap[i] != test[-1]:
                    return False
                else:
                    test.pop()

        return not test
        
            