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
# This is a test area


import numpy as np
np.random.seed(12)
a = list(np.random.randint(0, 50, size=10))
np.random.seed(12)
b= list(np.random.randint(0, 50, size=10))
np.random.seed(12)
c = list(np.random.randint(0, 50, size=11))

print((a))

print(InsertionSort(a))

print(b)
print(selectionSort(b))

print(c)
print(mergeSort(c))

print(binarySearch(c,49)) # True