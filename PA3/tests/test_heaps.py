import unittest
from gradescope_utils.autograder_utils.decorators import weight
from heaps import *

class TestHeaps(unittest.TestCase):
    @weight(0.75)
    def test_case1(self):
        """04 Heaps: Heapify 1 (min)"""
        tree = heapify([5,1,2,3,5],False)
        self.assertEqual(tree.tolist(), [1, 3, 2, 5, 5])

    @weight(0.75)
    def test_case2(self):
        """04 Heaps: Heapify 1 (max)"""
        tree = heapify([5,1,2,3,5],True)
        self.assertEqual(tree.tolist(), [5, 5, 2, 3, 1])

    @weight(0.75)
    def test_case3(self):
        """04 Heaps: Heapify 2 (min)"""
        tree = heapify([-1,2,5,20,1.2],False)
        self.assertEqual(tree.tolist(), [-1, 1.2, 5, 20, 2])
        
    @weight(0.75)
    def test_case4(self):
        """04 Heaps: Heapify 2 (max)"""
        tree = heapify([-1,2,5,20,1.2],True)
        self.assertEqual(tree.tolist(), [20, 2, 5, -1, 1.2])