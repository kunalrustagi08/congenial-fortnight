class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Solution 1
        """
        my_dict = {}
        
        for i in nums:
            my_dict[i] = 1 + my_dict.get(i, 0)
        
        key1= 0 
        for i in nums:
            key1 = i
            
            if my_dict.get(target - i) and (target - i) == i and my_dict[i] > 1:
                break
            elif my_dict.get(target - i) and (target - i) != i:
                break
                 

        for i in range(len(nums)):
            if key1 == nums[i]:
                first = i

        for i in range(len(nums)):
            if target - key1 == nums[i] and i != first:
                second = i

        return [first, second]
        """

        #Solution 2: concise and efficient
        h = {}
        result = []
        for i, num in enumerate(nums):
            temp = target - num
            if temp in h:
                return [h[temp], i]
            h[num] = i
                
