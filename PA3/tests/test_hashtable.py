import unittest
from gradescope_utils.autograder_utils.decorators import weight
from hashtable import *
import random
class TestHashTable(unittest.TestCase):
    @weight(0.75)
    def test_case1(self):
        """01 Hash Tables: Hash code function"""
        for probe in [0,1,2]:
            for i in range(5,10):
                ht = HashTable(i,probe)
                for j in range(100):
                    self.assertEqual(ht.hashCode(j), j%i)

    @weight(1)
    def test_case2(self):
        """01 Hash Tables: Adding in values into hash table"""
        random.seed(0)
        for probe in [0,1,2]:
            for i in range(5,10):
                ht = HashTable(i,probe)
                for j in range(i):
                    ht[j] = 0
                    self.assertEqual(len(ht), j+1)

    @weight(1.75)
    def test_case3(self):
        """01 Hash Tables: Adding in values into hash table with collisions"""
        random.seed(0)
        for probe in [0,1,2]:
            for i in range(5,10):
                ht = HashTable(i, probe)
                for j in range(i):
                    ht[j*i] = 0
                    self.assertEqual(len(ht), j+1) 

    @weight(1)
    def test_case4(self):
        """01 Hash Tables: Getting values from hash table"""
        random.seed(0)
        for probe in [0,1,2]:
            for i in range(5,10):
                ht = HashTable(i)
                for j in range(i):
                    ht[j] = j
                for j in range(i):
                    self.assertEqual(ht[j],j)

    @weight(1.75)
    def test_case5(self):
        """01 Hash Tables: Getting values from hash table with collisions"""
        random.seed(0)
        for probe in [0,1,2]:
            for i in range(5,10):
                ht = HashTable(i, probe)
                for j in range(i):
                    ht[j*i] = j
                for j in range(i):
                    self.assertEqual(ht[j*i],j)

    @weight(1)
    def test_case6(self):
        """01 Hash Tables: Deleting values from hash table"""
        random.seed(0)
        for probe in [0,1,2]:
            for i in range(5,10):
                ht = HashTable(i, probe)
                for j in range(i):
                    ht[j] = j
                for j in range(i):
                    self.assertEqual(ht[j],j)
                for j in range(i):
                    del ht[j]
                    self.assertEqual(ht[j],None)

    @weight(1.75)
    def test_case7(self):
        """01 Hash Tables: Deleting values from hash table with collisions"""
        random.seed(0)
        for probe in [0,1,2]:
            for i in range(5,10):
                ht = HashTable(i, probe)
                for j in range(i):
                    ht[j*i] = j
                for j in range(i):
                    self.assertEqual(ht[j*i],j)
                for j in range(i):
                    del ht[j*i]
                    self.assertEqual(ht[j*i],None)
                