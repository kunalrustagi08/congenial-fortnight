class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.StackSize = 0

    
    def push(self, data):

        curr_pointer = Node(data)
        print(curr_pointer)
        if self.top is None:
            self.top = curr_pointer
            print(self.top)
            self.StackSize = self.StackSize + 1
        
        else:
            curr_pointer.next = self.top
            print(curr_pointer.next)
            self.top = curr_pointer
            print(self.top)
    
    def pop(self):
        try:
            if self.top == None:
                raise Exception("Stack is empty")
            else:
                curr_pointer = self.top
                self.top = self.top.next
                head_data = curr_pointer.data
                self.StackSize -= 1
                del curr_pointer
                return head_data
        except Exception as e:
            print(e)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
s.pop()
s.pop()
s.pop()