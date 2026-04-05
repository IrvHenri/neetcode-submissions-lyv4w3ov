# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Initialize pointers: prev starts as None, curr starts at head
        prev, curr = None, head
        
        while curr:
            # Save the next node before we change the current node's pointer
            temp = curr.next
            
            # Reverse the link: point current node backward to previous node
            curr.next = prev
            
            # Move prev forward to current (this will become new head at the end)
            prev = curr
            
            # Move curr forward to the next node we saved earlier
            curr = temp
        
        # Prev now points to the new head of the reversed list
        return prev



        