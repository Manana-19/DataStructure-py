# Importing my completed modules in here
from structure.array import Array
from structure.hash_table import HashTable
from structure.linked_list import LinkedList
from structure.queue import Queue
from structure.stacks import Stacks
from structure.bst import BST
from structure.graph import Graphs
from algorithms.bubblesort import BubbleSort
from algorithms.selectionsort import selectionSort
from algorithms.insertionsort import InsertionSort
from algorithms.mergeSort import mergeSort
from algorithms.binarySearch import binarySearch
from algorithms.bfs import BFS
from algorithms.dfs import DFSPreOrder, DFSInOrder, DFSPostOrder

# This is a test area


# import numpy as np
# np.random.seed(12)
# a = list(np.random.randint(0, 50, size=10))
# np.random.seed(12)
# b= list(np.random.randint(0, 50, size=10))
# np.random.seed(12)
# c = list(np.random.randint(0, 50, size=11))

# print((a))

# print(InsertionSort(a))

# print(b)
# print(selectionSort(b))

# print(c)
# print(mergeSort(c))

# print(binarySearch(c,49)) # True



a = BST()

a.insert(50)
a.insert(70)
a.insert(2)
a.insert(7)
a.insert(0)
a.insert(55)
a.insert(170)

print('BFS')

print(BFS(a)) # [50,2,70,0,7,55,170]

print('DFS')

print(DFSPreOrder(a.root, [])) # [50,2,0,7,70,55,170]
print(DFSInOrder(a.root, [])) # [0,2,7,50,55,70,170]
print(DFSPostOrder(a.root, [])) # [0,7,2,55,170,70,50]

#            50
#       /         \
#     2             70
#    / \           /  \
#   0   7         55   170