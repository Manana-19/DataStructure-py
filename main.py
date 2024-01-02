from structure.array import Array
from structure.hash_table import HashTable
from structure.linked_list import LinkedList
# This is a test area
a = LinkedList(10)
a.append(20)
a.append(30)
a.append(40)
a.prepend(50)
print(a.show())
print(a.insert(15,3))
print(a.show())
a.removeValue(30)
print(a.show())
a.RemoveIndex(2)
print(a.show())