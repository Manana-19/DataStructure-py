from structure.array import Array
from structure.hash_table import HashTable
from structure.linked_list import LinkedList
from structure.queue import Queue
from structure.stacks import Stacks
# This is a test area
a=Stacks('a')
b=Queue('a')

for i in range(10):
    a.push(i)
    b.push(i)

print(a.show())
print(b.show())

print(a.pop())
print(b.pop())

print(a.show())
print(b.show())