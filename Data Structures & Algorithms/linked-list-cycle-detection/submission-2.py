# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast = head
        slow = head


        while slow and fast.next:

            slow = slow.next
            fast = fast.next.next

            if fast and fast == slow:
                return True
            if not fast:
                return False
            
        return False
