# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# iterative
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack: list[TreeNode] = []
        pointer = root
        while pointer or stack:
            if pointer is not None:
                stack.append(pointer)
                pointer = pointer.left 
            elif stack:
                pointer = stack.pop()
                pointer.right, pointer.left = pointer.left, pointer.right
                pointer = pointer.left
            else:
                break
        return root
    
# recursive
# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if root is None:
#             return
#         root.left, root.right = root.right, root.left
#         self.invertTree(root.left)
#         self.invertTree(root.right)
#         return root