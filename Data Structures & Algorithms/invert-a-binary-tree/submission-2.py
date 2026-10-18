# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 1. 왼쪽과 오른쪽 자식 노드 스왑
        root.left, root.right = root.right, root.left
        
        # 2. 하위 트리에 대해 재귀 호출
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root