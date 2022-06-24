from copy import copy
class Array:
    def __init__(self,size:int=100):
        self.n = 0
        self.size = size # size of array 
        self.array = [None]*self.size # Initialize array with None elements
    def insert(self,index:int,new_element: int or float):
        ''' Insert an element at predefined index Best Case: O(I), Worst Case: O(n)'''
        arr = copy(self.array) # essential to be an copy (avoid unwanted alteration of self.array)
        self.n += 1 # increment the no of elements
        if self.n + 1 == self.size: # if array is full ... create an new array with 2x larger
            self.size *= 2 
            self.array = [None]*self.size
            for i in range(len(arr)): self.array[i] = arr[i] # copy elements from old array (full) to new array (larger)
        arr = copy(self.array) 
        self.array[index] = new_element # add new element at specified index
        if arr[index] != None: # ntif index already has an eleme, insert new element at the position and slide array
            self.array[:index] = arr[:index]
            self.array[index+1:] = arr[index:len(arr)-1]
        return self.array
    def append(self,new_element:int or float):
        ''' Insert element at the end of list (contiguous) Best Case: O(I), Worst Case: O(n)'''
        return self.insert(index=self.n+1,new_element=new_element) # insert new element at the end of array (contiguous)
    def find(self,element:int or float) -> bool:
        ''' return True if element found in list, return False otherwise '''
        for i in self.array: # search | Worst Case: O(n) -- linear time
            if i == element:return True
        return False
    def binary_search(self,element:int or float):
        array = copy(self.array) # better time-complexity -- O(log n) -- dividing by 2 the number of possible elements at each generation
        array = [i for i in array if i != None]
        l,r = 0,len(array)-1
        if element > array[-1] or element < array[0]:return False
        while l <= r:
            m = (l+r)//2
            if element == array[m]:return True
            if element < array[m]: r = m - 1
            if element > array[m]: l = m + 1
        return False
    def delete(self,index:int):
        """ delete an element given index """
        if len(self.array) < index: return False
        self.array[index:] = self.array[index+1:] + [None] # delete  
        return self.array
    def remove(self,element:int or float):
        ''' delete an element from its value '''
        ix = 0 
        for i in self.array:# find index of given value   
            if i == element:return self.delete(ix)  # call function at given indexes
            ix+=1
        return False
    def pop(self):
        ''' delete the last element (O(I)) - Constant Time''' # remove last element from array
        self.array[-1] = None
        return self.array

my_array = Array(3)
print(my_array.insert(1,10))
print(my_array.insert(1,20))
print(my_array.insert(1,5))
print(my_array.append(20))
print(my_array.append(35))
print(my_array.append(100))
print(my_array.remove(20))
print(my_array.insert(-1,1000))
print(my_array.pop())