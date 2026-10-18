# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 노드가 없으면 깊이는 0
        if not root:
            return 0
        
        # 1 + max(왼쪽 서브트리 깊이, 오른쪽 서브트리 깊이)
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))