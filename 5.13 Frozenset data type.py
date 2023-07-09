# Frozenset(): is used to store the sequence of various types of data where insertion order is not required to preserve
# , duplicates are not allowed and Immutable they we should go for set data type

'''
* sequence of various types of data, means --- Heterogeneous objects are allowed
* insertion order is not required to preserve
* Duplicates values are not allowed
* Immutable
* indexing not applicable
* slicing not applicable
* Values should be enclosed be enclosed by flower or curly bracket {}
'''
# wile defining empty set
d = frozenset()
print(type(d))

s = {10, 20, 30, "Ram", 90, 20, 100}
fs = frozenset(s)
print(fs)
print(type(fs))
