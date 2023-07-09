
# Dictionary dict(): is used to store the sequence of various types of data in a group of values as key-value pair
# then we should go for dict data type

'''
* Dictionary it is key-value pair
* sequence of various types of data, means --- Heterogeneous objects are allowed
* insertion order is not required to preserve
* Key - Duplicates values are not allowed and immutable
* Mutable --- n[key]="value"
* indexing not applicable
* slicing not applicable
* Values should be enclosed be enclosed by flower or curly bracket {}
'''

d = {1: "Arjun", 2: "Bharath", 3: "Chandu"}
print(type(d))
print(d)
print(d[1])
print(d.keys())
d[4] = "Ram"
print(d)

