# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodeValues = []
        for l in lists:
            while l is not None:
                nodeValues.append(l.val)
                l = l.next

        sortedValues = sorted(nodeValues)
        answer = pointer = ListNode(0, None)
        for value in sortedValues:
            current = ListNode(value, None)
            pointer.next = current
            pointer = pointer.next
        return answer.next
