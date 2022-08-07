# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive solution
class Solution1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, root, result):
        if root is None:
            return
        self.traverse(root.left, result)
        result.append(root.val)
        self.traverse(root.right, result)

# Iterative solution
class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root
        while(curr != None or stack):
            while(curr != None):
                stack.append(curr)
                curr = curr.left
            curr = stack[-1]
            stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result
