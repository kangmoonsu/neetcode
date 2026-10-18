# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = deque([root]) # 큐 초기화
        
        while q:
            level = []
            # 현재 레벨에 있는 노드의 개수만큼만 반복
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                
                # 자식 노드가 있으면 큐에 추가 (다음 레벨 탐색 대상)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(level)
            
        return res