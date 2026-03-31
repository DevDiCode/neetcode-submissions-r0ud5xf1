# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        sentinel = ListNode(0,head)

        slow = fast = sentinel

        for i in range(n):
            fast = fast.next 

        
        while fast and  fast.next:
            slow = slow.next 
            fast = fast.next
        

        next = slow.next.next if slow.next.next else None

        slow.next = next 

        return sentinel.next

        