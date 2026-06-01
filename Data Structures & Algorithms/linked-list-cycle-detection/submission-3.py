# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # tortoise and hare approach
        # slow pointer, fast pointer
        # slow moves 1x speed, fast moves 2x speed
        # while fast.next.next:
        # slow = slow.next, fast = fast.next.next
        # if slow == fast -> return True, else return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False