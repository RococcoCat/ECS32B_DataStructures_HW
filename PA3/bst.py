from utils import BinaryTree, TreeNode
    
class BST(BinaryTree):
    def __init__(self, arr, sort = False):
        # Insert value in arr into the binary search tree.
        # If sort is True, then insert the values in arr in a specified order such that you have a balanced tree
        super().__init__()
        self.sort = sort # if sort = TRUE, make a balanced tree
        for i in arr:
            self.addNode(i)
       
    def addNode(self,data):
        #Adds data with BST property (lesser on left, greater on right subtree)
        if self.root==None: # if root == None, initialize node as root
            self.root = TreeNode(data)
        else:
            node = self.root
            queue = [node] 
            while queue: # traverse until you find an empty node.less or node.more
                cur = queue.pop(0)
                if data < node.data: # if data is less, go left
                    if cur.less == None:
                        cur.less = TreeNode(data)
                    else: # add the visited left node to queue
                        queue.append(cur.less)                    
                elif data > node.data: # if data is greater, go right
                    if cur.more == None:
                        cur.more = TreeNode(data)
                    else:
                        queue.append(cur.more)      
        if self.sort and self.balancefactor(self.root.data) != 0:
            # balance tree
            sorted_array = self.tolist()
            self.root = self.balance(sorted_array)
    def balance(self, arr):
        # balance the tree recursively
        # arr is sorted
        # set root to be middle of array
        # do the same recursively for left and right half of sorted array
        if len(arr) > 0:
            middle = (len(arr))//2
            root = TreeNode(arr[middle])
            root.less = self.balance(arr[:middle])
            root.more = self.balance(arr[middle+1:])
            return root
        else:
            return None
    
    def removeNode(self,data): 
        # traverse until you find node = data
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if data < cur.data:
                prev = cur # assign previous node
                queue.append(cur.less)
            elif data > cur.data:
                prev = cur
                queue.append(cur.more)
            else:
                node = cur
        # remove node
        if node.less and node.more == None: # if no children
            if prev.data < node.data:
                prev.more = None
            else:
                prev.less = None
        elif node.less == None: # if one child
            if prev.data < node.data:
                prev.more = node.more
            else:
                prev.less = None
        elif node.more == None: # if one child
            if prev.data < node.data:
                prev.more = node.less
            else:
                prev.less = None
        #else: # if 2 children
            # get in order successor
                
    def search(self, data):       
        # traverse until you find node = data
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if cur == None:
                return None
            if data < cur.data:
                queue.append(cur.less)
            elif data > cur.data:
                queue.append(cur.more)
            else:
                node = cur
           
        return node
    
    def inorderTraversal(self, node):
        # (left, root, right)
        # recursively get left subtree, root, then right subtree
        # stops if there's node == None (ie if there's nothing left / right)
        res = []
        if node:
            res = self.inorderTraversal(node.less) # base case: none on left
            res.append(node.data) # root
            res = res + self.inorderTraversal(node.more) # base case: none on right
        return res
    
    def tolist(self):
        # load data into list using in order traversal 
        return self.inorderTraversal(self.root)
           
    def height(self,data):
        node = self.search(data)
        return self.maxDepth(node)
    
    def maxDepth(self, node):
        # recursively gets the furthest node in the tree / subtree
        # base case = nothing left / right (in which case None is entered)
        # adds up the height and compares if right / left is larger: returns the larger one
        while node: # base case is root node
            l_height = self.maxDepth(node.less)
            r_height = self.maxDepth(node.more)
            if l_height > r_height:
                return l_height + 1 # +1 b/c base case
            else:
                return r_height + 1 
        return 0
        
    def balancefactor(self,data):
        # get difference btw heights of left and right subtree        
        node = self.search(data)
        l_height = self.maxDepth(node.less)
        r_height = self.maxDepth(node.more)
        bf = abs(l_height - r_height)
        return bf
        
    def __repr__(self):
        return str(self.tolist())