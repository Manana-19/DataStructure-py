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
# This is a test area

a=[]

for x in range(5,9):
    a.append(x)

for i in range(0,5,2):
    a.append(i)

print(a)
print(selectionSort(a))

