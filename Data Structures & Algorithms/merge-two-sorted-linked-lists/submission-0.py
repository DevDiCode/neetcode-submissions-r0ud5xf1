# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        head1 = list1
        head2 = list2
        carry = 0 
        test = ListNode(None)
        sentinel = test


        while head1 and  head2:

            if head1.val<=head2.val:
                sentinel.next = head1
                head1 = head1.next
            else:
                sentinel.next = head2
                head2 = head2.next
            
            sentinel = sentinel.next

        
        if head1:
            sentinel.next = head1
        else:
            sentinel.next = head2

        return test.next
        