# Bytes: data type represent a group of byte numbers with in range(256) are immutable
# allowed only int values are 0 to 255 (256-1) and index is allowed and immutable or not able change the value
# Important points
'''
* sequence number with in range of 0 to 255
* indexing applicable
* slicing applicable
* Immutable (value assignments is not possible or not able to change the value)
'''

x = [20, 30, 50, 255]
b = bytes(x)
print(b)
for i in b:
    print(i)

# Index method
print('-----index------')
print(b[0])

# Slice method
print('-----slice------')
print(b[0:3])
