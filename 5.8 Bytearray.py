# Bytearray(): data type is exactly same as bytes data type except immutable
# allowed only int values are 0 to 256 and index is allowed and mutable or able change the change the existing value
'''
* sequence number with in range of 0 to 255
* indexing applicable
* slicing applicable
* Mutable (value assignments is not possible or not able to change the value)
'''

# Ex
x = [20, 30, 50, 255]
b = bytearray(x)
for i in b:
    print(i)

# Mutable
print('-----mutable------')
b[0] = 100
b.append(55)
del b[1]
for f in b:
    print(f)

# Index method
print('-----index------')
print(b[0])
print(b[-1])

# Slice method
print('-----slice------')
print(b[0:2])
