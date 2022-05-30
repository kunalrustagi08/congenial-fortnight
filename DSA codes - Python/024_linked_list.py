class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_front(self, data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp
    
    def insert_at_end(self, data):
        temp = Node(data)
        # print(1, temp.data, temp.next, temp)
        if self.head == None:
            self.head = temp
        else:
            curr = self.head
            while curr.next != None:
                # print(curr.data, curr.next, curr)
                curr = curr.next
            curr.next = temp
    
    def insert_after(self, data, index):
        curr = self.head
        count = 1
        while count < index - 1 and curr.next != None:
            curr = curr.next
            count += 1
        temp = Node(data)
        temp.next = curr.next
        curr.next = temp

    def traverse(self):
        curr = self.head
        while curr != None:
            print(curr.data, end=" > ")
            curr = curr.next
        print()
    
    def delete_from_front(self):
        if self.head == None:
            print("Empty LL")
        else:
            temp = self.head
            self.head = self.head.next
            del temp
    
    def delete_from_end(self):
        if self.head == None:
            print("Empty LL")
        else:
            curr = self.head
            prev = None
            while curr.next != None:
                prev = curr
                curr = curr.next
            prev.next = curr.next
            del curr

    def delete_at_index(self, index):
        if self.head == None:
            print("Empty LL")
        else:
            curr = self.head
            prev = None
            count = 1
            while count < index and curr.next != None:
                prev = curr
                curr = curr.next
                count += 1
            prev.next = curr.next
            del curr

    def get_last_element(self):
        curr = self.head
        while curr != None:
            prev = curr
            curr = curr.next
        print(prev.data)
    
    def reverse_list(self):
        pnode = None
        cnode = self.head
        

        while cnode != None:
            nnode = cnode.next
            cnode.next = pnode
            pnode = cnode
            cnode = nnode

        self.head = pnode
        


L = LinkedList()
L.insert_at_end(9)
# print()
# L.traverse()
L.insert_at_end(3)
# print()
# L.traverse()
L.insert_at_end(12)
# print()
# L.traverse()
# L.insert_at_front(10)
# print()
# L.traverse()
L.insert_at_end(2)
# print()
# L.traverse()
L.insert_at_end(102)
# print()
# L.traverse()
# L.insert_at_front(130)
# print()
# L.traverse()
# L.delete_from_end()
# L.delete_from_front()
# L.delete_from_end()
# L.delete_from_front()
# print()
L.traverse()
# L.get_last_element()
L.reverse_list()
L.traverse()