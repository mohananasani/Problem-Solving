"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.
 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Statement

Used in navigation systems where we need to trace back a path.

When a user reaches a destination,
the system must show the return route in reverse order.

The path is stored as a linked list of locations.
We reverse the list to generate the backward route.

Scenario

A GPS navigation system stores the travel path as:

Home → Street A → Street B → Mall

Each location is connected like a linked list.

When the user wants to go back home,
the system must show:

Mall → Street B → Street A → Home

But:

• The data is stored only in forward direction
• We cannot create a new list (memory constraint)

So the system:

✔ Reverses the existing linked list
✔ Updates the pointers
✔ Generates the return route efficiently

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Time: O(n)
    Space:O(1)
    Approach: 3 pointers 
    Steps:
        You walk through the list, turning each arrow backward one by one.
    """
    def reverseList(self, head):
        
        # None and Single element
        if not head or head.next is None:
            return head
        count  = 1
        left = head
        middle = right = head.next
        
        while middle is not None:
            #increasing count
            count+=1

            # Maintaining the forward chain in right before changing the direction
            right = middle.next
            middle.next = left

            # Removing circular dependency of first element 
            if count == 2:
                left.next = None
                
            # moving left to forward
            left = middle

            #Moving middle to right after changing the direction
            middle = right

            
        head = left
        return head

# Improve coding standards of above 
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next     # store next
            curr.next = prev    # reverse pointer
            prev = curr         # move prev forward
            curr = nxt          # move curr forward

        return prev


        