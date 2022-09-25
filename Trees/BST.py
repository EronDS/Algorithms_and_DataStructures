# need to implement remove operation and annotate

class Node:
    def __init__(self,x:int or float):
        self.value = x 
        self.right = None
        self.left = None


class BST:
    def __init__(self,x):
        self.root = Node(x)
    
    def insert(self,new_element):
        curr = self.root
        while curr:
            if new_element >= curr.value:
                if curr.right: curr = curr.right
                else:
                    curr.right = Node(new_element)
                    return
            if new_element < curr.value:
                if curr.left: curr = curr.left
                else:
                    curr.left = Node(new_element)
                    return
        return False
    
    def post_order_traversal(self, node = None):
        'LRV traversal'
        if node == None: curr = self.root
        if node != None: curr = node
        if curr.left != None: self.post_order_traversal(curr.left)
        if curr.right != None: self.post_order_traversal(curr.right)
        if curr: print(curr.value)
        return
    def in_order_traversal(self,node = None):
        'LVR traversal'
        if node == None: curr = self.root
        if node != None: curr = node
        if curr.left: self.in_order_traversal(curr.left)
        if curr: print(curr.value)
        if curr.right: self.in_order_traversal(curr.right)
        return

    def pre_order_traversal(self,node = None):
        'VLR traversal'
        if node == None: curr = self.root
        if node != None: curr = node
        if curr: print(curr.value)
        if curr.left: self.pre_order_traversal(curr.left)
        if curr.right: self.pre_order_traversal(curr.right)

    def find_minimum_node(self):
        '''traverse left until the end of the subtree is found'''
        curr = self.root
        while curr.left: curr = curr.left
        print(curr.value)
        return
    
    def find_maximum_node(self):
        '''traverse right until the end of the right subtree is found'''
        curr = self.root
        while curr.right: curr = curr.right
        print(curr.value)
        return

    def find_x(self,x:int or float):
        curr = self.root
        while curr:
            if x > curr.value and curr.right: curr = curr.right
            if x < curr.value and curr.left: curr = curr.left
            if x == curr.value: return True
            return False
    

        
        

bst = BST(10)
bst.insert(20)
bst.insert(30)
bst.insert(2)
bst.insert(5)

