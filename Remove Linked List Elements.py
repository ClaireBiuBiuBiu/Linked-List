'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head
        #这样设置是防止 head是要被删掉的 设置一个前置node 这样head永远在中间 是一种standarize的方法
        prev, curr = sentinel, head

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr =curr.next
        return sentinel.next