from __future__ import annotations

class Heap:

    data = []
    
    def __init__(self):
        pass

    def initialize(self):
        data = []
    
    def root_node(self):
        return self.data[0]
    
    def last_node(self):
        return self.data[-1]

    def insert(self, value):

        self.data.append(value)
        new_node_index = len(self.data) - 1

        while new_node_index > 0 and self.data[new_node_index] > self.data[parent_index(new_node_index)]:
            self.data[parent_index(new_node_index)], self.data[new_node_index] = self.data[new_node_index], self.data[parent_index(new_node_index)]

            new_node_index = parent_index(new_node_index)
    
    def has_larger_child(self, index):

        flag = (self.data[left_child_index(index)] and self.data[left_child_index(index)] > self.data[index]) or \
               (self.data[right_child_index(index)] and self.data[right_child_index(index)] > self.data[index])
        
        return flag
    
    def calculate_larger_child_index(self, index):

        if not self.data[right_child_index(index)]:
            return left_child_index(index)
        
        if self.data[right_child_index(index)] > self.data[left_child_index(index)]:
            return right_child_index(index)
        else:
            return left_child_index(index)
    
    def delete(self):

        del self.data[0]
        trickle_node_index = 0

        while self.has_larger_child(trickle_node_index):

            larger_child_index = self.calculate_larger_child_index(trickle_node_index)
            self.data[trickle_node_index], self.data[larger_child_index] = self.data[trickle_node_index], self.data[larger_child_index]

            trickle_node_index = larger_child_index
    

    def print_queue(self):
        print(self.data)

def left_child_index(index):
    return (index * 2) + 1

def right_child_index(index):
    return (index * 2) + 2

def parent_index(index):
    return (index - 1) // 2

h = Heap()
h.initialize()
h.insert(88)
h.insert(25)
h.insert(100)
h.insert(87)
h.insert(16)
h.insert(8)
h.insert(12)
h.print_queue()
h.delete()
h.print_queue()