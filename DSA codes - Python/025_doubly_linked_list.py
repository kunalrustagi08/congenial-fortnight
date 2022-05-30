class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class DoublingLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_front(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            temp = Node(data)
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
    
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            temp = Node(data)
            temp.prev = self.tail
            self.tail.next = temp
            self.tail = temp
    
    def insert_at_index(self, data, index):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            temp = Node(data)
            pos = 1
            curr = self.head
            while pos < index - 1 and curr.next != None:
                curr = curr.next
                pos += 1
            temp.prev = curr
            temp.next = curr.next
            curr.next = temp
            temp.next.prev = temp

    def traverse(self):
        curr = self.head
        while curr != None:
            print(curr.data, end=" ,")
            curr = curr.next
    
    def remove_from_front(self):
        if self.head == None:
            print("Empty DLL")
        else:
            self.head = self.head.next
            del self.head.prev
            self.head.prev = None
    
    def reverse_print(self):
        curr = self.tail
        while curr != None:
            print(curr.data, end=" ,")
            curr = curr.prev


DLL = DoublingLinkedList()
DLL.insert_at_front(2)
DLL.insert_at_end(5)
DLL.insert_at_end(19)
DLL.insert_at_front(-1)
DLL.insert_at_index(34,2)
DLL.insert_at_index(23,2)
# DLL.traverse()
# DLL.remove_from_front()
DLL.traverse()
DLL.reverse_print()
