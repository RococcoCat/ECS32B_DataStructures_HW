from utils import *
from arrays import *
from linkedlist import *



class StackOrQueue():
    def __init__(self, useLinkedList = False, isQueue=False):
        """This function will initialize this collection.
        Implement this collection is a singly linked list if isLinked = True. Otherwise, use a
        dynamic array.
        To determine whether this collection is a queue or stack, use the isQueue argument.
        """
        self.isQueue = isQueue
        self.useLinkedList = useLinkedList
        if self.useLinkedList:
            self.data = LinkedList()
        else:
            self.data = DynamicArray(10)
           
        
    def peek(self):
        # Return the first value in the collection but do not remove the value.
        return self.data[0]

    def push(self, value):
        # Add the value into the collection.
        # Treat this as enqueue if isQueue is used.
        if self.isQueue:
            self.data.append(value)            
        else:
            self.data[0] = value

    def pop(self):
        # Remove and return the first value from the collection.
        # If collection is empty, return None.
        if len(self.data) == 0:
            return None
        else:
            first = self.data[0]
            del self.data[0]
            return first
    
    def __repr__(self):
        print(self.data) #Not graded but useful for debugging
    
    def __len__(self):
        count = 0
        for i in self:
            count += 1
        return count
            
    def __iter__(self):
        # Yield the next value (Used for iterable functions)
        for i in self.data:
            yield i
        # yield statement returns a generator object to the one who calls the function which contains yield, instead of simply returning a value
