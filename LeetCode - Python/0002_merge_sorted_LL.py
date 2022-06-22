class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
    final_list = ListNode()
    head = final_list
    
    while list1.next != None or list2.next != None:
        
        if list1.val <= list2.val:
            temp = ListNode(list1.val)
            
            if final_list == head:
                head = temp
                final_list = head
                
            else:
                final_list.next = temp
                final_list = final_list.next
            list1 = list1.next
        
        else:
            temp = ListNode(list2.val)
            
            if final_list == head:
                head = temp
                final_list = head
                
            else:
                final_list.next = temp
                final_list = final_list.next
            list2 = list2.next
    
    return head
                