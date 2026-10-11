# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next  
            curr.next = prev 
            prev = curr      
            curr = nxt       
            
        return prev  # 반복이 끝나면 prev가 새로운 head가 됨