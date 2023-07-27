# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        stack: list[TreeNode] = []
        pointer = root
        while pointer or stack:
            if pointer is not None:
                stack.append(pointer)
                pointer = pointer.left 
            elif stack:
                pointer = stack.pop()
                pointer.right, pointer.left = pointer.left, pointer.right
                values.append(pointer.val)
                pointer = pointer.left
            else:
                break
        return values