from sys import stdin

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self,head):
        self.head = head
        
    def display(self):
        current = self.head
        while current is not None:
            print(current)
            current = current.next
            
    def push(self,value):
        head = self.head
        self.head = Node(value)
        self.head.next = head

    def pop(self):
        head = self.head
        self.head = head.next
        return head

    def peek(self):
        return self.head
        
node1 = Node(12)
node2 = Node(99)
node3 = Node(37)

node1.next = node2
node2.next = node3

L = LinkedList(node1)
L.peek()

  

