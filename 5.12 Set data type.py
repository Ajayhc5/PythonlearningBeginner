# Set(): is used to store the sequence of various types of data where insertion order is not required to preserve
# and duplicates are not allowed they we should go for set data type

'''
* sequence of various types of data, means --- Heterogeneous objects are allowed
* insertion order is not required to preserve
* Duplicates values are not allowed in keys
* Mutable --- add, remove, update, clear, copy the value
* indexing not applicable
* slicing not applicable
* Values should be enclosed be enclosed by flower or curly bracket {}
'''
# wile defining empty set
d = set()
print(type(d))

s = {10, 20, 30, "Ram", 90, 20, 100}
print(s)
print(type(s))

s.add(50)
print(s)

s.remove("Ram")
print(s)
