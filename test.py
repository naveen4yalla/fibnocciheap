

 
 
class Node:
    
 
    def __init__(self, val):
        self.val = val
        # Number of nodes in left subtree
        self.left_tree_size = 0
        self.left = None
        self.right = None
        self.parent = None
 
    def mergeTrees(self, other):
        print("gggggg")
        assert self.left_tree_size == other.left_tree_size, "Unequal Sizes of Blocks"
 
        if self.val < other.val:
            print(self.parent,other.parent)
            other.left = self.right
            other.parent = None
            if self.right:
                self.right.parent = other
            self.right = other
            self.left_tree_size = self.left_tree_size * 2 + 1
            return self
        else:
            self.left = other.right
            self.parent = None
            if other.right:
                other.right.parent = self
            other.right = self
            other.left_tree_size = other.left_tree_size * 2 + 1
            return other
 
 
class BinomialHeap:
 
    
 
    def __init__(self, bottom_root=None, min_node=None, heap_size=0):
        self.size = heap_size
        self.bottom_root = bottom_root
        self.min_node = min_node
 
    def mergeHeaps(self, other):
        
 
        # Empty heaps corner cases
        if other.size == 0:
            return
        if self.size == 0:
            self.size = other.size
            self.bottom_root = other.bottom_root
            self.min_node = other.min_node
            return
        # Update size
        self.size = self.size + other.size
 
        # Update min.node
        if self.min_node.val > other.min_node.val:
            self.min_node = other.min_node
        # Merge
 
        # Order roots by left_subtree_size
        combined_roots_list = []
        i, j = self.bottom_root, other.bottom_root
        while i or j:
            if i and ((not j) or i.left_tree_size < j.left_tree_size):
                combined_roots_list.append((i, True))
                i = i.parent
            else:
                combined_roots_list.append((j, False))
                j = j.parent
        # Insert links between them
        for i in range(len(combined_roots_list) - 1):
            if combined_roots_list[i][1] != combined_roots_list[i + 1][1]:
                combined_roots_list[i][0].parent = combined_roots_list[i + 1][0]
                combined_roots_list[i + 1][0].left = combined_roots_list[i][0]
        # Consecutively merge roots with same left_tree_size
        i = combined_roots_list[0][0]
        while i.parent:
            if (
                (i.left_tree_size == i.parent.left_tree_size) and (not i.parent.parent)
            ) or (
                i.left_tree_size == i.parent.left_tree_size
                and i.left_tree_size != i.parent.parent.left_tree_size
            ):
 
                # Neighbouring Nodes
                previous_node = i.left
                next_node = i.parent.parent
 
                # Merging trees
                i = i.mergeTrees(i.parent)
 
                # Updating links
                i.left = previous_node
                i.parent = next_node
                if previous_node:
                    previous_node.parent = i
                if next_node:
                    next_node.left = i
            else:
                i = i.parent
        # Updating self.bottom_root
        while i.left:
            i = i.left
        self.bottom_root = i
 
        # Update other
        other.size = self.size
        other.bottom_root = self.bottom_root
        other.min_node = self.min_node
 
        # Return the merged heap
        return self
 
    def insert(self, val):
        """
        insert a value in the heap
        """
        if self.size == 0:
            self.bottom_root = Node(val)
            self.size = 1
            self.min_node = self.bottom_root
            print("hello")
        else:
            # Create new node
            new_node = Node(val)
            print("mac")
            # Update size
            self.size += 1
 
            # update min_node
            if val < self.min_node.val:
                self.min_node = new_node
            # Put new_node as a bottom_root in heap
            self.bottom_root.left = new_node
            print(self.bottom_root.left.val)
            new_node.parent = self.bottom_root
            print(new_node.parent.val)
            self.bottom_root = new_node
            print(self.min_node.val,self.bottom_root.val,self.bottom_root.parent.val)
            # Consecutively merge roots with same left_tree_size
            while (
                self.bottom_root.parent
                and self.bottom_root.left_tree_size
                == self.bottom_root.parent.left_tree_size
            ):
                print("hallo")
                # Next node
                next_node = self.bottom_root.parent.parent
                print(next_node)
                # Merge
                self.bottom_root = self.bottom_root.mergeTrees(self.bottom_root.parent)
 
                # Update Links
                self.bottom_root.parent = next_node
                self.bottom_root.left = None
                if next_node:
                    next_node.left = self.bottom_root
 
    def peek(self):
        """
        return min element without deleting it
        """
        return self.min_node.val
 
    def isEmpty(self):
        return self.size == 0
 
    def deleteMin(self):
        """
        delete min element and return it
        """
        # assert not self.isEmpty(), "Empty Heap"
 
        # Save minimal value
        min_value = self.min_node.val
 
        # Last element in heap corner case
        if self.size == 1:
            # Update size
            self.size = 0
 
            # Update bottom root
            self.bottom_root = None
 
            # Update min_node
            self.min_node = None
 
            return min_value
        # No right subtree corner case
        # The structure of the tree implies that this should be the bottom root
        # and there is at least one other root
        if self.min_node.right is None:
            # Update size
            self.size -= 1
 
            # Update bottom root
            self.bottom_root = self.bottom_root.parent
            self.bottom_root.left = None
 
            # Update min_node
            self.min_node = self.bottom_root
            i = self.bottom_root.parent
            while i:
                if i.val < self.min_node.val:
                    self.min_node = i
                i = i.parent
            return min_value
        # General case
        # Find the BinomialHeap of the right subtree of min_node
        bottom_of_new = self.min_node.right
        bottom_of_new.parent = None
        min_of_new = bottom_of_new
        size_of_new = 1
 
        # Size, min_node and bottom_root
        while bottom_of_new.left:
            size_of_new = size_of_new * 2 + 1
            bottom_of_new = bottom_of_new.left
            if bottom_of_new.val < min_of_new.val:
                min_of_new = bottom_of_new
        # Corner case of single root on top left path
        if (not self.min_node.left) and (not self.min_node.parent):
            self.size = size_of_new
            self.bottom_root = bottom_of_new
            self.min_node = min_of_new
            # print("Single root, multiple nodes case")
            return min_value
        # Remaining cases
        # Construct heap of right subtree
        newHeap = BinomialHeap(
            bottom_root=bottom_of_new, min_node=min_of_new, heap_size=size_of_new
        )
 
        # Update size
        self.size = self.size - 1 - size_of_new
 
        # Neighbour nodes
        previous_node = self.min_node.left
        next_node = self.min_node.parent
 
        # Initialize new bottom_root and min_node
        self.min_node = previous_node or next_node
        self.bottom_root = next_node
 
        # Update links of previous_node and search below for new min_node and
        # bottom_root
        if previous_node:
            previous_node.parent = next_node
 
            # Update bottom_root and search for min_node below
            self.bottom_root = previous_node
            self.min_node = previous_node
            while self.bottom_root.left:
                self.bottom_root = self.bottom_root.left
                if self.bottom_root.val < self.min_node.val:
                    self.min_node = self.bottom_root
        if next_node:
            next_node.left = previous_node
 
            # Search for new min_node above min_node
            i = next_node
            while i:
                if i.val < self.min_node.val:
                    self.min_node = i
                i = i.parent
        # Merge heaps
        self.mergeHeaps(newHeap)
 
        return min_value
 
    def preOrder(self):
        """
        Returns the Pre-order representation of the heap including
        values of nodes plus their level distance from the root;
        Empty nodes appear as #
        """
        # Find top root
        top_root = self.bottom_root
        while top_root.parent:
            top_root = top_root.parent
        # preorder
        heap_preOrder = []
        self.__traversal(top_root, heap_preOrder)
        return heap_preOrder
 
    def __traversal(self, curr_node, preorder, level=0):
        """
        Pre-order traversal of nodes
        """
        if curr_node:
            preorder.append((curr_node.val, level))
            self.__traversal(curr_node.left, preorder, level + 1)
            self.__traversal(curr_node.right, preorder, level + 1)
        else:
            preorder.append(("#", level))
 
    def __str__(self):
        """
        Overwriting str for a pre-order print of nodes in heap;
        Performance is poor, so use only for small examples
        """
        if self.isEmpty():
            return ""
        preorder_heap = self.preOrder()
 
        return "\n".join(("-" * level + str(value)) for value, level in preorder_heap)
 
 
# Unit Tests
s=BinomialHeap()
s.insert(19)
s.insert(15)
print(s.preOrder())
