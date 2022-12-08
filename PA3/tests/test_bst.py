import unittest
from gradescope_utils.autograder_utils.decorators import weight
from bst import *

class TestBST(unittest.TestCase):
    @weight(0.5)
    def test_case1(self):
        """02 BST: Adding 2 nodes and tolist"""
        tree = BST([]) 
        tree.addNode(1)
        tree.addNode(2)
        self.assertEqual(tree.tolist(),[1,2])

    @weight(0.75)
    def test_case2(self):
        """02 BST: Removing 1 node after adding 2 nodes and tolist"""
        tree = BST([]) 
        tree.addNode(1)
        tree.addNode(2)
        tree.addNode(3)
        tree.removeNode(2)
        self.assertEqual(tree.tolist(),[1,3])

    @weight(0.75)
    def test_case3(self):
        """02 BST: Check height"""
        tree = BST([]) 
        tree.addNode(1)
        tree.addNode(2)
        tree.addNode(3)
        for i in range(1,4):
            self.assertEqual(tree.height(i),4-i)

    @weight(0.75)
    def test_case4(self):
        """02 BST: Check balancefactor"""
        tree = BST([]) 
        tree.addNode(1)
        tree.addNode(2)
        tree.addNode(3)
        for i in range(1,4):
            self.assertEqual(tree.balancefactor(i),3-i)

    @weight(0.75)
    def test_case5(self):
        """02 BST: Construct BST with initial list and tolist"""
        tree = BST([4,2,6,1,7,9,10])
        self.assertEqual(tree.tolist(),[1, 2, 4, 6, 7, 9, 10])

    @weight(1)
    def test_case6(self):
        """02 BST: Check height (sort = True)"""
        tree = BST([4,2,6,1,7,9,10], sort=True) 
        for n,h in zip([4,2,6,1,7,9,10],[1, 2, 3, 1, 1, 2, 1]):
            self.assertEqual(tree.height(n),h)

    @weight(1)
    def test_case7(self):
        """02 BST: Check balancefactor (sort = True)"""
        tree = BST([4,2,6,1,7,9,10], sort=True) 
        for n in [4,2,6,1,7,9,10]:
            self.assertEqual(tree.balancefactor(n),0)

    @weight(1)
    def test_case8(self):
        """02 BST: Check balancefactor with removing (sort = True)"""
        tree = BST([4,2,6,1,7,9,10], sort=True) 
        tree.removeNode(4)
        for n,bf in zip([2,6,1,7,9,10],[1, 0, 0, 0, 0, 0]):
            self.assertEqual(tree.balancefactor(n),bf)

    @weight(1)
    def test_case9(self):
        """02 BST: Check balancefactor with adding (sort = True)"""
        tree = BST([4,2,6,1,7,9,10], sort=True) 
        tree.addNode(0)
        for n,bf in zip([0,4,2,6,1,7,9,10],[0, 0, 1, 1, 1, 0, 0, 0]):
            self.assertEqual(tree.balancefactor(n),bf)

    @weight(0.5)
    def test_case10(self):
        """02 BST: Search"""
        tree = BST([4,2,6,1,7,9,10]) 
        for n in [4,2,6,1,7,9,10]:
            self.assertTrue(tree.search(n))
        self.assertFalse(tree.search(0))

    @weight(1)
    def test_case11(self):
        """02 BST: Search (sort = True)"""
        tree = BST([4,2,6,1,7,9,10], sort=True) 
        for n in [4,2,6,1,7,9,10]:
            self.assertTrue(tree.search(n))
        self.assertFalse(tree.search(0))
