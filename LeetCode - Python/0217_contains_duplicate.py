class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Hashmaps
        duplicate_dict = set()
        
        for i in nums:
            if i in duplicate_dict:
                return True
            duplicate_dict.add(i)
        
        return False
