from utils import *
import random
import math

class HashTable(DynamicArray):
    def __init__(self, size, probe=0):
        self.data = DynamicArray(size)
        self.size = size
        self.probe = probe
    def hashCode(self, key):
        if self.probe == 0:
            # linear
            return key % self.size
        if self.probe == 1:
            # quadratic
            if self.data[key%self.size] != None:
                for i in range(int(self.size**0.5)):
                    return (key+i^2)%self.size
            else:
                return key % self.size
        if self.probe == 2:
            # random
            random.seed(key)
            if self.data[key % self.size] != None:
                rng = random.random()
                return int((key + rng) % self.size)
            else:
                return key % self.size
    def __getitem__(self, key):
        return self.data[self.hashCode(key)]
    
    def __setitem__(self, key, value):
        self.data[self.hashCode(key)] = value
        #if len(self) > self.get_size() * 0.8:
        #    self.reallocate(self.get_size()*2)
        # reallocate -> copy, need to use hash function instead of just indexing
        
    def __delitem__(self, key):
        self.data[self.hashCode(key)] = None
        
    def reallocate(self, size):
        copy = self.copy()
        self.resize(size)
        for i in copy:
            self.data.append(i)
        
    def resize(self, size):
        self.data = [None]*size
        self.size = size
        return self

    def copy(self):
        ret = StaticArray(self.size)
        for i,v in enumerate(self):
            ret[self.hashCode(i)] = v
        return ret
