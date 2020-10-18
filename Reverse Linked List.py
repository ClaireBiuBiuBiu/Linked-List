'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?


Approach #1 (Iterative) [Accepted]
Assume that we have linked list 1 → 2 → 3 → Ø, we would like to change it to Ø ← 1 ← 2 ← 3.

While you are traversing the list, change the current node's next pointer to point to its previous element.
Since a node does not have reference to its previous node, you must store its previous element beforehand.
You also need another pointer to store the next node before changing the reference. Do not forget to return the new head reference at the end!
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            Temp = curr.next
            curr.next = prev# first element, before it will become null
            prev = curr
            curr = Temp
        return prev


'''
solution
In this article, we will talk more about details of our algorithm to reverse the linked list.

In the solution we mentioned previously, there are two nodes which we should keep track of: 
the original head node and the new head node.

Therefore, we need to use two pointers in one linked list at the same time. 
One pointer head always points at our original head node while another pointer curHead always points at our newest head node.

Let's focus on a single step (the 2nd step in the previous article). 
Our goal is to move the next node of head, which is 15, to the head of the list.



1. First, we use a temporary pointer p to indicate the next node of the head node. And link the "next" field of head to the "next" field of p.



2. Then, we link the "next" field of p to the curHead.



3. Now our linked list actually looks like the picture below. And we set curHead to be p.



By this way, we successfully move node 15 to the head of the list. And we can repeat this process until the next node of head is null.
'''