class Node:
    def __init__(self,x:int or float):
        self.x = x
        self.next = None
    
class LinkedList:
    def __init__(self,x:int or float):
        self.head = Node(x)
        self.tail = self.head
        self.n = 0 
    def append(self,x:int or float):
        ''' insert element at the end of linked list (contiguous)'''
        if self.head == None:
            self.head=Node(x)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(x)
        self.tail = current.next
        self.n += 1
        return
    def print_traversal(self):
        ''' traverse and print the traversal (start at head) '''
        if self.head==None:return False
        self.nodes = [] 
        current = self.head
        while current.next:
            self.nodes.append(current.x)
            current = current.next
        self.nodes.append(current.x)
        print(*self.nodes)
        return 
    def peak_head(self):
        ''' get head value O(I) '''
        return self.head.x
    def peak_tail(self):
        ''' get tail value O(I)'''
        return self.tail.x
    def get_element(self,index:int):
        ''' Get element from given index (traversal)
        Best-scenario time complexity: O(I) - Constant Time
        Worst-scenario time complexity: O(n) - Linear Time'''
        i = 0 
        if self.head == None:return False
        current = self.head
        while current.next != None:
            i += 1
            current = current.next
            if i == index: return current.x
        return False
    def find(self,element:int or float):
        """ Find element from its value (traversal)
        Best-scenario time complexity: O(I) - Constant Time
        Worst-scenario time complexity: O(n) - Linear Time"""
        ix=0
        if self.head == None:return False
        current = self.head 
        while current.next != None:
            if current.x == element: return ix
            current = current.next
            ix += 1
        return False
    def remove_element(self,value):
        ''' Remove element from its value'''
        current = self.head
        if self.head.x == value:
            self.head = self.head.next
            return
        if self.tail.x == value:
            temp = 0
            while current.next != None:
                temp = current
                current = current.next
            self.tail = temp
            self.tail.next = None
            return
        while current.next != None:
            current = current.next
            if current.next.x == value:
                current.next = current.next.next
                return
        return False
    def insert(self,value:int or float,index:int):
        """ Insert new element node(value)  between index and index + 1 (start index = 0)"""
        ix = 0 
        current = self.head
        while current.next:
            if index == ix: 
                temp = current.next
                current.next = Node(value)
                current.next.next = temp
                return
            ix+=1
            current = current.next
        return

ll = LinkedList(1)
for i in range(2,11):
    ll.append(i)

ll.print_traversal()
print(ll.peak_head())
print(ll.peak_tail())          
print(ll.get_element(3))
print(ll.find(2))
print(ll.find(1000))
ll.remove_element(3)
ll.print_traversal()
ll.remove_element(1)
ll.print_traversal()
ll.remove_element(10)
ll.print_traversal()
ll.insert(100,2)
ll.print_traversal()

