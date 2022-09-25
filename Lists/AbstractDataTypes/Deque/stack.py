
class Node:
    def __init__(self,x):
        self.x = x
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.n = 0 
    def push(self,new_element):
        if self.head == None:
            self.head = Node(x=new_element)
            self.n+=1
            return
        if self.head != None:
            curr = self.head
            self.head = Node(x=new_element)
            self.head.next = curr
            self.n+=1
            return
        return 
    def top(self): 
        if self.head: return(print(self.head.x))
        return False
    def traversal(self):
        nodes = [] 
        curr = self.head
        while curr.next:
            nodes.append(curr.x)
            curr = curr.next
        nodes.append(curr.x)
        return print(' -> '.join([str(i) for i in nodes]))
    def pop(self):
        if self.head:
            self.head = self.head.next
            return
