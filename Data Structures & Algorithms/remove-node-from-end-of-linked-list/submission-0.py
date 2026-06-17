# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointers with fast at head and slow at dummy node
        # move fast pointer n steps
        # move both pointers until right hits end
        # slow.next is what to delete -> slow.next = slow.next.next

        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next