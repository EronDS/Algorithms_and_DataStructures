# ABT implement through DoublyLinkedList

class Node:
    def __init__(self,x:int or float):
        self.x = x 
        self.next = None
        self.prev = None

class Deque:
    def __init__(self,x): 
        self.head = Node(x)
        self.tail = self.head
        
    def addFront(self,x):
        if self.head:
            temp = self.head
            self.head = Node(x)
            self.head.next = temp 
            self.head.next.prev = self.head
            return
    def addBack(self,x):
        if self.tail:
            temp = self.tail
            self.tail = Node(x)
            self.tail.prev = temp
            self.tail.prev.next = self.tail
            return
    def frontTraversal(self):
        nodes = [] 
        curr = self.head
        while curr.next:
            nodes.append(curr.x)
            curr = curr.next
        nodes.append(curr.x)
        return print(' -> '.join([str(i) for i in nodes]))
    def backTraversal(self):
        curr = self.tail 
        nodes = [] 
        while curr.prev:
            nodes.append(curr.x)
            curr = curr.prev
        nodes.append(curr.x)
        return print(' <- '.join([str(i) for i in nodes]))

    def peekFront(self): return(print(self.head.x))
    def peekBack(self): return(print(self.tail.x))

    def removeFront(self): 
        if self.head:
            self.head = self.head.next
            self.head.prev = None
            return
    def removeBack(self):
        if self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

  
