class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        def return_dict(x:str):
            temp = {}
            for i in x:
                if not temp.get(i):
                    temp[i] = 1
                else:
                    temp[i] += 1
            return temp
                
        sd = return_dict(s)
        td = return_dict(t)
        
        return sd == td
