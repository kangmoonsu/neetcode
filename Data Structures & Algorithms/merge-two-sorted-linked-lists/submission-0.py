# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 결과를 담을 dummy 노드와 현재 위치를 가리킬 tail 포인터 생성
        dummy = ListNode() # new linkedlist
        tail = dummy # tail pointer 
        
        # 2. 두 리스트 모두 노드가 남아있을 때까지 비교하며 합침
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # tail 포인터 이동
            
        # 3. 한쪽 리스트가 남은 경우 통째로 이어 붙임
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        # dummy 다음 노드가 실제 병합된 리스트의 head
        return dummy.next