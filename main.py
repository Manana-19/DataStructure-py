from structure.array import Array
from structure.hash_table import HashTable
from structure.linked_list import LinkedList
from structure.queue import Queue
from structure.stacks import Stacks
from structure.bst import BST
# This is a test area

a=BST()
for i in range(3,6):
    a.insert(i)
for i in range(3):
    a.insert(i)
print(a.root)
print(a.lookup(5))