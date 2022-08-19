class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # binary search, O(log n)

        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = low + (high - low)//2             # this -> (low + high) // 2 may lead to overflow in languages like C++, Java, 
                                                    # since int is bounded, not in Python
            # print(mid, nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1
        