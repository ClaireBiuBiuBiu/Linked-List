'''
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
'''

class ListNode:
    def __init__(self,x):
        self.val = x
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNoed(0)
        self.tail = ListNode(0)
        self.head.next =self.tail
        self.tail.prev = self.head

    def get(self,index):
        if index <0 or index >= size.self:
            return -1
        if index + 1 <self.size-index:
            curr = self.head
            for i in range(index+1):
                curr = curr.next
        else:
            curr = self.tail
            for i in range(self.size-index):
                curr = curr.prev
        return curr.val

    def addAtHead(self,val):
        pred, succ = self.head, self.head.next

        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        succ.prev = to_add
        pred.next = to_add

    def addAtTail(self,val):
        pred, succ = self.tail.prev, self.tail

        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        succ.prev = to_add
        pred.next = to_add

    def addAtIndex(self,index,val):
        if index > self.size:
            return
        if index<0
            index = 0

        if index < self.size -index:
            pred = self.head
            for i in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.head
            for i in range(self.size-index):
                succ = succ.prev
            pred = succ.prev
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        succ.prev = to_add
        pred.next = to_add

    def deleteAtIndex(self,index):
        if index <0 or index >=self.size:
            return
        if index<self.size -index:
            pred = self.head
            for i in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for i in range(self.size-index-1):
                succ = succ.prev
            pred = succ.prev.prev
        self.size -=1

        pred.next = succ
        succ.prev = pred

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)