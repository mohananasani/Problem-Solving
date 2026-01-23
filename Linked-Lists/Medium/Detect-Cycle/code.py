"""
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.


Statement

Used in systems where data flows through connected nodes
and we need to ensure the path does not loop infinitely.

When a system processes linked data,
it must detect whether the path forms a cycle.

The data is stored as a linked list of nodes.
We check if any node points back to a previous node.

Scenario

A task management system stores workflow steps as:

Start → Review → Approval → Completion

Each step is connected like a linked list.

Due to a configuration error,
the Completion step points back to Review:

Start → Review → Approval → Completion
                           ↖───────────────

This creates a cycle in the workflow.

If not detected:

The system may enter an infinite loop

Tasks may never complete

Resources may be wasted

So the system:

✔ Traverses the linked list
✔ Detects whether a cycle exists
✔ Prevents infinite processing
✔ Ensures system stability

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        if not head :
            return False

        slow = fast = head
        # Checking current and next one is valid
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # intersected
            if slow == fast:
                return True

        return False
        