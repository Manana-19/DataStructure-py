from structure.array import Array
from structure.hash_table import HashTable
from structure.linked_list import LinkedList
from structure.queue import Queue
from structure.stacks import Stacks
from structure.bst import BST
from structure.graph import Graphs
# This is a test area

a = Graphs()
for i in range(5):
    a.addNode(i)
a.addEdge(1,2)
a.addEdge(1,3)
print(a.showConnections())