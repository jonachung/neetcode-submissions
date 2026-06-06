# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # have a dummy node head and a node that references head
        # loop through list1 and list2
        # if list1.val < list2.val -> add list1 to node.next and increment list1
        # else -> add list2 to node.next and increment list2
        # increment node to node.next

        # if list1 or list2 still left, add rest to node.next
        # return head.next
        head = ListNode()
        node = head

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return head.next