''' 
In heap -> keep an balanced tree O(logn) search through values (keys);


Binary Min  Array implementation (priority queue)

2 Properties: 1. Binary Tree, 2. Heap Property

1.1. Every node has 0,1 or 2 children.

2.1. Complete Tree (filled left to right)

2.2.1. Min Heap: Every parent key must be smaller than its children nodes; Root node: Minimum key -- Constant Time finding mix value (O(1))
2.2.2. Max Heap: Every parent key must be higher than its children nodes; Root node: Largest Key -- Constant Time finding max value (O(1))


MIN HEAP
- INSERTING (HEAPIFY) -> insert at left (heap property 2.1.), if children key (value) < parent: parent = children, children = parent (SWAP)

parent_index = children_index // 2
left_children_index = 2*parent_index 
Right_children_index = 2*parent_index + 1



Insert (at leftmost empty place) and Heapify 
Remove -> Keep Heap priority


'''
class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0
    
    def insert(self,new_element):
        self.heap.append(new_element)
        self.size += 1
        self.percolateUp(self.size) # last leaf inserted (left to right)
    
    def percolateUp(self, i):
        ''' heapify -> Heal functio to insert -> check and change accordingly 
        from leaf to root | Worst Case: (O(logn))'''
        while i // 2 > 0: # percolate up until root 
            if self.heap[i//2] > self.heap[i]: # check heap property, change parent and child if child < than parent
                temp = self.heap[i//2]
                self.heap[i//2] = self.heap[i]
                self.heap[i] = temp
            i = i // 2 # change current node to parent (and check heap property again)
    def get_minChild(self,i):
        if self.size < 2* i+1: return 2*i
        if self.size >= 2*i+1:
            if self.heap[2*i+1] < self.heap[2*i]:
                return 2*i+1
            else: return 2*i
    def percolateDown(self,i):
        while 2*i <= self.size:
            minChild = self.get_minChild(i)
            if self.heap[i] > self.heap[minChild]:
                temp = self.heap[i]
                self.heap[i] = self.heap[minChild]
                self.heap[minChild] = temp
            i = minChild
    
    def deleteMin(self):
        head = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.percolateDown(1)


mh = MinHeap()
mh.insert(10)
print(mh.heap[1:])
mh.insert(20)
print(mh.heap[1:])
mh.insert(5)
print(mh.heap[1:])
mh.insert(8)
print(mh.heap[1:])
mh.insert(0)
print(mh.heap[1:])
mh.deleteMin()
print(mh.heap[1:])
    
