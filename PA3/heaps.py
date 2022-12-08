import heapq
from utils import *

def heapify(arr, isMax = False):
    tree = BinaryTree()
    if isMax == True:
        heapq._heapify_max(arr)
    else:
        heapq.heapify(arr)
    for i in arr:
        tree.addNode(i)
    return tree