# List(): is used to store the sequence of various types of data. this data type is Mutable

# we want to represent a group of values as single entity where insertion order required to preserve and duplicates are
# allowed they we should go for list data type

'''
* sequence of various types of data, means --- Heterogeneous objects are allowed
* insertion order required to preserve
* Duplicates values are allowed
* Mutable --- Append, insert, delete, update the value
* indexing applicable
* slicing applicable
* Values should be enclosed be enclosed by square bracket []
'''

x = []
x.append(10)
x.append(20)
x.append("ajay")
x.append(50)
x.append("ram")
print(x)

x.insert(1, 15)
print(x)

del x[1]
print(x)

x[2] = "AJAY"
print(x)

# Index & slice
print(x[0])
print(x[-1])
print(x[1:4])

