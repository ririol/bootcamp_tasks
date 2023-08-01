class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []
        pointer = root
        stack = []
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
        
        for i in range(1, len(values)):
            if values[i] <= values[i-1]:
                return False

        return True