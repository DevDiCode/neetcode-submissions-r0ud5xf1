# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        """


        test -> 1- > 2 ->3 -> 4 -> 5
                         s       f       
        """
        sentinel = ListNode(0,head)

        temp = sentinel 
        
        slow = temp 
        fast = temp 

        for _ in range(n):
            fast = fast.next

        
        while fast.next :
            slow = slow.next 
            fast = fast.next 
        


        slow.next = slow.next.next

        return sentinel.next


