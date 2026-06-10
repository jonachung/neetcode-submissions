# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        
        solution = ListNode()
        cur = solution
        
        while l1 or l2 or carry > 0:
            if (l1 != None):
                value1 = l1.val
            else:
                value1 = 0
                
            if (l2 != None):
                value2 = l2.val
            else:
                value2 = 0
                
            # find digit
            value = value1 + value2 + carry
            carry = value // 10 # get carry
            value = value % 10 # after carry
            
            cur.next = ListNode(value)
            
            # update l1 and l2 and cur
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return solution.next