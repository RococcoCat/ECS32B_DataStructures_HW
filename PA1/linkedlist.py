from utils import Node, Collections, StaticArray

class LinkedList(Collections):
    def __init__(self, isSet = False, isDoubly = False, isCircular = False):
        super(LinkedList,self).__init__()
        self.head = None 
        self.isSet = isSet
        self.isDoubly = isDoubly
        self.isCircular = isCircular       
        
        
    def __getitem__(self, index):        
        if self.head == None:
            return None
        cur = self.head
        if index <= self.get_size():
            for i in range(index):
                cur = cur.next
            return cur
        else:
            for i in range(self.get_size()-1):
                cur = cur.next
            return cur


    def __setitem__(self, index, value):
        # can be adding to the front, back, or middle
        # if front: need to make new head
        # size += 1
        
        if self.head == None: # means linked list is empty
            self.head = Node(value)
        elif index == 0: # adding value to the front
            new_head = Node(value) # Create a node
            new_head.next = self.head # point node to the original head
            self.head = new_head # set new_head to be the new head
            if self.isCircular == True: # set pointer of tail to the new head
                self[get_size()-1].next = self.head 
            if self.isDoubly: # point old head to new head
                self[1].prev = new_head
            
        elif index >= self.get_size(): # Appending (adding value to the end)
            # traverse linked list and set last node to point to a new node
            # __getitem__() = lis[0]
            # __setitem__() = lis[0] = 2
            cur = self[self.get_size()-1]
            cur.next = Node(value) 
            if self.isDoubly:
                new_node = cur.next
                new_node.prev = cur
                
        else: # if adding value in the middle    
            # 1. for loop from head to index
            # 2. make a new node w/ value and next pointing to node at next index
            # 3. point old node at that index to the new node
            # 4. if isDoubly is true, need to point new node.prev to old node and next_node.prev to the new node
            new_node = Node(value)
            cur = self.head
            for i in range(index-1):
                cur = cur.next
                break
            next_node = cur.next
            new_node.next = cur.next
            cur.next = new_node
            if self.isDoubly == True:
                new_node.prev = cur
    
                  

    def __delitem__(self, index):
        if self.head==None:
            return
        elif index==0: # removing from the front
            self.head = self.head.next # set next node to be new head
        elif index == self.get_size()-1: 
            cur = self[self.get_size()-2] # get second to last node
            cur.next = None # point it to None
        else:
            cur = self[index - 1]
            cur.next = self[index + 1]
         


    def append(self, value):
        # add new node at tail if adding at the end
        # need to change pointers if adding in the middle
        new_node = Node(value)
        cur = self.head # always start with the head
        if cur == None:
            self.head = new_node
        else:
            while cur.next != None: # traverse until last node
                cur = cur.next 
            cur.next = new_node # set next node to be one after last
            if self.isDoubly == True:
                new_node.prev = cur
                
    def extend(self, arr):
        # arr is static
        cur = self.head # always start with the head
        if cur == None:
            self.head = new_node
        else:
            while cur.next != None: # traverse until last node
                cur = cur.next
            for i in arr:
                new_node = Node(arr[i])
                cur.next = new_node # set last node to point to first of arr
                cur = cur.next                            
                    

    def remove(self, value):
        # 3 scenarios removing from front, middle, end
        # if from the front, need to set new head
        cur = self.head
        if cur == None:
            return self
        elif cur.data == value:
            self.head = cur.next
        else:
            while cur.next != None:
                x = cur
                cur = cur.next 
                if cur.data == value:
                    pass

    def argwhere(self, value):
        result = StaticArray(2)
        for index, element in enumerate(self):
            if element.data == value:
                result.append(index)
        return result

    def __len__(self): # exactly equal to size
        count = 0
        cur = self.head # start from head node
        ret = str(cur)
        while True:
            cur = cur.next # go to the next node
            count += 1
            if cur==None: # break when you reach the end
                break
        return count

    def get_size(self):
        count = 0
        cur = self.head # start from head node
        ret = str(cur)
        while True:
            cur = cur.next # go to the next node
            count += 1
            if cur==None: # break when you reach the end
                break
        return count

    def __eq__(self, arr):
        # when are 2 collections equal if they share all the same values in the same order, 
        # size doesn't matter
        for i, j in zip(self, arr):
            if i != j:
                return False
        return True

    def __repr__(self):
        #Not required but useful for debugging
        cur = self.head # start from head node
        ret = str(cur)
        while True:
            cur = cur.next # go to the next node
            if cur==None: # break when you reach the end
                break
            ret += "->" + str(cur)
        return ret
    def __iter__(self):
        cur = self.head # start from head node
        while True:
            yield cur
            cur = cur.next # go to the next node
            if cur==None: # break when you reach the end
                break
