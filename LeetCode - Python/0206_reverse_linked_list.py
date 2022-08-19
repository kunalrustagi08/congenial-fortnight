# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # My approach
        oldHead = head
        
        if oldHead is None or oldHead.next is None:
            return head
        
        else:
            while oldHead.next:
                tempHead = oldHead.next
                #print(oldHead.val, tempHead.next.val, tempHead.val, head.val)
                oldHead.next = tempHead.next
                #print(oldHead.val, oldHead.next.val, tempHead.next.val, tempHead.val, head.val)
                tempHead.next = head
                print(oldHead.val, head.val)
                head = tempHead

            return head
        
        # Neetcode
        
#         prev, curr = None, head
        
#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp
        
#         return prev