class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        final_list = None
        head = None
        
        while list1 != None and list2 != None:
            
            if list1.val <= list2.val:
                temp = ListNode(list1.val)
                
                if head == None:
                    head = temp
                    final_list = head
                    
                else:
                    final_list.next = temp
                    final_list = final_list.next
                print("1:", temp.val, head.val)
                list1 = list1.next
                
            
            else:
                temp = ListNode(list2.val)
                
                if head == None:
                    head = temp
                    final_list = head
                    
                else:
                    final_list.next = temp
                    final_list = final_list.next
                print("2:", temp.val, head.val)
                list2 = list2.next
        
        
        while list1 == None and list2 != None:
            
            temp = ListNode(list2.val)
            
            if head == None:
                head = temp
                final_list = head

            else:
                final_list.next = temp
                final_list = final_list.next
            print("3:", temp.val, head.val)
            list2 = list2.next
        
        while list2 == None and list1 != None:
            
            temp = ListNode(list1.val)
            
            if head == None:
                head = temp
                final_list = head

            else:
                final_list.next = temp
                final_list = final_list.next
            print("4:", temp.val, head.val)
            list1 = list1.next
                
            
        return head