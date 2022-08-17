class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Double pointer approach
        s = s.lower()
        
        string = ''.join(ch for ch in s if ch.isalnum())
        
        l = 0
        h = len(string) - 1
        while l <= h:
            if string[l] != string[h]:
                return False
            l += 1
            h -= 1
        
        return True
        