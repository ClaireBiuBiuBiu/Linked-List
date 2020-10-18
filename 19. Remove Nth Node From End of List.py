#Given the head of a linked list, remove the nth node from the end of the list and return its head.

#Follow up: Could you do this in one pass?

''''
Approach 1: Two pass algorithm
Intuition

We notice that the problem could be simply reduced to another one : Remove the (L - n + 1)(L−n+1) th node from the beginning in the list ,
where LL is the list length. This problem is easy to solve once we found list length LL.

Algorithm

First we will add an auxiliary "dummy" node, which points to the list head. The "dummy" node is used to simplify some corner cases such as a list with only one node,
or removing the head of the list. On the first pass, we find the list length LL.
Then we set a pointer to the dummy node and start to move it through the list till it comes to the (L - n)(L−n) th node.
We relink next pointer of the (L - n)(L−n) th node to the (L - n + 2)(L−n+2) th node and we are done.'''
class ListNode:
    def __init__(self,val = 0,next=None):
        self.val = val
        self.next = None

class solution:
    def removeNthFromEnd(self,head: ListNode, n:int)-> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head

        while(first != None):
            length += 1
            first = first.next
        length -= n
        first = dummy

        while(first >0):
            length -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next

'''
Approach 2: One pass algorithm
Algorithm

The above algorithm could be optimized to one pass. 
Instead of one pointer, we could use two pointers. 
The first pointer advances the list by n+1n+1 steps from the beginning, while the second pointer starts from the beginning of the list. 
Now, both pointers are exactly separated by nn nodes apart. We maintain this constant gap by advancing both pointers together until the first pointer arrives past the last node. 
The second pointer will be pointing at the nnth node counting from the last. 
We relink the next pointer of the node referenced by the second pointer to point to the node's next next node.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(1,n+2):
            i += 1
            first = first.next
        while(first != None):
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next