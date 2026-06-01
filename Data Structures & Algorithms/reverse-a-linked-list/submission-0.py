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
            next_node = curr.next  # make sure we don't lose the next node
            curr.next = prev       # reverse the direction of the pointer
            prev = curr            # set the current node to prev
            curr = next_node       # move on

        return prev