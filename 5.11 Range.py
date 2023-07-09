# Range(): Data type means sequence of values or number. mean from value  to value-1

# Important points
'''
* sequence number with in range
* 3 type of forms
* indexing applicable
* slicing applicable
* Immutable (value assignments is not possible or not able to change the value)
'''

# Ex: i need to represent 0 to 9 then (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# Type 1 --- range(n), means n-1, if n = 5 then values are 0, 1, 2, 3, 4, 5.
print('-----form 1------')
x = range(10)  # range(j) --> 0 to j-1
print(type(x))
print(x)
for i in x:
    print(i)

# Type 2 --- range(begin, end) from begin value to end-1
print('-----form 2------')
y = range(0, 6)  # range(i,j) --> i to j-1
print(type(y))
for j in y:
    print(j)

# Type 3 --- range(begin, end, increment/decrement value) from begin value to end-1
# increment value = 1, then 0+1=1, 1+1=2, 2+1=3, .........
print('-----form 3------')
z = range(0, 11, 2)
print(type(z))
for k in z:
    print(k)

# how to append the range values in list
print('-----------')
l = []
r = range(0, 100, 5)

for i in r:
    l.append(i)
print(l)

# Index method
print('-----index------')
w = range(10)
print(w[0])
print(w[5])
print(w[-1])

# Slice method
print('-----slice------')
print(w[1:6])
