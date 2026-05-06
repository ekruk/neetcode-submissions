# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head
        nex = head

        #edge cases are the first addition, and last addition

        while head is not None:

            nex = head.next
            head.next = prev
            prev = head 
            head = nex 


        return prev

        