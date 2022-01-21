from urllib.parse import ParseResultBytes


class Node:
    def __init__(self,val):
        self.value = val
        self.right = None
        self.left  = None
        self.left_sub_tree = 0
    pass
class BinomialHeap:
    def __init__(self,heap_size=0,min_node=None,bottom_root=0):
        self.size = heap_size
        self.bottom_root = bottom_root
        self.min_node = min_node
    def mergeHeaps(self,other):
        pass
    def deleteNode(self):
        pass
    def insertNode(self):
        pass
    def decreaseValue(self):
        pass
    def increaseValue(self):
        pass
    
