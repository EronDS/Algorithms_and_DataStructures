# implement balance funtion and cleaning (self.nodes())
import copy

class Node:
    def __init__(self,x:int or float):
        self.value = x 
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.root = None
        self.nodes = []
        self.size = 0
    
    def insert(self,new_element):
        if self.root == None: 
            self.root = Node(new_element)
            self.size += 1
        curr = self.root
        while curr:
            if new_element >= curr.value:
                if curr.right: curr = curr.right
                else:
                    curr.right = Node(new_element)
                    self.size += 1
                    return
            if new_element < curr.value:
                if curr.left: curr = curr.left
                else:
                    curr.left = Node(new_element)
                    self.size += 1 
                    return
        return False
    
    def clear(self): self.nodes = [] 
    
    def post_order_traversal(self, node = None):
        'LRV traversal'
        if self.size == 0: return False
        if node == None: curr = self.root
        if node != None: curr = node
        if curr.left != None: self.post_order_traversal(curr.left)
        if curr.right != None: self.post_order_traversal(curr.right)
        if curr: self.nodes.append(curr.value)
        list_nodes = copy.copy(self.nodes)
        return list_nodes

    def in_order_traversal(self,node = None):
        'LVR traversal'
        if self.size == 0: return False
        if node == None: curr = self.root
        if node != None: curr = node
        if curr.left: self.in_order_traversal(curr.left)
        if curr: self.nodes.append(curr.value)
        if curr.right: self.in_order_traversal(curr.right)
        list_nodes = copy.copy(self.nodes)
        return list_nodes

    def pre_order_traversal(self,node = None):
        'VLR traversal'
        if self.size == 0: return False
        if node == None: curr = self.root
        if node != None: curr = node
        if curr: self.nodes.append(curr.value)
        if curr.left: self.pre_order_traversal(curr.left)
        if curr.right: self.pre_order_traversal(curr.right)
        list_nodes = copy.copy(self.nodes)
        return list_nodes

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
    
    def get_parent(self,element):
        ''' Helper function (1) to remove_element (remove given element operation)'''
        curr = self.root
        parent = curr
        if curr == None:return(None,None)
        while curr:
            if element > curr.value:
                parent = curr
                curr = curr.right
            if element < curr.value:
                parent = curr
                curr = curr.left
            if element == curr.value:
                return (parent,curr)
    def get_children(self,node):
        ''' Helper function (2) of remove_element (remove given element operation)'''
        no_children = 0 
        if node.left and node.right: 
            no_children = 2
            return no_children
        if node.right or node.left:
            no_children = 1
            return no_children
        return no_children

    def remove_element(self,element):
        '''Remove Operation'''
        if self.root.value == element:
            t1 = self.root.right.left
            t2 = self.root.left
            self.root = self.root.right
            self.root.right.left = t1
            self.root.left = t2
            return
        parent,node = self.get_parent(element=element)
        if parent is None and node is None: return False
        children = self.get_children(node)
        if children == 0:
            if parent:
                if parent.right: parent.right = None
                elif parent.left: parent.left = None
                else: self.root = None
        if children == 1:
            if node.left: new_node = node.left
            if node.right: new_node = node.right
            if parent.left == node: parent.left=new_node
            if parent.right == node: parent.right=new_node
        
        if children == 2:
            if node.left: new_node = node.left
            parent.left = new_node
        return
    
    def clear(self):
        self.root = None
        self.empty()
        bst = BST()
        return bst
    def empty(self):
        self.size = 0 
        return
    def get_size(self): return self.size




