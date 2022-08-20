# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Approach 1: Using Floyd Tortoise and Hare algorithm, time is O of n, space is O of 1 (Nicee!!!)
        # Link to algo and explanation
        # https://www.youtube.com/watch?v=gBTe7lFR3vc
        
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
        
#         # Approach 2: Using hashtable, time is O of n, space is also O of n (Boooo!!!)
#         index_dict = {}
#         curr = head
        
#         while curr:
#             if curr not in index_dict.keys():
#                 index_dict[curr] = True
#             else:
#                 return True
#             curr = curr.next

#         return False
                