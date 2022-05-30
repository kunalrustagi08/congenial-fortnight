class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.leftChild = left
        self.data = data
        self.rightChild = right
    
def search(searchValue, node):
    if node is None or node.data == searchValue:
        print(node.data)
        return node
    
    elif searchValue < node.data:
        print("In less than operation", node.data)
        return search(searchValue, node.leftChild)
    
    else:
        print("In greater than operation", node.data)
        return search(searchValue, node.rightChild)

def traverse(node):
    if node is None:
        return
    print(node.data)
    traverse(node.leftChild)
    traverse(node.rightChild)

def insert(value, node):
    if value < node.data:
        if node.leftChild is None:
            node.leftChild = TreeNode(value)
        else:
            insert(value, node.leftChild)
    
    elif value > node.data:
        if node.rightChild is None:
            node.rightChild = TreeNode(value)
        else:
            insert(value, node.rightChild)

def deletion(value, node):

    if node is None:
        return None
    
    elif value < node.data:
        node.leftChild = deletion(value, node.leftChild)
        return node
    elif value > node.data:
        node.rightChild = deletion(value, node.rightChild)
        return node
    
    elif value == node.data:
        if node.leftChild is None:
            return node.rightChild
        elif node.rightChild is None:
            return node.leftChild
        else:
            node.rightChild = lift(node.rightChild, node)
            return node

def lift(node, nodeToDelete):
    if node.leftChild:
        node.leftChild = lift(node.leftChild, nodeToDelete)
        return node
    else:
        nodeToDelete.data = node.data
        return node.rightChild

def right(node):
    if node.rightChild is None:
        return node.data
    else:
        return right(node.rightChild)



node1 = TreeNode(25)
node2 = TreeNode(75)
root = TreeNode(50, node1, node2)

search(25, root)
# traverse(root)
insert(12, root)
insert(26, root)
insert(52, root)
insert(79, root)
insert(55, root)
traverse(root)
# deletion(25,root)
# traverse(root)
# right(root)