class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # Solution 1
        if len(a) > len(b):
            b = '0'*(len(a) - len(b)) + b
        elif len(a) < len(b):
            a = '0'*(len(b) - len(a)) + a
        
        print(a,b)
        res = ''
        sum = 0
        carry = 0
        
        for i in range(1,len(a)+1):
            sum = carry + int(a[-i]) + int(b[-i])
            if sum == 0:
                res = '0' + res
                carry = 0
            elif sum == 1:
                res = '1' + res
                carry = 0
            elif sum == 2:
                res = '0' + res
                carry = 1
            elif sum == 3:
                res = '1' + res
                carry = 1
            print(i,sum,carry)
        
        if carry == 1:
            res = '1' + res
        return res
        
        # Solution 2: more efficient
        # return str(bin(int(a, base = 2)+int(b, base = 2)))[2:]
        