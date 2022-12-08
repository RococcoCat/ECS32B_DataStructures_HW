from utils import StaticArray
from utils import Collections

class DynamicArray(StaticArray):
    def __init__(self, size, isSet = False):
        # super(DynamicArray,self).__init__(size)
        self.isSet = isSet
        self.size = size
        self.data = [None] * self.size
        # Constructor for collection with size empty slots.
        # To determine whether this collection will enforce the set property, use isSet argument.
        # if isSet == True, no duplicate elements
      
    #def __getitem__(self, index):
    #    super().__getitem__(index)

    def __setitem__(self, index, value):
        # if index == None, add value at index
        if self.isSet == True and value in self:
            return self
        if self[index]==None:
            for i,v in enumerate(self):
                if v == None:
                    super().__setitem__(i,value)
                    break
        # else: shift everything from index to len right by 1, and insert value at index
        else:
            for i in range(self.get_size()-1,index,-1):
                super().__setitem__(i,self[i-1])
            super().__setitem__(index,value)
            
        # Double the size if more than 80% is occupied. Only double upon adding new items.
        if len(self) > self.get_size() * 0.8:
            self.reallocate(self.get_size()*2)
          
    def __delitem__(self, index):
        # Remove the element at index of the collection
        if self[index] == None: # Delete empty slot
            return self
        elif index == self.size-1: # Delete last element
            del self[index]
        else: # Delete element btw other elements and shift over other values from right to left starting at index
            size = self.get_size() - 1
            for i in range(index, size):
                super().__setitem__(i,self[i+1])
            super().__setitem__(size,None)
            
        # Halve the size if less than 20% is occupied. Only halve upon removing items.
        if self.__len__() < 0.2 * self.get_size():
            self.reallocate(round(self.get_size() * 0.5))
            
    def append(self, value):
        # Add value to collection at the next open slot.
        if self.isSet == True and value in self:
            return self
        for i,v in enumerate(self):
            if v == None:
                super().__setitem__(i,value)
                break
        if self.__len__() > 0.8 * self.get_size():
            self.reallocate(self.get_size() * 2)

    def extend(self, arr):
        # Append the values of arr to the collection.
        for i in arr:
            self.append(i)
        if self.__len__() > 0.8 * self.get_size():
            self.reallocate(self.get_size() * 2)

    def remove(self, value):
        # Remove the first instance of the value from collection.
        
        for index, element in enumerate(self):
            if element == value:
                del self[index]
                # self[index] = None
                # del self[index] , getitem broken rn, should work if fixed
                #for i in range(index, self.__len__()-1):
                #    super().__setitem__(i,self[i+1])
                break

            

    def argwhere(self, value):
        # Find the value in your collection.
        # Returns a StaticArray with elements containing the indices where the value exists.
     
        result = StaticArray(len(self))
        for index, element in enumerate(self):
            if element == value:
                result.append(index)
        return result

    def __eq__(self, arr) -> bool:
        # Check whether arr is equivalent to this collection
        # Two collections are equal only if they share all the same values, in the correct order.
        # Their sizes do not matter
        """
            for v1, v2 in zip(self, arr):
                if v1 != v2:
                    return False
            return True
        else:
            return False
        """
                   
        if type(arr) == StaticArray or type(arr) == DynamicArray: 
            for i, v in enumerate(self):
                if v != arr[i]:
                    return False
            return True
        else:
            return False



    def __len__(self):
        # Return the number of total slots.
        # number of elements that are not None
        count = 0
        for i in self:
            if i != None:
                count += 1
        return count

    def get_size(self):
        # Return the number of elements in this collection. (includes None)
        return self.size
    
    def __repr__(self):
     #Not required but useful for debugging
        output = []
        for i in self:
            output.append(i)
        print(output)
        
    def __eq__(self, arr):
        # Check whether arr is equivalent to this collection
        # Two collections are equal only if they share all the same values, in the correct order.
        # Their sizes do not matter
        
        x = zip(self, arr)
        if type(arr) == StaticArray:
            for i in x:
                for a,b in i:
                    if a != b:
                        return False
            return True 
        else:
            return False


    def __iter__(self):
        # Yield the next value (Used for iterable functions)
        for i in self.data:
            yield i
        # yield statement returns a generator object to the one who calls the function which contains yield, instead of simply returning a value



    def reallocate(self, size):
        # Reallocate your collection to a new collection with size.
        # This is where you transfer over your existing content.
        # This function should call resize

        # Follow this resizing rule:
            # Double the size if more than 80% is occupied. Only double upon adding new items.
            # Halve the size if less than 20% is occupied. Only halve upon removing items

        # 1. Resize 2. Copy over data
        """
        percent_occupied = (self.get_size() / size)
        if percent_occupied > 0.8:
            size *= 2
        elif size < 0.2:
            size *= 0.5
        else:
            size = size
        """
        copy = self.copy()
        self.resize(size)
        for i in copy:
            self.append(i)    
            
    def resize(self, size):
        """
        Do not modify this function.
        This function will enable you to resize your structure.
        This function is destructive! Be careful.
        """
        self.data = [None]*size
        self.size = size
        return self