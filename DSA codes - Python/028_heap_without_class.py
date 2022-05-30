from __future__ import annotations

def root_node():
    return data[0]

def last_node():
    return data[-1]

def insert(value):

    data.append(value)
    new_node_index = len(data) - 1

    while new_node_index > 0 and data[new_node_index] > data[parent_index(new_node_index)]:
        data[parent_index(new_node_index)], data[new_node_index] = data[new_node_index], data[parent_index(new_node_index)]

        new_node_index = parent_index(new_node_index)

def has_larger_child(index):

    flag = (data[left_child_index(index)] and data[left_child_index(index)] > data[index]) or \
            (data[right_child_index(index)] and data[right_child_index(index)] > data[index])
    
    return flag

def calculate_larger_child_index(index):

    if not data[right_child_index(index)]:
        return left_child_index(index)
    
    if data[right_child_index(index)] > data[left_child_index(index)]:
        return right_child_index(index)
    else:
        return left_child_index(index)

def delete():

    data.pop(0)
    trickle_node_index = 0

    while has_larger_child(trickle_node_index):

        larger_child_index = calculate_larger_child_index(trickle_node_index)
        data[trickle_node_index], data[larger_child_index] = data[larger_child_index], data[trickle_node_index]

        trickle_node_index = larger_child_index


def print_queue():
    print(data)

def left_child_index(index):
    return (index * 2) + 1

def right_child_index(index):
    return (index * 2) + 2

def parent_index(index):
    return (index - 1) // 2

data = []
insert(88)
insert(25)
insert(100)
insert(87)
insert(16)
insert(8)
insert(12)
print_queue()
delete()
print_queue()
delete()
print_queue()