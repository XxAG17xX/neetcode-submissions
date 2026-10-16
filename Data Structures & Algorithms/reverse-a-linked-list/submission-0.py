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
            nextNode = curr.next   #save where curr currently points
            curr.next = prev       #reverse the link
            prev = curr            #move prev forward
            curr = nextNode        #move curr forward

        return prev